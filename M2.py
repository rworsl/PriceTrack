import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from datetime import datetime, date
import time

ended = True
page = requests.get('https://store.google.com/gb/product/pixel_5?gclid=CjwKCAiA25v_BRBNEiwAZb4-Zbh8AlGvcw4sotAWHukmCT_pmrFpJqv54L3Q_BLAAVC0KbDVVTbBCxoCy3IQAvD_BwE&gclsrc=aw.ds')
soup = BeautifulSoup(page.text, 'html.parser')
while ended == True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    nicedate = today.strftime("%d/%m/%Y")
    if str(current_time) == "09:00:00":
        price = soup.find(class_='is-price')
        textprice = str(price)
        clean = str(textprice).replace('<span class="is-price">£',"")
        clean = clean.replace('</span>',"")
        latestPrice = "" + str(clean)
        f = open("M2_price.txt", "a")
        f.write(latestPrice + " " + str(nicedate) + "\n")
        f.close()
        time.sleep(5)
