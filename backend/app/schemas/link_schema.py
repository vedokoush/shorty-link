from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class LinkRequest(BaseModel):
    originalUrl: HttpUrl
    customCode: Optional[str] = None
    createdAt: datetime
    expireAt: Optional[datetime] = None

class LinkResponse(BaseModel):
    shortUrl: str
    qrCode: str
    createdAt: datetime
    expireAt: datetime
