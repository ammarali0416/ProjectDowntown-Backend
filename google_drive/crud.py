import datetime
from google_drive.drive import service
from googleapiclient.http import MediaIoBaseUpload
from Schemas import ValidLocation, ImageUploadSuccess

async def image_upload(location: ValidLocation, image) -> ImageUploadSuccess:
    # Map locations to their respective folder IDs
    location_folders = {
        ValidLocation.Graveyard: '15M5z6HjMto0D_ES7IXSc7lYw42xYYBqR',
        ValidLocation.BusStop: '1t9aGbPyjAFAiHcg7gPV5OWLLKN05GP8V',
        ValidLocation.Gaslight: '16G5hM95xFSIcm5eeLeEzRiMZOKTabRRH',
        ValidLocation.Bridge: '1NPZIV0tfiGntSGFEXEQMyEri58t356vU',
        ValidLocation.GoodSam: '1rRNIWoV_QiKxD1pwAH2esA7WAN057E7W',
        ValidLocation.Borrell: '1FRawazir7bVlMS0tuUIu2Cc_C-P5Nffb',
    }

    # Get the folder ID for the specified location
    location_folder_id = location_folders.get(location)

    if not location_folder_id:
        raise ValueError(f"Invalid location: {location}")

    # Add timestamp to the filename
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    original_filename = image.filename
    new_filename = f"{timestamp}_{original_filename}"

    # Metadata for the uploaded file
    file_metadata = {
        'name': new_filename,  # Use the new filename with the timestamp prefix
        'parents': [location_folder_id]
    }

    # Media file upload using MediaIoBaseUpload
    media = MediaIoBaseUpload(image.file, mimetype=image.content_type, resumable=True)

    # Upload the file
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    file_id = file.get("id")
    google_drive_path = f"PD App Data/Image Data/{location.value}/{new_filename}"

    # Create the response model instance
    success_response = ImageUploadSuccess(
        GoogleDrivePath=google_drive_path,
        file_id=file_id,
        filename=new_filename,
        location=location.value
    )

    return success_response