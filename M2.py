import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from datetime import datetime, date
import time

ended = True
page = requests.get('https://www.ebuyer.com/801061-wd-blue-1tb-3d-nand-ssd-m-2-2280-at-ebuyer-com-wds100t2b0b?_sgm_campaign=scn_8714e1eb7e000&_sgm_source=801061&_sgm_action=click')
soup = BeautifulSoup(page.text, 'html.parser')


while ended == True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    nicedate = today.strftime("%d/%m/%Y")
    if str(current_time) == "09:00:00":
        price = soup.find(class_='price')
        textprice = str(price)
        clean = textprice.replace('<p class="price">',"")
        clean = clean.replace('<span class="smaller currency-symbol">£</span>',"")
        clean = clean.replace('<span class="vat-text"> inc. vat</span> </p>',"")
        clean = clean.replace(' ',"")
        clean = clean.replace("\r","")
        clean = clean.replace("\n","")
        latestPrice = "" + str(clean)
        f = open("M2_price.txt", "a")
        f.write(latestPrice + " " + str(nicedate) + "\n")
        f.close()
        time.sleep(5)
