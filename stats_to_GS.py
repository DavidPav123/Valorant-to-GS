from detect import read_images
from google_sheets_push import update_sheet

if __name__ == "__main__":
    update_sheet(read_images("screenshots\game1.png"), "Sheet1!A1:Z26")
    update_sheet(read_images("screenshots\game2.png"), "Sheet2!A1:Z26")
    update_sheet(read_images("screenshots\game3.png"), "Sheet3!A1:Z26")

    
