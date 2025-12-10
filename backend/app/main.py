from fastapi import FastAPI
from app.routers import shortener
from app.db.crud import del_expired_links

app = FastAPI()

app.include_router(shortener.router)

@app.on_event("startup")
async def clean_expired():
    await del_expired_links()
