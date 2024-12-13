import requests
import fade
import os
from colorama import *

red = Fore.RED
cyan = Fore.CYAN
magenta = Fore.MAGENTA
yellow = Fore.YELLOW
green = Fore.GREEN
reset = Fore.RESET

api = "http://localhost:4000/products/"

def run():
    os.system("title Gay Khan CRUD 1.0")
    os.system("mode con: cols=90 lines=40")
    logo = '''

                         ██████╗ ██████╗  ██╗   ██╗ ██████╗ 
                        ██╔════╝ ██╔══██╗ ██║   ██║ ██╔══██╗
                        ██║      ██████╔╝ ██║   ██║ ██║  ██║
                        ██║      ██╔══██╗ ██║   ██║ ██║  ██║
                        ╚██████╗ ██║  ██║ ╚██████╔╝ ██████╔╝
                         ╚═════╝╚═╝  ╚═╝  ╚═════╝   ╚═════╝ 
                                            GAY Khan :)
'''
    while True:
        logo_text = fade.purpleblue(logo)
        print(logo_text)
        method_list = [f'{green}Read {reset}',f'{cyan}Create {reset}',f'{yellow}Update {reset}',f'{red}Delete {reset}']
        print(" Methods List")
        for id, method in enumerate(method_list,start=1):
            print(f" [{id}]", method)

        print("")
        method = int(input(" [+] Select method: "))
        print("")

        if(method == 1):
            get()
            x = input("Enter to continue ...")
            os.system('cls')
        elif(method == 2):
            post()
        elif(method == 3):
            put()
        elif(method == 4):
            delete()


def get():

    req = requests.get(api)
    if req.status_code == 200:
        json = req.json()

        for item in json:
            print(f"{f' {magenta}ID':<5} {'Category':<12} {'Name':<20} {'Price':<10} {'Description':<30} {'Stock':<15} {reset}")
            print(f" {item['id']:<5} {item['category_id']:<12} {item['name']:<20} {item['price']:<10} {item['description']:<30} {item['unit_in_stock']:<15}")
            print("-" * 85)

        
def post():
    catID = int(input(" Category ID: "))
    name = input(" Name: ")
    price = int(input(" Price: "))
    desc = input(" Description: ")
    stock = int(input(" Stock: "))

    payload = {
        "category_id": catID,
        "name": name,
        "price": price,
        "description": desc,
        "unit_in_stock": stock
    }

    req = requests.post(api, json=payload)
    if(req.status_code == 200):
        print("")
        print(" [+] POST Success")
    else:
        print(" [!] Error")

def put():

    productID = int(input(" Product ID: "))

    catID = int(input(" Category ID: "))
    name = input(" Name: ")
    price = int(input(" Price: "))
    desc = input(" Description: ")
    stock = int(input(" Stock: "))

    put_url = f"{api}{productID}"

    payload = {
        "category_id": catID,
        "name": name,
        "price": price,
        "description": desc,
        "unit_in_stock": stock
    }
    req = requests.put(put_url, json=payload)
    if(req.status_code == 200):
        print("")
        print(" [+] PUT Success")
    else:
        print(" [!] Error", req.status_code)


def delete():

    productID = int(input(" Product ID: "))
    delete_url = f"{api}{productID}"
    req = requests.delete(delete_url)
    if(req.status_code == 200):
        print("")
        print(" [+] DELETE Success")
    else:
        print(" [!] Error", req.status_code)


run()