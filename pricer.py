import matplotlib.pyplot as plt
from datetime import datetime, date
import time

ended = True
alsoended = True
pricetrack = []
datetrack = []
pricetrack2 = []
datetrack2 = []
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

with open('M2_price.txt', 'r') as costs:
    for line in costs.readlines():
        tuples = line.split(' ')
        pricetrack.append(tuples[0])
        datetrack.append(tuples[1])

while ended == True:
    pricetrack = []
    datetrack = []
    with open('M2_price.txt', 'r') as costs:
        for line in costs.readlines():
            tuples = line.split(' ')
            pricetrack.append(tuples[0])
            datetrack.append(tuples[1])
    if str(current_time) != "01:00:00" or str(current_time) != "02:00:00" or str(current_time) != "03:00:00" or str(
            current_time) != "04:00:00" or str(current_time) != "05:00:00" or str(current_time) != "06:00:00" or str(
            current_time) != "07:00:00" or str(current_time) != "08:00:00" or str(current_time) != "09:00:00" or str(
            current_time) != "10:00:00" or str(current_time) != "11:00:00" or str(current_time) != "12:00:00" or str(
            current_time) != "13:00:00" or str(current_time) != "14:00:00" or str(current_time) != "15:00:00" or str(
            current_time) != "16:00:00" or str(current_time) != "17:00:00" or str(current_time) != "18:00:00" or str(
            current_time) != "19:00:00" or str(current_time) != "20:00:00" or str(current_time) != "21:00:00" or str(
            current_time) != "22:00:00" or str(current_time) != "23:00:00" or str(current_time) != "00:00:00":
        fig, ax = plt.subplots()
        ax.plot(datetrack, pricetrack, 'ro')
        ax.invert_yaxis()
        ax.set_xlabel('Date')
        ax.set_ylabel('Price (£)')
        ax.set_title('Phone Price')
        plt.plot(datetrack, pricetrack, label="Pixel")
        plt.legend()
        plt.show()
