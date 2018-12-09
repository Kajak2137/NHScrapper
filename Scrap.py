import pathlib

import requests
import json
import urllib.request as urlib
import ScrapPDFConvert as conv
from os import path

api = "https://nhentai.net/api/gallery/"
nh = "https://i.nhentai.net/galleries/"
number = input("Provide the Sauce: ")
yesChoice = ["y", "yes", "yep"]
noChoice = ["n", "no", "nope"]


def get_the_sauce():
    content = api + number
    headers = {'user-agent': 'Mozilla 5.10'}
    sauce = requests.get(content, headers=headers).json()
    if "error" not in str(sauce):
        prepare_the_sauce(sauce)
    else:
        print("404: Sauce not Found")


def prepare_the_sauce(sauce):
    sauce = json.dumps(sauce)
    prepared_sauce = json.loads(sauce)
    scrap_the_sauce(prepared_sauce)


def scrap_the_sauce(prepared_sauce):
    how_much = prepared_sauce["num_pages"]
    sauce_id = prepared_sauce["media_id"]
    title = prepared_sauce["title"]["pretty"]  # change to english or japanese for different names
    if path.isdir(title):
        print("The sauce is already scrapped.")
        end_handler(title)
    else:
        for i in range(1, how_much + 1):
            page_number = str(i) + ".jpg"
            dirr = title + "/" + page_number
            sauce_link = nh + sauce_id + "/" + page_number
            pathlib.Path(title).mkdir(exist_ok=True)
            urlib.urlretrieve(sauce_link, dirr)
            print("Scrapping the sauce: " + str(i) + " of " + str(how_much))
        print("Scrapped the sauce successfully.")
        end_handler(title)


def end_handler(title):
    choice = input("Would you like to convert to an PDF format?")
    if choice in yesChoice:
        format_choice = "pdf"  # input("Please choose a format: PDF, MOBI, EPUB") - unfinished support for epub and mobi formats
        if format_choice:
            if "pdf" in format_choice:
                pdf = conv.convert_pdf(title)
                if pdf:
                    print("PDF Creation Complete.")
                else:
                    print("PDF Creation Failed.")
                    print("Error: " + pdf)
            elif "mobi" in format_choice:
                mobi = conv.convert_mobi(title)
                if mobi:
                    print("MOBI Creation Complete.")
                else:
                    print("MOBI Creation Failed.")
                    print("Error: " + mobi)
            elif "epub" in format_choice:
                epub = conv.convert_epub(title)
                if epub:
                    print("EPUB Creation Complete.")
                else:
                    print("EPUB Creation Failed.")
                    print("Error: " + epub)
    elif choice in noChoice:
        print("Scrapping Finished.")
    choice = input("Would to like to scrap another sauce?")
    if choice in yesChoice:
        get_the_sauce()
    elif choice in noChoice:
        pass


if __name__ == "__main__":
    get_the_sauce()
