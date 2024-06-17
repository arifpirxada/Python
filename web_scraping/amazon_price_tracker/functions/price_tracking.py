from notifypy import Notify
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def check_price(product):

    try:
        ua = UserAgent()
        r = requests.get(product["url"], headers={'User-Agent': ua.random})
    except requests.exceptions.RequestException as e:
        print("\033[31mAn error occured while fetching data\033[0m")
        return product

    soup = BeautifulSoup(r.content, "html.parser")

    # Find the price =>
    price_text = soup.find("span", class_="a-price-whole").text
    price = price_text.replace(",","")
    price = price.rstrip(".")
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