import uvicorn
from fastapi import FastAPI, File, UploadFile, status, Header, Request, Depends
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/")
async def getAll():
    return "all cheers"