import requests
import selectorlib
import smtplib, ssl
import os
import time
import mysql.connector

SQL_USER = os.getenv("sql_user")
SQL_PASSWORD = os.getenv("sql_password")
URL = "https://programmer100.pythonanywhere.com/tours/"


cnx = mysql.connector.connect(user=SQL_USER, password=SQL_PASSWORD,
                                    host='localhost', 
                                    database='my_db',
                                    charset='utf8')



def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url=url)
    source = response.text
    return source 


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("app10/extract.yaml")
    value = extractor.extract(source)["tours"]
    return value
    
    
def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "app8flask@gmail.com"
    password = "ooruzcufgubxifsa"

    receiver = "app8flask@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    
    
def store(extracted_info):
    row = extracted_info.split(",")
    row = [item.strip() for item in row]
    cursor = cnx.cursor(buffered = True)
    cursor.execute('''INSERT INTO events VALUES(%s,%s,%s)''', row)
    cnx.commit()
        
def read(extracted_info):
    row = extracted_info.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = cnx.cursor(buffered = True)
    cursor.execute('''SELECT * FROM events WHERE band=%s AND city=%s AND date=%s''', (band, city, date))
    rows = cursor.fetchall()
    return rows
    

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        if extracted != "No upcoming tours":
            content = read(extracted)
            if not content:
                store(extracted)
                print("Email sent")
                #send_email(message="Hey, new event was found!")
                
        time.sleep(2)
        # This makes the app check for the events every 2 sec