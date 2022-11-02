from __future__ import annotations

import secrets
import sys
from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

USERNAME = "ubuntu"
PASSWORD = "debian"

app = FastAPI()

security = HTTPBasic()


@app.get("/greetings")
async def greetings(
    credentials: HTTPBasicCredentials = Depends(security),
) -> dict:
    if not (
        secrets.compare_digest(credentials.username, USERNAME)
        and secrets.compare_digest(credentials.password, PASSWORD)
    ):
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail=HTTPStatus.UNAUTHORIZED.description,
        )

    return {
        "ok": True,
        "status_code": HTTPStatus.OK,
        "message": "Hello from Fly!",
        "python_version": sys.version,
    }
