from pydantic import BaseModel, Field
from typing import List, Optional, Annotated
from enum import Enum

class ValidLocation(str, Enum):
    Graveyard = "Graveyard"
    BusStop = "Bus Stop"
    Gaslight = "Gaslight"
    Bridge = "Bridge"
    GoodSam = "Good Sam"
    Borrell = "Borrell"

class LocationCount(BaseModel):
    Date: Annotated[str, "The date of the count as a string in format 'DD/MM/YYYY'"]
    Location: Annotated[ValidLocation, "The location of the count."]
    Number_of_People: Annotated[int, "The number of people at the location."]
    Comments: Annotated[str | None, "Any comments about the count."]

class ItemRequestWrite(BaseModel):
    Date: Annotated[str, "The date of the request as a string in format 'DD/MM/YYYY'"]
    Requested_To: Annotated[str, "The person or group the request is made to."]
    Requester: Annotated[str, "The person making the request."]
    Location: Annotated[str, "The location of the request."]
    Item_Request: Annotated[str, "The item requested."]
    Notes: Annotated[str | None, "Any notes about the request."]
    Approximate_Price: Annotated[float | None, "The approximate price of the item requested."]

class ImageUploadSuccess(BaseModel):
    GoogleDrivePath: Annotated[str, Field(description="The path to the uploaded image in Google Drive.")]
    file_id: Annotated[str, Field(description="The ID of the uploaded file in Google Drive.")]
    filename: Annotated[str, Field(description="The original filename of the uploaded image.")]
    location: Annotated[str, Field(description="The location where the image was uploaded.")]