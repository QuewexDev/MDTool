import webhook
import time
import os
import sys
from colorama import init, Fore, Back

ROOT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

os.chdir(ROOT_DIR)

init()

banner = f"""{Fore.BLUE}
███╗   ███╗██████╗ ████████╗ ██████╗  ██████╗ ██╗     
████╗ ████║██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██╔████╔██║██║  ██║   ██║   ██║   ██║██║   ██║██║     {Fore.CYAN}
██║╚██╔╝██║██║  ██║   ██║   ██║   ██║██║   ██║██║     
██║ ╚═╝ ██║██████╔╝   ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝     ╚═╝╚═════╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝{Fore.RESET}"""

def menu():
    print(banner)
    print("=========================================================")
    print("| 1. Send Webhook | 2. Spam Webhook | 3. Get Guild Info |")
    print("| 4. Send Webhook with URL from url.txt | 5. Exit       |")
    print("=========================================================\n")

    try:
        choice = int(input("> "))
    except:
        print("Invalid choice. Please choose a number from the menu.")
        return

    match choice:
        case 1:
            try:
                url = str(input("Webhook URL: "))
                message = str(input("Message: "))
                username = str(input("Username (left blank to use standart): "))
                webhook.send_webhook(url, message, username)
            except ValueError:
                print("Incorrect input")
        
        case 2:
            try:
                url = str(input("Webhook URL: "))
                message = str(input("Message: "))
                username = str(input("Username (left blank to use standart): "))
                times = int(input("How much times: "))
                delay = float(input("Delay (Can be float number): "))
                webhook.spam_webhook(url, message, username, delay, times)
            except ValueError:
                print("Incorrect input")
        
        case 3:
            try:
                url = str(input("Webhook URL: "))
                print(webhook.getGuildInfo(url))
                input("Press enter to continue")
            except Exception as e:
                print(e)
        
        case 4:
            try:
                if not os.path.isfile("url.txt"):
                    print("Failed to load url.txt! Type Webhook URL here.")
                    url = str(input("Webhook URL: "))
                    with open("url.txt", "w+") as f:
                        f.write(url)
                else:
                    with open("url.txt", "r") as f:
                        url = f.read()
                
                message = str(input("Message: "))
                username = str(input("Username (left blank to use standart): "))
                webhook.send_webhook(url, message, username)
            except ValueError:
                print("Incorrect input")
        
        case 5:
            exit()
        
        case _:
            print("Incorrect choice!")

if __name__ == "__main__":
    while True:
        os.system("cls" if sys.platform == "win32" else "clear")
        menu()
