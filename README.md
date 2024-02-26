## Depriciated, replaced by: https://github.com/DavidPav123/Valorant-to-Goggle-Sheets-and-CSV.git
# Valorant-to-GS

Usage instructions:

1. Download project

2. Download tesseract OCR from the following link and install it on your computer, taking note of the location its installed to. https://github.com/UB-Mannheim/tesseract/wiki

3. Install the pytesseract package using the following pip command: *pip install pytesseract*

4. Install the opencv package using the following pip command: *pip package cv2*

5. Change the **path_to_tesseract** variable on line 180 in *detect.py* 

6. Change the **SPREADSHEET_ID** variable on line 16 in *google_sheets_push.py*

7. To run the program put a screenshot of the Valorant end game screen in the **Screenshots** folder and then run *Stats_to_GS.py*.
