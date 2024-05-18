from .sheets import data_collection_DATA
from .sheets import requests_from_friends_REQUESTS
from Schemas import LocationCount, ItemRequestWrite

async def add_count_data(count: LocationCount) -> LocationCount:
    data = [count.Date, count.Location, None, count.Number_of_People, count.Comments]
    
    response = data_collection_DATA.append_row(data, table_range = 'A1:E1', value_input_option = 'USER_ENTERED', include_values_in_response=True)
    return count

async def add_item_request(request: ItemRequestWrite) -> ItemRequestWrite:
    data = [request.Date, request.Requested_To, request.Requester, request.Location, request.Item_Request, request.Notes, request.Approximate_Price]
    
    response = requests_from_friends_REQUESTS.append_row(data, table_range = 'B2:H2', value_input_option = 'USER_ENTERED', include_values_in_response=True)
    return request