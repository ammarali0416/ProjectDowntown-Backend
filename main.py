from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv, find_dotenv

from Schemas import LocationCount
from Schemas import ItemRequestWrite

from google_sheets.crud import add_count_data
from google_sheets.crud import add_item_request

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
          summary="Add a count to the Data Collection Google Sheet", 
          response_model=LocationCount, 
          response_description="Numerical data added",
          description="Adds a count and location to the following Google Sheet:https://docs.google.com/spreadsheets/d/1glCIk5k6bJWhS984VecLBYfK4wwd_1-_YW9TRE1bEM4/edit#gid=1891335984",
          tags=["Data Collection"])
async def add_count(count: LocationCount) -> LocationCount:
    response = await add_count_data(count)
    return response

@app.post("/AddRequest",
          status_code=status.HTTP_202_ACCEPTED,
          summary="Add a request to the Item Request Google Sheet",
          response_model=ItemRequestWrite,
          response_description="Item request added",
          description=
            """Adds an item request to the following Google Sheet: https://docs.google.com/spreadsheets/d/1opidAtrdOkiZIi-6hiQppn1SGuZtOw0nDKuwo6RlDBw/edit#gid=0.
            Data includes the request date, the requester, the volunteer recieving the request, the item and location. Optionally allows notes and price.""",
          tags=["Item Requests"])
async def add_request(request: ItemRequestWrite) -> ItemRequestWrite:
    response = await add_item_request(request)
    return response