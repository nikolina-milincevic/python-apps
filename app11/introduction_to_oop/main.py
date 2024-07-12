import requests
import selectorlib
import smtplib, ssl
import os
import time
import os
import mysql.connector


URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

SQL_USER = os.getenv("sql_user")
SQL_PASSWORD = os.getenv("sql_password")



class Event:
    def scrape(self, url):
        """Scrape the page source from the URL"""
        response = requests.get(url, headers=HEADERS)
        source = response.text
        return source


    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("app11/introduction_to_oop/extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class Email:
    def send(self, message):
        host = "smtp.gmail.com"
        port = 465

        username = "app8flask@gmail.com"
        password = "qyciukmocfaiarse"

        receiver = "app8flask@gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
        print("Email was sent!")


class Database:
    def __init__(self, database_name):
        self.cnx = mysql.connector.connect(user=SQL_USER, password=SQL_PASSWORD,
                                host="localhost", database=database_name)
    
    def store(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(%s,%s,%s)", row)
        self.connection.commit()

    def read(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band=%s AND city=? AND date=%s", (band, city, date))
        rows = cursor.fetchall()
        print(rows)
        return rows


if __name__ == "__main__":
    while True:
        event = Event()
        scraped = event.scrape(URL)
        extracted = event.extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            database = Database(database_name="my_db")
            row = database.read(extracted)
            if not row:
                database.store(extracted)
                #Email.send(message="Hey, new event was found!")
        time.sleep(2)