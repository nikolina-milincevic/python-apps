# This is the app to scrape average temperature
# from the we page
# https://programmer100.pythonanywhere.com

import requests
import selectorlib
from datetime import datetime

URL = "https://programmer100.pythonanywhere.com"


def scrape(my_url):
    response = requests.get(url=my_url)
    source = response.text
    return source

def extract(my_source):
    extractor = selectorlib.Extractor.from_yaml_file("app10/extract.yaml")
    value = extractor.extract(my_source)["temperature"]
    return value

def save_value(my_value):
    with open("app10/temperature.txt", "a") as file:
        file.write(my_value + "\n")
        
def get_content():
    with open("app10/temperature.txt", "r") as file:
        content = file.read()
    return content


if __name__ == "__main__":
    content = get_content()
    if content.startswith("date") == False:
        save_value("date, temperature")
        
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    date = datetime.now()
    date = date.strftime("%Y-%M-%D %H:%M:%S")
    save_value(f"{date}, {extracted}")