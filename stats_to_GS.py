from detect import read_images
from google_sheets_push import update_sheet

if __name__ == "__main__":
    update_sheet(read_images(), "Sheet1!A1:Z26")