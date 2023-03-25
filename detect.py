import os
from glob import glob
from os.path import getctime
from PIL import Image
from typing import List
import pytesseract
import cv2

ROOT_DIR: str = os.path.dirname(os.path.abspath(__file__))


def create_images() -> None:
    list_of_files: List[str] = glob(f"{ROOT_DIR}\screenshots\*")
    latest_file: str = max(list_of_files, key=getctime)
    im = Image.open(latest_file)

    # Plyer 1 stats
    name_1 = im.crop((335, 355, 485, 380)).resize((300,50))
    name_1.save(os.path.join(ROOT_DIR, "images\\P1\\name.jpg"), "PNG")
    kills_1 = im.crop((835, 345, 870, 380)).resize((100,100))
    kills_1.save(os.path.join(ROOT_DIR, "images\\P1\\kills.jpg"), "PNG")
    Deaths_1 = im.crop((885, 345, 920, 380)).resize((100,100))
    Deaths_1.save(os.path.join(ROOT_DIR, "images\\P1\\Deaths.jpg"), "PNG")
    Assists_1 = im.crop((935, 345, 970, 380)).resize((100,100))
    Assists_1.save(os.path.join(ROOT_DIR, "images\\P1\\Assists.jpg"), "PNG")

    # Player 2 stats
    name_2 = im.crop((335, 405, 485, 430)).resize((300,50))
    name_2.save(os.path.join(ROOT_DIR, "images\\P2\\name.jpg"), "PNG")
    kills_2 = im.crop((835, 400, 870, 435)).resize((100,100))
    kills_2.save(os.path.join(ROOT_DIR, "images\\P2\\kills.jpg"), "PNG")
    Deaths_2 = im.crop((885, 400, 920, 435)).resize((100,100))
    Deaths_2.save(os.path.join(ROOT_DIR, "images\\P2\\Deaths.jpg"), "PNG")
    Assists_2 = im.crop((935, 400, 970, 435)).resize((100,100))
    Assists_2.save(os.path.join(ROOT_DIR, "images\\P2\\Assists.jpg"), "PNG")

    # Player 3 stats
    name_3 = im.crop((335, 460, 485, 485)).resize((300,50))
    name_3.save(os.path.join(ROOT_DIR, "images\\P3\\name.jpg"), "PNG")
    kills_3 = im.crop((835, 450, 870, 485)).resize((100,100))
    kills_3.save(os.path.join(ROOT_DIR, "images\\P3\\kills.jpg"), "PNG")
    Deaths_3 = im.crop((885, 450, 920, 485)).resize((100,100))
    Deaths_3.save(os.path.join(ROOT_DIR, "images\\P3\\Deaths.jpg"), "PNG")
    Assists_3 = im.crop((935, 450, 970, 485)).resize((100,100))
    Assists_3.save(os.path.join(ROOT_DIR, "images\\P3\\Assists.jpg"), "PNG")

    # Player 4 stats
    name_4 = im.crop((335, 510, 485, 535)).resize((300,50))
    name_4.save(os.path.join(ROOT_DIR, "images\\P4\\name.jpg"), "PNG")
    kills_4 = im.crop((835, 505, 870, 540)).resize((100,100))
    kills_4.save(os.path.join(ROOT_DIR, "images\\P4\\kills.jpg"), "PNG")
    Deaths_4 = im.crop((885, 505, 920, 540)).resize((100,100))
    Deaths_4.save(os.path.join(ROOT_DIR, "images\\P4\\Deaths.jpg"), "PNG")
    Assists_4 = im.crop((935, 505, 970, 540)).resize((100,100))
    Assists_4.save(os.path.join(ROOT_DIR, "images\\P4\\Assists.jpg"), "PNG")

    # Player 5 stats
    name_5 = im.crop((335, 560, 485, 585)).resize((300,50))
    name_5.save(os.path.join(ROOT_DIR, "images\\P5\\name.jpg"), "PNG")
    kills_5 = im.crop((835, 555, 870, 590)).resize((100,100))
    kills_5.save(os.path.join(ROOT_DIR, "images\\P5\\kills.jpg"), "PNG")
    Deaths_5 = im.crop((885, 555, 920, 590)).resize((100,100))
    Deaths_5.save(os.path.join(ROOT_DIR, "images\\P5\\Deaths.jpg"), "PNG")
    Assists_5 = im.crop((935, 555, 970, 590)).resize((100,100))
    Assists_5.save(os.path.join(ROOT_DIR, "images\\P5\\Assists.jpg"), "PNG")

    # Player 6 stats
    name_6 = im.crop((335, 615, 485, 640)).resize((300,50))
    name_6.save(os.path.join(ROOT_DIR, "images\\P6\\name.jpg"), "PNG")
    kills_6 = im.crop((835, 610, 870, 645)).resize((100,100))
    kills_6.save(os.path.join(ROOT_DIR, "images\\P6\\kills.jpg"), "PNG")
    Deaths_6 = im.crop((885, 610, 920, 645)).resize((100,100))
    Deaths_6.save(os.path.join(ROOT_DIR, "images\\P6\\Deaths.jpg"), "PNG")
    Assists_6 = im.crop((935, 610, 970, 645)).resize((100,100))
    Assists_6.save(os.path.join(ROOT_DIR, "images\\P6\\Assists.jpg"), "PNG")

    # Player 7 stats
    name_7 = im.crop((335, 665, 485, 690)).resize((300,50))
    name_7.save(os.path.join(ROOT_DIR, "images\\P7\\name.jpg"), "PNG")
    kills_7 = im.crop((835, 660, 870, 695)).resize((100,100))
    kills_7.save(os.path.join(ROOT_DIR, "images\\P7\\kills.jpg"), "PNG")
    Deaths_7 = im.crop((885, 660, 920, 695)).resize((100,100))
    Deaths_7.save(os.path.join(ROOT_DIR, "images\\P7\\Deaths.jpg"), "PNG")
    Assists_7 = im.crop((935, 660, 970, 695)).resize((100,100))
    Assists_7.save(os.path.join(ROOT_DIR, "images\\P7\\Assists.jpg"), "PNG")

    # Player 8 stats
    name_8 = im.crop((335, 715, 485, 740)).resize((300,50))
    name_8.save(os.path.join(ROOT_DIR, "images\\P8\\name.jpg"), "PNG")
    kills_8 = im.crop((835, 710, 870, 745)).resize((100,100))
    kills_8.save(os.path.join(ROOT_DIR, "images\\P8\\kills.jpg"), "PNG")
    Deaths_8 = im.crop((885, 710, 920, 745)).resize((100,100))
    Deaths_8.save(os.path.join(ROOT_DIR, "images\\P8\\Deaths.jpg"), "PNG")
    Assists_8 = im.crop((935, 710, 970, 745)).resize((100,100))
    Assists_8.save(os.path.join(ROOT_DIR, "images\\P8\\Assists.jpg"), "PNG")

    # Player 9 stats
    name_9 = im.crop((335, 770, 485, 795)).resize((300,50))
    name_9.save(os.path.join(ROOT_DIR, "images\\P9\\name.jpg"), "PNG")
    kills_9 = im.crop((835, 765, 870, 800)).resize((100,100))
    kills_9.save(os.path.join(ROOT_DIR, "images\\P9\\kills.jpg"), "PNG")
    Deaths_9 = im.crop((885, 765, 920, 800)).resize((100,100))
    Deaths_9.save(os.path.join(ROOT_DIR, "images\\P9\\Deaths.jpg"), "PNG")
    Assists_9 = im.crop((935, 765, 970, 800)).resize((100,100))
    Assists_9.save(os.path.join(ROOT_DIR, "images\\P9\\Assists.jpg"), "PNG")

    # Player 10 stats
    name_10 = im.crop((335, 820, 485, 845)).resize((300,50))
    name_10.save(os.path.join(ROOT_DIR, "images\\P9+1\\name.jpg"), "PNG")
    kills_10 = im.crop((835, 815, 870, 850)).resize((100,100))
    kills_10.save(os.path.join(ROOT_DIR, "images\\P9+1\\kills.jpg"), "PNG")
    Deaths_10 = im.crop((885, 815, 920, 850)).resize((100,100))
    Deaths_10.save(os.path.join(ROOT_DIR, "images\\P9+1\\Deaths.jpg"), "PNG")
    Assists_10 = im.crop((935, 815, 970, 850)).resize((100,100))
    Assists_10.save(os.path.join(ROOT_DIR, "images\\P9+1\\Assists.jpg"), "PNG")


def read_images() -> List[List[str]]:
    player_arr: List[List[str]] = [["Name", "Kills", "Deaths", "Assists", "Character"],[], [], [], [], [], [], [], [], [], []]
    # Create screenshots from initial screenshot
    create_images()

    # Defining paths to tesseract.exe
    path_to_tesseract: str = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

    folders: List[str] = glob(f"{ROOT_DIR}\images\*")

    for i in range(1, len(folders) + 1):
        # Name
        image_path = f"{folders[i -1 ]}\\name.jpg"
        image = cv2.imread(image_path, 0)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[
            1
        ]
        data = pytesseract.image_to_string(thresh, lang="eng", config="--psm 6")
        player_arr[i].append(data.strip())

        # Kills
        image_path = f"{folders[i - 1]}\\Kills.jpg"
        image = cv2.imread(image_path, 0)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[
            1
        ]
        data = pytesseract.image_to_string(thresh, lang="eng", config="--psm 6 -c tessedit_char_whitelist=0123456789" )
        player_arr[i].append(data.strip())

        # Assists
        image_path = f"{folders[i - 1]}\\Deaths.jpg"
        image = cv2.imread(image_path, 0)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[
            1
        ]
        data = pytesseract.image_to_string(thresh, lang="eng", config="--psm 6 -c tessedit_char_whitelist=0123456789")
        player_arr[i].append(data.strip())

        # Deaths
        image_path = f"{folders[i - 1]}\\Assists.jpg"
        image = cv2.imread(image_path, 0)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[
            1
        ]
        data = pytesseract.image_to_string(thresh, lang="eng", config="--psm 6 -c tessedit_char_whitelist=0123456789")
        player_arr[i].append(data.strip())

    print(player_arr)
    return player_arr

#create_images()