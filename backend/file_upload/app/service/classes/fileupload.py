from fastapi import UploadFile, File
from fastapi.responses import FileResponse
import json
import requests
import pandas as pd
import csv
import os


class FileHandler:

    URI = r"http://localhost:8000"
    URI_record = rf"{URI}/record/"
    URI_transaction = rf"{URI}/transaction/"
    URI_address = rf"{URI}/address/"

    def __init__(self, uploaded_file: UploadFile):
        self.uploaded_file = uploaded_file
        self.parsed_content = None
        self.transaction_id = None
        self.households = None
        self.report_path = f"{os.getcwd()}\static\\report.csv"
        print(self.report_path)

    def read_json_file(self):
        content = self.uploaded_file.file.read()
        self.parsed_content = json.loads(content)

    def add_transaction(self):
        payload = {"file_name": f"{self.uploaded_file.filename}"}
        request = requests.post(url=FileHandler.URI_transaction, json=payload)
        response = request.json()
        self.transaction_id = response["id"]

    def add_addresses(self):
        address_keys = ["address1", "city", "state", "zip"]
        for record in self.parsed_content:
            address = {}
            for k, v in record.items():
                if k in address_keys:
                    address[k] = v
            try:
                print(address)
                address_id = self._add_address(address)
                record["address_id"] = address_id
                print(address_id)
            except:
                address_id = self._get_address_id(address)
                record["address_id"] = address_id
                print(address_id)

    def add_records(self):
        for record in self.parsed_content:
            self._add_record(record)

    def _add_record(self, record: dict):
        payload = {
            "name": record["name"],
            "address_id": record["address_id"],
            "company": record["company"],
            "transaction_id": self.transaction_id,
        }
        try:
            request = requests.post(FileHandler.URI_record, json=payload)
        except:
            pass

    def _add_address(self, address: dict):
        request = requests.post(url=FileHandler.URI_address, json=address)
        response = request.json()
        return response["id"]

    def _get_address_id(self, address: dict):
        url = f"{FileHandler.URI_address}params/?address1={address['address1']}&city={address['city']}&state={address['state']}&zip={address['zip']}"

        request = requests.get(url)
        response = request.json()
        return response["id"]

    def make_household(self):
        data = self._get_all_db_records()
        df = pd.json_normalize(data)
        pt = df.pivot_table(index="address.id", values="name", aggfunc="count")
        pt = pt[pt.name > 1]
        householded_address_ids = list(pt.index)
        for address_id in householded_address_ids:
            self._update_household_address(address_id)
        self.households = len(householded_address_ids)

    def _get_all_db_records(self):
        records = requests.get(url=FileHandler.URI_record)
        contents = records.json()
        return contents

    def _update_household_address(self, address_id):
        payload = {"is_household": True}
        request = requests.put(f"{FileHandler.URI_address}{address_id}", json=payload)

    def create_report(self):
        records_added = self._count_records_by_transaction_id()
        upload_date = self._get_transaction_time()
        report = [
            ["file_name", self.uploaded_file.filename],
            ["records_added", records_added],
            ["householded_records", self.households],
            ["transaction_time", upload_date],
        ]
        with open(self.report_path, "w") as csvfile:
            writer = csv.writer(csvfile)
            for record in report:
                writer.writerow(record)

    def export_report(self):
        return FileResponse(
            self.report_path, headers={"Content-Type": "multipart/form-data"}
        )

    def _count_records_by_transaction_id(self):
        request = requests.get(
            f"{FileHandler.URI_record}count_transaction/{self.transaction_id}"
        )
        response = request.json()

    def _get_transaction_time(self):
        request = requests.get(f"{FileHandler.URI_transaction}{self.transaction_id}")
        response = request.json()
        return response["upload_date"]
