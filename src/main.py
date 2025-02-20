from src.conf.log import log
from src.api import api
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse, Response
from fastapi.requests import Request
from src.middleware.log_middleware import logger_middle


@asynccontextmanager
async def lifespan(_app: FastAPI):
    try:
        from src.conf.db_config import engine
        yield
        await engine.dispose()
    except Exception as e:
        raise e


app = FastAPI(
    lifespan=lifespan,
)


app_cors=CORSMiddleware(
    app=app,
    allow_methods=("GET", "POST", "PUT", "PATCH"),
    allow_headers=(),
    allow_origins=['*'],
)


origins = ["*"]


@app.on_event('startup')
async def add_middleware():
    app.add_middleware(
        app_cors,
        # allow_origins=origins,
        # allow_credentials=True,
    )
app.middleware('http')(logger_middle)


@app.get('/')
async def home(response: Response, request: Request):
    log.warn(request.headers)
    return JSONResponse(
        content={"detail": "Welcome to home page"},
        status_code=status.HTTP_200_OK
    )

app.include_router(api)
