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
    name_1 = im.crop((338, 357, 480, 374))
    name_1.save(os.path.join(ROOT_DIR, "images\\P1\\name.jpg"), "PNG")
    kills_1 = im.crop((835, 355, 866, 375))
    kills_1.save(os.path.join(ROOT_DIR, "images\\P1\\kills.jpg"), "PNG")
    Assists_1 = im.crop((891, 355, 916, 375))
    Assists_1.save(os.path.join(ROOT_DIR, "images\\P1\\Deaths.jpg"), "PNG")
    Deaths_1 = im.crop((940, 355, 970, 375))
    Deaths_1.save(os.path.join(ROOT_DIR, "images\\P1\\Assists.jpg"), "PNG")

    # Player 2 stats
    name_2 = im.crop((338, 410, 480, 425))
    name_2.save(os.path.join(ROOT_DIR, "images\\P2\\name.jpg"), "PNG")
    kills_2 = im.crop((835, 407, 866, 430))
    kills_2.save(os.path.join(ROOT_DIR, "images\\P2\\kills.jpg"), "PNG")
    Assists_2 = im.crop((891, 407, 916, 430))
    Assists_2.save(os.path.join(ROOT_DIR, "images\\P2\\Deaths.jpg"), "PNG")
    Deaths_2 = im.crop((940, 405, 970, 430))
    Deaths_2.save(os.path.join(ROOT_DIR, "images\\P2\\Assists.jpg"), "PNG")

    # Player 3 stats
    name_3 = im.crop((338, 465, 480, 480))
    name_3.save(os.path.join(ROOT_DIR, "images\\P3\\name.jpg"), "PNG")
    kills_3 = im.crop((835, 457, 866, 480))
    kills_3.save(os.path.join(ROOT_DIR, "images\\P3\\kills.jpg"), "PNG")
    Assists_3 = im.crop((891, 457, 916, 480))
    Assists_3.save(os.path.join(ROOT_DIR, "images\\P3\\Deaths.jpg"), "PNG")
    Deaths_3 = im.crop((940, 455, 970, 480))
    Deaths_3.save(os.path.join(ROOT_DIR, "images\\P3\\Assists.jpg"), "PNG")

    # Player 4 stats
    name_4 = im.crop((338, 513, 480, 532))
    name_4.save(os.path.join(ROOT_DIR, "images\\P4\\name.jpg"), "PNG")
    kills_4 = im.crop((835, 510, 870, 535))
    kills_4.save(os.path.join(ROOT_DIR, "images\\P4\\kills.jpg"), "PNG")
    Assists_4 = im.crop((891, 510, 916, 533))
    Assists_4.save(os.path.join(ROOT_DIR, "images\\P4\\Deaths.jpg"), "PNG")
    Deaths_4 = im.crop((940, 510, 970, 535))
    Deaths_4.save(os.path.join(ROOT_DIR, "images\\P4\\Assists.jpg"), "PNG")

    # Player 5 stats
    name_5 = im.crop((338, 565, 480, 582))
    name_5.save(os.path.join(ROOT_DIR, "images\\P5\\name.jpg"), "PNG")
    kills_5 = im.crop((835, 560, 870, 585))
    kills_5.save(os.path.join(ROOT_DIR, "images\\P5\\kills.jpg"), "PNG")
    Assists_5 = im.crop((891, 562, 916, 585))
    Assists_5.save(os.path.join(ROOT_DIR, "images\\P5\\Deaths.jpg"), "PNG")
    Deaths_5 = im.crop((940, 560, 970, 585))
    Deaths_5.save(os.path.join(ROOT_DIR, "images\\P5\\Assists.jpg"), "PNG")

    # Player 6 stats
    name_6 = im.crop((338, 615, 480, 635))
    name_6.save(os.path.join(ROOT_DIR, "images\\P6\\name.jpg"), "PNG")
    kills_6 = im.crop((835, 610, 870, 640))
    kills_6.save(os.path.join(ROOT_DIR, "images\\P6\\kills.jpg"), "PNG")
    Assists_6 = im.crop((890, 610, 920, 635))
    Assists_6.save(os.path.join(ROOT_DIR, "images\\P6\\Deaths.jpg"), "PNG")
    Deaths_6 = im.crop((940, 610, 970, 635))
    Deaths_6.save(os.path.join(ROOT_DIR, "images\\P6\\Assists.jpg"), "PNG")

    # Player 7 stats
    name_7 = im.crop((338, 670, 480, 689))
    name_7.save(os.path.join(ROOT_DIR, "images\\P7\\name.jpg"), "PNG")
    kills_7 = im.crop((835, 665, 866, 690))
    kills_7.save(os.path.join(ROOT_DIR, "images\\P7\\kills.jpg"), "PNG")
    Assists_7 = im.crop((891, 665, 916, 690))
    Assists_7.save(os.path.join(ROOT_DIR, "images\\P7\\Deaths.jpg"), "PNG")
    Deaths_7 = im.crop((940, 665, 970, 690))
    Deaths_7.save(os.path.join(ROOT_DIR, "images\\P7\\Assists.jpg"), "PNG")

    # Player 8 stats
    name_8 = im.crop((335, 720, 480, 740))
    name_8.save(os.path.join(ROOT_DIR, "images\\P8\\name.jpg"), "PNG")
    kills_8 = im.crop((835, 716, 866, 741))
    kills_8.save(os.path.join(ROOT_DIR, "images\\P8\\kills.jpg"), "PNG")
    Assists_8 = im.crop((890, 715, 920, 745))
    Assists_8.save(os.path.join(ROOT_DIR, "images\\P8\\Deaths.jpg"), "PNG")
    Deaths_8 = im.crop((940, 715, 970, 745))
    Deaths_8.save(os.path.join(ROOT_DIR, "images\\P8\\Assists.jpg"), "PNG")

    # Player 9 stats
    name_9 = im.crop((338, 773, 480, 790))
    name_9.save(os.path.join(ROOT_DIR, "images\\P9\\name.jpg"), "PNG")
    kills_9 = im.crop((835, 767, 866, 793))
    kills_9.save(os.path.join(ROOT_DIR, "images\\P9\\kills.jpg"), "PNG")
    Assists_9 = im.crop((890, 765, 920, 795))
    Assists_9.save(os.path.join(ROOT_DIR, "images\\P9\\Deaths.jpg"), "PNG")
    Deaths_9 = im.crop((940, 765, 970, 795))
    Deaths_9.save(os.path.join(ROOT_DIR, "images\\P9\\Assists.jpg"), "PNG")

    # Player 10 stats
    name_10 = im.crop((338, 825, 480, 843))
    name_10.save(os.path.join(ROOT_DIR, "images\\P9+1\\name.jpg"), "PNG")
    kills_10 = im.crop((835, 821, 866, 846))
    kills_10.save(os.path.join(ROOT_DIR, "images\\P9+1\\kills.jpg"), "PNG")
    Assists_10 = im.crop((891, 821, 916, 846))
    Assists_10.save(os.path.join(ROOT_DIR, "images\\P9+1\\Deaths.jpg"), "PNG")
    Deaths_10 = im.crop((940, 820, 970, 850))
    Deaths_10.save(os.path.join(ROOT_DIR, "images\\P9+1\\Assists.jpg"), "PNG")


def read_images() -> List[List[str]]:
    player_arr: List[List[str]] = [[], [], [], [], [], [], [], [], [], []]
    # Create screenshots from initial screenshot
    create_images()

    # Defining paths to tesseract.exe
    path_to_tesseract: str = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

    folders: List[str] = glob(f"{ROOT_DIR}\images\*")

    for i in range(len(folders)):
        # Name
        image_path = f"{folders[i]}\\name.jpg"
        image = cv2.imread(image_path, 0)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[
            1
        ]
        data = pytesseract.image_to_string(thresh, lang="eng", config="--psm 6")
        player_arr[i].append(data.strip())

        # Kills
        image_path = f"{folders[i]}\\Kills.jpg"
        image = cv2.imread(image_path, 0)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[
            1
        ]
        data = pytesseract.image_to_string(thresh, lang="eng", config="--psm 6")
        player_arr[i].append(data.strip())

        # Assists
        image_path = f"{folders[i]}\\Deaths.jpg"
        image = cv2.imread(image_path, 0)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[
            1
        ]
        data = pytesseract.image_to_string(thresh, lang="eng", config="--psm 6")
        player_arr[i].append(data.strip())

        # Deaths
        image_path = f"{folders[i]}\\Assists.jpg"
        image = cv2.imread(image_path, 0)
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[
            1
        ]
        data = pytesseract.image_to_string(thresh, lang="eng", config="--psm 6")
        player_arr[i].append(data.strip())

    print(player_arr)
    return player_arr
