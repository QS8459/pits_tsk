from fastapi import APIRouter, Depends, UploadFile, File
from src.core.service.file.file import get_file_service
from src.core.service.account.authorization import get_user
from src.core.schemas.file.file import FileResponseSchema
from src.utils.utils import save_file
from src.conf.log import log

file_api:APIRouter = APIRouter(prefix='/file', tags=['File'])


@file_api.post("/upload/", response_model=FileResponseSchema)
async def upload_file(
        file: UploadFile = File(...),
        user_head = Depends(get_user),
        file_service=Depends(get_file_service)
):
    log.info(user_head)
    save_file(file)
    result = await file_service.add(title=file.filename, path=f'/app/uploaded/{file.filename}', type=file.content_type, owner=user_head.get('uid'))
    return result

