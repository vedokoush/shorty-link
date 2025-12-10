from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from app.schemas.link_schema import LinkRequest, LinkResponse
from app.services.generator import generate_code
from app.services.qr_service import generate_qr_base64
from app.db.crud import save_link, get_link, get_all_links
from datetime import datetime, timezone

router = APIRouter()

BASE_DOMAIN = "http://localhost:8000/"

@router.post("/api/shorten", response_model=LinkResponse)
async def shorten_link(body: LinkRequest):
    code = body.customCode or generate_code()
    await save_link(code, body.originalUrl,body.createdAt,body.expireAt)

    short_url = BASE_DOMAIN + code
    qr = generate_qr_base64(short_url)

    return LinkResponse(shortUrl=short_url, qrCode=qr,createdAt=body.createdAt,expireAt=body.expireAt)


@router.get("/api/links")
async def get_links():
    links = await get_all_links()
    return JSONResponse(content=links)


@router.get("/{code}")
async def redirect(code: str):
    url = await get_link(code)
    if not url:
        raise HTTPException(status_code=404, detail="Short link not found or expired!")
    return RedirectResponse(url)
