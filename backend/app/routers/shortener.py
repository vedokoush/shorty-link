from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from app.schemas.link_schema import LinkRequest, LinkResponse
from app.services.generator import generate_code, generate_numeric_code
from app.services.qr_service import generate_qr_base64
from app.db.crud import save_link, get_link, get_all_links, code_exists
from datetime import datetime

router = APIRouter()

BASE_DOMAIN = "http://localhost:8000/"

@router.post("/api/shorten", response_model=LinkResponse)
async def shorten_link(body: LinkRequest):

    if body.lifetime == True:
        code = generate_numeric_code()
        expireAt = None
    else:
        code = body.customCode or generate_code()
        expireAt = body.expireAt

    if await code_exists(code):
        raise HTTPException(status_code=400, detail="Custom code already exists!")

    await save_link(code, body.originalUrl, body.createdAt, expireAt)

    short_url = BASE_DOMAIN + code
    qr = generate_qr_base64(short_url)

    return LinkResponse(shortUrl=short_url, qrCode=qr,
                        createdAt=body.createdAt, expireAt=expireAt)