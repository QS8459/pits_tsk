from src.conf.log import log
from fastapi import (
    Request,
    Response,
    status,
    HTTPException,
)
from fastapi.responses import JSONResponse


async def logger_middle(request: Request, call_next):
    try:
        log.info("Middleware triggered")
        response = await call_next(request)
    except HTTPException as e:
        log.error(f'Exception: {e}')
        return JSONResponse(
            status_code=500,
            content={"detail": "Something went wrong"}
        )
    return response
