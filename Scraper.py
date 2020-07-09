import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

#https://www.amazon.es/Sony-PlayStation-Negro-1000-Wifi/dp/B07HSJW7HK/ref=sr_1_8?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=playstation+pro&qid=1565363715&s=gateway&sr=8-8

headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}

def check_price(URL, wish_price, mail):

    continue_tracking = True

    while continue_tracking:

        page = requests.get(URL, headers=headers)

        soup1 = BeautifulSoup(page.content, 'html.parser')
        soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

        title = soup2.find(id="productTitle").get_text()
        price = soup2.find(id="priceblock_ourprice").get_text()

        price_split = price.split(',')

        converted_price = int(price_split[0])
        converted_wish_price = int(wish_price)

        if(converted_price <= converted_wish_price):
            continue_tracking = False
            print(title.strip())
            print(converted_price)
            send_email(mail, URL)
        else:
            print('Searching...')
            time.sleep(30)

def send_email(mail,url):

    #Configuración del servidor
    my_address = 'my_mail_account'
    my_password = 'my_password'
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(my_address, my_password)

    #Configuración del email
    msg = MIMEMultipart()
    msg['From'] = my_address
    msg['To'] = mail
    msg['Subject'] = '¡Prices have dropped!'
    body = 'Visit this Amazon link ' + url
    msg.attach(MIMEText(body, 'plain'))
    server.send_message(msg)
    del msg

    server.quit()

    print('The mail has been sent succesfully')
