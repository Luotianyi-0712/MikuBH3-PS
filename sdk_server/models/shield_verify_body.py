from pydantic import BaseModel


class ShieldVerifyBody(BaseModel):
    token: str
    uid: str
