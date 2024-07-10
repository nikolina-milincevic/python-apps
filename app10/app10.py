import requests
import selectorlib
import smtplib, ssl
import os
import time


URL = "https://programmer100.pythonanywhere.com/tours/"


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
    with open("app10/data.txt", "a") as file:
        file.write(extracted_info + "\n")
        
        
def read():
    with open("app10/data.txt", "r") as file:
        return file.read()
    

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        content = read()
        print(extracted)
        if extracted != "No upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email(message="Hey, new event was found!")
                
        time.sleep(2)
        # This makes the app check for the events every 2 sec