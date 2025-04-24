from fastapi import APIRouter
from app.logger import read_logs, log_metadata
from app.metadata import extract_metadata
from pydantic import BaseModel

router = APIRouter()

class ImageTag(BaseModel):
    image_tag: str  # Expecting image_tag as part of JSON body

@router.get("/history")
def get_history():
    return read_logs()

@router.post("/scan")
def scan_image(data: ImageTag):
    image_name = data.image_tag
    metadata = extract_metadata(image_name)
    log_metadata(metadata)
    return {"message": "Image metadata logged", "data": metadata}


