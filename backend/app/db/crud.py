from .database import db
from pydantic import HttpUrl

link_collection = db.get_collection("links")

async def get_all_links():
    links = []
    async for link in link_collection.find():
        links.append({"code": link["code"], "original_url": link["original_url"]})
    return links

async def save_link(code: str, original_url: HttpUrl):
    await link_collection.insert_one({"code": code, "original_url": str(original_url)})

async def get_link(code: str):
    document = await link_collection.find_one({"code": code})
    if document:
        return document.get("original_url")
    return None
