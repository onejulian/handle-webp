import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from webp import convert_to_webp

class Params(BaseModel):
    idArticle: str
    ext: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "server is running"}

@app.post("/image")
async def handle_images(params: Params):
    convert_to_webp(params.idArticle, params.ext)
    return {"message": "get_article", "params": params}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8084)