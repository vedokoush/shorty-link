from .database import db
from pydantic import HttpUrl
from datetime import datetime
from typing import Optional

link_collection = db.get_collection("links")

async def get_all_links():
    links = []
    async for link in link_collection.find():
        links.append({"code": link["code"], "original_url": link["original_url"],"createdAt": link.get("createdAt"),"expireAt": link.get("expireAt")})
    return links

async def save_link(code: str, original_url: HttpUrl, createdAt: datetime, expireAt: datetime):
    await link_collection.insert_one({"code": code, "original_url": str(original_url),"createdAt": createdAt,"expireAt": expireAt})

async def get_link(code: str):
    document = await link_collection.find_one({"code": code})
    if document:
        return document.get("original_url")
    return None
