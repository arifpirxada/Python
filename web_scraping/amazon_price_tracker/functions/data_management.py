import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os

"""
Functions =>
* show_products
* product_already_exists
* add_product
* remove_product
* get_data

"""

def show_products(data):
    i = 0
    for product in data:
        i = i + 1
        print(f"\nProduct {i}.")
        print(f"\t\033[33mTitle: \033[0m{product["title"]}\n")
        print(f"\t\033[33mUrl: \033[0m{product["url"]}\n")
        print(f"\t\033[33mCurrent Price: \033[0m{product["current_price"]}\n")
        print(f"\t\033[33mExpected Price: \033[0m{product["expected_price"]}")
        print("\t\033[33m -------------------------------------------------- \033[0m")
    if i == 0:
        print("There are no products!")


def product_already_exists(data, link):
    if not data:
        return False
    
    for product in data:
        if product["url"] == link:
            return True
        
    return False

def add_product(data):

    # PURPLE COLOR: '\033[95m'
    # END COLOR: \033[0m

    print("\033[32mAdd Product\033[0m")
    print("\033[32m------------\033[0m")
    url = input("\033[95mEnter url: \033[0m")
    
    # check if number of products are already 10
    if len(data) == 10:
        print("\n\033[31m10 products already added! cannot add more.\033[0m")
        return data

    # check if product already exists =>
    if product_already_exists(data, url):
        print("\n\033[31mProduct already exists!\033[0m")
        return data

    expected_price = int(input('\033[95m' + "\nExpected Price: \033[33m"))
    print("\033[0m")

    try:
        print("\n\033[32m-------------------------")
        print("Fetching product details...\033[0m")

        ua = UserAgent()
        r = requests.get(url, headers={'User-Agent': ua.random})
    except requests.exceptions.RequestException as e:
        print("\033[31mAn error occured while fetching product data! Please try later\033[0m") # Red text
        return data
    if not r:
        print("\033[31mError fetching data! Please try later\033[0m") # Red text
        return data
    soup = BeautifulSoup(r.content, "html.parser")

    title = soup.find("span", {"id": "productTitle"})

    if not title:
        print("\033[31mError fetching product title! Please try later\033[0m") # Red text
        return data
    title = title.text.strip()
    
    current_price = soup.find("span", {"class": "a-price-whole"})
    if not current_price:
        print("\033[31mError fetching product price! Please try later\033[0m") # Red text
        return data
    
    current_price = int(current_price.text.replace(",", "").replace(".", ""))

    data.append({
        "title": title,
        "url": url,
        "expected_price": expected_price,
        "current_price": current_price
    })

    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data.json')
    with open (file_path, "w") as dt:
        json.dump(data, dt, indent=4)
        print("\n\033[32mProduct has been Added!")
        print("-------------------------\033[0m")

    
    return data

def remove_product(data):
    print("\033[32mDelete Product\033[0m")
    print("\033[32m---------------\033[0m")
    url = input("\033[95mEnter url: \033[0m")
    
    new_data = []

    for product in data:
        if product["url"] != url:
            new_data.append(product)

    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data.json')
    with open(file_path, "w") as f:
        json.dump(new_data, f, indent=4)
        print("\n\033[32mProduct has been Removed if it existed!")
        print("-----------------------------------\033[0m")


    return new_data 


def get_data():
    try:
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data.json')
        with open (file_path, "r") as f:
            try:
                dt = json.load(f)
                if len(dt) == 0:
                    print("\033[32mPlease add some product to start price tracking!\033[0m") # Green coloured text
                return dt
            except json.JSONDecodeError:
                # Set data.json to empty array 
                with open (file_path, "w") as f:
                    f.write("[]")
                    return []
    except FileNotFoundError:
        with open (file_path, "w") as f:
            f.write("[]")
            return []
