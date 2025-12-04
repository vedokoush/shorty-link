from pydantic import BaseModel, HttpUrl
from typing import Optional

class LinkRequest(BaseModel):
    originalUrl: HttpUrl
    customCode: Optional[str] = None

class LinkResponse(BaseModel):
    shortUrl: str
    qrCode: str