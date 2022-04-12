import asyncio
from fastapi import UploadFile, File
import requests
import json

from .classes.fileupload import FileHandler


def file_upload(uploaded_file: UploadFile):
    fh = FileHandler(uploaded_file)
    fh.read_json_file()
    fh.add_transaction()
    fh.add_addresses()
    fh.add_records()
    fh.make_household()
    fh.create_report()
    return fh.export_report()
