from .sheets import data_collection_DATA
from Schemas import LocationCount

async def append_row(count: LocationCount):
    data = [count.Date, count.Location, None, count.Number_of_People, count.Comments]
    
    response = data_collection_DATA.append_row(data, table_range = 'A1:E1', value_input_option = 'USER_ENTERED', include_values_in_response=True)
    return count