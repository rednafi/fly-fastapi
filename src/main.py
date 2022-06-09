import secrets
from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()


@app.get("/greetings")
async def greetings(
    credentials: HTTPBasicCredentials = Depends(security),
) -> dict:
    if not (
        secrets.compare_digest(credentials.username, "ubuntu")
        and secrets.compare_digest(credentials.password, "debian")
    ):
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail=HTTPStatus.UNAUTHORIZED.description,
        )

    return {"ok": True, "message": "Hello from Fly!"}
