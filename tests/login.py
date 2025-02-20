from fastapi.testclient import TestClient
from src.conf.log import log
from io import BytesIO
from src.main import app
import pytest
#Had no time to write tests
client = TestClient(
    app=app,
    headers={
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImV4YW1wbGUyQGVtYWlsLmRvbWFpbiIsInBhc3N3b3JkIjoiUGFzc3dvcmRfMSEiLCJ1aWQiOiIyZDQ0MTI0Zi1jMTM4LTQ5YjUtODdhZC1iOGYwOTE2OGVjMWUiLCJleHAiOjE3NDAwMTE2MzN9.ixilzajwoB4Dun45vZZ2XrqnxpkKM99-vDbzBfc0H9E'
    }
)


def test_upload_file():
    file = open('main.py', 'rb')
    files = {"file": ("main.py", file, "text/plain")}  # Create test file

    response = client.post("http://127.0.0.1:5000/api/v1/file/upload/", files=files)  # Send the request
    log.error(response.json())
    assert response.status_code == 200
    json_resp = response.json()

    # assert json_resp["size"] == len(file)