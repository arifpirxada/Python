from notifypy import Notify
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random

def check_price(product):

    try:
        ua = UserAgent()
        r = requests.get(product["url"], headers={'User-Agent': ua.random})
    except requests.exceptions.RequestException as e:
        if isinstance(e, requests.exceptions.ProxyError):
            print("\033[31mCould not connect to proxy!\033[0m")
        else:
            print("\033[31mAn error occured while fetching data\033[0m")
            
        return product

    soup = BeautifulSoup(r.content, "html.parser")
    print(soup.prettify())
    # Find the price =>
    price = soup.find("span", attrs={"class": "a-price-whole"})

    if not price:
        print("\033[31mAn error occured while fetching price\033[0m")
        return product

    price.replace('<span class="a-price-whole">',"")
    price.replace('<span class="a-price-decimal">.</span>', "")
    price = int(price)

    if price < product["expected_price"]:
        notification = Notify()
        notification.title = "Price below expected price"
        notification.message = f"Price: ₹{price}! Buy '{product["title"]}' Now." 
        notification.icon = "assets/price-tracker-icon.png"
        notification.application_name = "Arif Pirxada's Price Tracker"
        notification.audio = "assets/notification-sound.wav"

        notification.send()
        product["current_price"] = price
    
    elif price < product["current_price"]:
        notification = Notify()
        notification.title = "Price drop"
        notification.message = f"Price drop: from ₹{product["current_price"]} to ₹{price}! Product: {product["title"]}" 
        notification.icon = "assets/price-tracker-icon.png"
        notification.application_name = "Arif Pirxada's Price Tracker"
        notification.audio = "assets/notification-sound.wav"

        notification.send()
        product["current_price"] = price

    return product