from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv, find_dotenv

from Schemas import LocationCount
from google_sheets.crud import append_row

from metadata import title, description, summary, version, contact

load_dotenv(find_dotenv())

app = FastAPI(
    title=title,
    description=description,
    summary=summary,
    version=version,
    contact=contact
)

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

@app.post("/AddCount", 
          status_code=status.HTTP_202_ACCEPTED, 
          summary="Add a count to the Google Sheet", 
          response_model=LocationCount, 
          response_description="The record added to the Google Sheet",
          tags=["Data Collection"])
async def add_count(count: LocationCount) -> LocationCount:
    response = await append_row(count)
    return response