from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from review_extractor import extract_reviews

app = FastAPI()


class URLRequest(BaseModel):
    url: str


@app.get('/')
async def read_root():
    return {"message": "Welcome to the Review API!"}


@app.get("/api/reviews")
async def get_reviews(url: str):
    try:
        if not url:
            raise HTTPException(status_code=400, detail="URL is required")

        reviews = extract_reviews(url)
        return reviews
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
