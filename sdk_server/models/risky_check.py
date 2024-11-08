from pydantic import BaseModel
from typing import Optional


class DataScheme(BaseModel):
    id: str
    action: str
    geetest: Optional[object]


class RiskyCheck(BaseModel):
    retcode: int
    message: str
    data: DataScheme
