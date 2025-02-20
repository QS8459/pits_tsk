from fastapi import UploadFile
from src.conf.log import log
import shutil


def save_file(file: UploadFile):
    try:
        with open(f"/app/uploaded/{file.filename}", "wb") as f_writer:
            shutil.copyfileobj(file.file, f_writer)

    except (shutil.Error, shutil.ExecError):
        log.error("Having issue with saving file")
