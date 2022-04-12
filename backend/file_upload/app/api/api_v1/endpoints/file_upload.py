from fastapi import APIRouter, UploadFile, File
import json

from ....service.file_upload import file_upload

router = APIRouter(tags=["File Services"], prefix="/file_service")


@router.post("/upload_file")
def read_file(uploaded_file: UploadFile = File(...)):
    return file_upload(uploaded_file)
