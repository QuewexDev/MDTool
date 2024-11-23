import requests
import time
import json
import string

# You can use it at your script as a module
# by Quewex

def send_webhook(url = None, message = "This message created using QuewexWebhook", username = "QuewexWebhook"):
    data = {
        "content" : message
    }

    if string.ascii_lowercase in username.lower():
        data["username"] = username

    if url == None:
        print("URL is not specified")
        return
    
    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)

def spam_webhook(url, message = "This message created using QuewexWebhook", username = "QuewexWebhook", delay = 0.5, times=5):
    data = {
        "content" : message
    }

    if string.ascii_lowercase in username.lower():
        data["username"] = username

    if url == None:
        print("URL is not specified")
        return
    
    if times > 0:
        for i in range(times):
            result = requests.post(url, json = data)
            time.sleep(delay)
    elif times == -1:
        print("Press CTRL+C to stop")
        try:
            while True:
                result = requests.post(url, json = data)
                try:
                    result.raise_for_status()
                except requests.exceptions.HTTPError as err:
                    print(err)
                    break
                time.sleep(delay)
        except KeyboardInterrupt:
            print("Stopped")

def getGuildInfo(url):
    result = requests.get(url)

    return result.json()