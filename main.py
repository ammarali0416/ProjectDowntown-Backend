from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv, find_dotenv

from Schemas import LocationCount
from google_sheets import append_row

load_dotenv(find_dotenv())

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specified origins (use ["*"] to allow all)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/AddCount", status_code=status.HTTP_202_ACCEPTED, summary="Add a count to the Google Sheet", response_model=LocationCount, response_description="The record added to the Google Sheet")
async def add_count(count: LocationCount) -> LocationCount:
    response = await append_row(count)
    return response