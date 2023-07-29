import os
import time
from colorama import Fore
import socket
import requests
from getpass import getpass
from utils import (
    ip_lookup,
    phonenumber_lookup,
    websearch,
    ig_scrape,
)
from helper import printer, url_helper
2
if os.name == "nt":
    os.system("cls")
    os.system("ITMS 448 - 548")
if os.name == "posix":
    os.system("clear")

version = "0.2.12a"


def internet_check():
    """
    Checks if the internet connection is available.

    :return: None
    """
    try:
        socket.create_connection(("www.google.com", 80))
        printer.success("\nInternet Connection is Available!")
        return None
    except OSError:
        printer.warning("\nWarning! Internet Connection is Unavailable!")
        return None




def print_banner():
    """
    Prints the banner of H4X-Tools.
    """
    print(Fore.CYAN + f"""
ITMS 448 - 548 - OSINT
    """)


def print_about():
    """
    Prints the about text.
    """
    print(Fore.GREEN)
    


def print_donate():
    """
    Prints the donate text.
    """
    printer.nonprefix(f"""{Fore.GREEN}
            """)


def print_menu():
    """
    Prints the main menu of H4X-Tools.
    """
    print(Fore.CYAN)
    print("[1] Web Search           ||   [2] Phone Lookup")
    print("[3] IP Lookup            ||   [4] Instagram Scraper")   
    print("[5] Exit")        
    print("\n")


def handle_ig_scrape():
    """
    Handles the IG Scrape util.

    Note, you have to log in to Instagram in order to use this util.
    """
    printer.warning("NOTE! You have to log in to Instagram everytime in order to use this util.")
    printer.warning("I suggest you to create a new account for this purpose.")
    username = str(input("Your username : "))
    password = getpass("Your password : ")
    target = str(input("Enter a target username : \t")).replace(" ", "_")
    ig_scrape.Scrape(username, password, target)
    time.sleep(1)



def handle_web_search():
    """
    Handles the Web Search util.
    """
    query = str(input("Search query : \t"))
    websearch.Search(query)


def handle_phone_lookup():
    """
    Handles the Phone number Lookup util.
    """
    no = str(input("Enter a phone-number with country code : \t"))
    phonenumber_lookup.LookUp(no)


def handle_ip_lookup():
    """
    Handles the IP/Domain Lookup util.
    """
    ip = str(input("Enter a IP address OR domain : \t"))
    ip_lookup.Lookup(ip)





# Create a dictionary to map menu options to corresponding functions
menu_options = {
    "1": handle_web_search,
    "2": handle_phone_lookup,
    "3": handle_ip_lookup,
    "4": handle_ig_scrape,
}


def __main__():
    """
    Main function.
    """
  
    # Check if the user is using the latest version

    while True:
        print_banner()
        time.sleep(1)
        print_menu()
        a = input("[*] Select your option : \t")

        if a in menu_options:
            menu_options[a]()  # Call the corresponding function based on the selected option
            time.sleep(3)  # Sleep so user has time to see results.
        elif a == "5":
            printer.warning("Exiting...")
            printer.info("Thanks for using ITMS 448 - 548 - OSINT")
            time.sleep(1)
            print(Fore.RESET)
            break
        else:
            printer.error("Invalid option!")
            time.sleep(2)


if __name__ == "__main__":
    __main__()
