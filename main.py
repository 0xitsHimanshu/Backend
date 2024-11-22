from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from typing import List

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Update with the origin of your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock data model
class OverlayData(BaseModel):
    mediaType: str
    image_url: str
    opacity: float
    dimensions: dict

app.mount("/media", StaticFiles(directory="static"), name="static")


# Mock endpoint to return overlay data
@app.get("/api/overlay", response_model=List[OverlayData])
async def get_overlay_data():
    return [
        {   
            "mediaType": "gif",
            "image_url": "http://localhost:8000/media/halloween.gif",
            "opacity": 1,
            "dimensions": {"width": "300px", "height": "150px", "top": "200px", "left": "200px"}
        }
    ]
