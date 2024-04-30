from pydantic import BaseModel
from typing import List, Optional, Annotated

class LocationCount(BaseModel):
    Date: Annotated[str, "The date of the count as a string in format 'DD/MM/YYYY'"]
    Location: Annotated[str, "The location of the count."]
    Number_of_People: Annotated[int, "The number of people at the location."]
    Comments: Annotated[str | None, "Any comments about the count."]