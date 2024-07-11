# This is the app to scrape average temperature
# from the we page
# https://programmer100.pythonanywhere.com

import requests
import selectorlib
from datetime import datetime
import os
import mysql.connector

SQL_USER = os.getenv("sql_user")
SQL_PASSWORD = os.getenv("sql_password")
URL = "https://programmer100.pythonanywhere.com"

cnx = mysql.connector.connect(user=SQL_USER, password=SQL_PASSWORD,
                              host="localhost", database="my_db")


def scrape(my_url):
    response = requests.get(url=my_url)
    source = response.text
    return source

def extract(my_source):
    extractor = selectorlib.Extractor.from_yaml_file("app10/extract.yaml")
    value = extractor.extract(my_source)["temperature"]
    return value

def save_value(my_date, my_temperature):
    cursor = cnx.cursor(buffered=True)
    my_query = '''INSERT INTO temperatures VALUES(%s, %s)'''
    cursor.execute(my_query, (my_date, my_temperature))
    cnx.commit()
        
# def get_content():
#     with open("app10/temperature.txt", "r") as file:
#         content = file.read()
#     return content


if __name__ == "__main__":  
    scraped = scrape(URL)
    temperature = int(extract(scraped))
    print(temperature)
    date = datetime.now()
    date = date.strftime("%Y-%M-%D %H:%M:%S")
    save_value(date, temperature)