import time
import os
from functions import data_management, price_tracking   
import json

"""
Functions =>  
* show_help
* clear_terminal
* get_current_time
* main

"""


def show_help():
    print("h -> help")
    print("add -> add product")
    print("remove -> remove product")
    print("show -> show products")
    print("start -> start tracking product price")
    print("cls -> Clear terminal")
    print("q -> Quit\n")
        

def clear_terminal():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-based systems (Linux, macOS, etc.)
        os.system('clear')

def get_current_time():
    current_time_seconds = time.time()
    current_struct_time = time.localtime(current_time_seconds)
    formatted_time = time.strftime("%I:%M %p", current_struct_time)

    return formatted_time


def main():
    data = data_management.get_data()
    print("\033\n[32mpress h to for help.\033[0m")

    while True:
        prompt = input('\033[95m' + "\nEnter your prompt: " + '\033[0m')
        print("\n")

        if prompt == "h":
            show_help()
        elif prompt == "show":
            data_management.show_products(data)
        elif prompt == "add":
            data = data_management.add_product(data)
        elif prompt == "remove":
            if len(data) > 0:
                data = data_management.remove_product(data)
            else:
                print("\033[31mPlease add some products! \033[0m \n")
        elif prompt == "start":
            if len(data) == 0:
                print("\033[31mPlease add some products! \033[0m \n")
            else:
                # START TRACKING PRICE =>
                while True:
                    print("\033[95m-------------------------")
                    cur_time = get_current_time()
                    print(f"\033[32mStarted New Price Fetch... ---> at \033[33m{cur_time}")
                    print("\033[95m-------------------------\033[0m")
                    for product in data:
                        print("\n\033[32m")
                        print(f"Fetching: \033[0m{product["title"][:50]}...\033[32m")
                        before_price = product["current_price"]

                        product = price_tracking.check_price(product)

                        print(f"Current Price: \033[0m{product["current_price"]}\033[32m")

                        if before_price > product["current_price"]:
                            print(f"\033[95mPrice dropped from ₹{before_price} to ₹{product["current_price"]}\033[0m")
                            print(f"\033[95mExpected Price: {product["expected_price"]}\033[0m")
                        elif before_price < product["current_price"]:
                            print(f"\033[31mPrice increased from ₹{before_price} to ₹{product["current_price"]}\033[0m")
                        elif before_price == product["current_price"]:
                            print("\033[95mNo change in price.\033[0m")


                        print("\033[95m-------------------------\033[0m")
                        # Fetch product price every 5 seconds
                        time.sleep(5)

                    print("\n\033[32mPrice fetch completed.\033[0m\n\n\n")
                    # Update the data =>
                    with open("data.json", "w") as f:
                        json.dump(data, f, indent=4)

                    time.sleep(3600) # Check price every hour
        elif prompt == "q":
            break
        elif prompt == "cls":
            clear_terminal()
        else:
            print("\033[31mPlease enter a valid command! Press h for help.\033[0m")
        


if __name__ == "__main__":
    main()