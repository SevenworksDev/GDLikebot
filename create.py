import requests
import random
import string
import time
import sys

print("Sevenworks Account Creator")
usernameInput = ""
nameString = 10

# Load proxies from the proxies.txt file
with open("proxies.txt", "r") as proxies_file:
    proxies = proxies_file.read().splitlines()

def adduser(myUsername, myPassword, myEmail):
    with open("accounts.txt", "a") as f:
        print(myUsername + " / " + myPassword + " / " + myEmail, file=f)

def create(gjuser, gjpass, gjemail, proxies):
    headers = {"User-Agent": ""}
    data = {
        "userName": gjuser,
        "password": gjpass,
        "email": gjemail + "@mail.com",
        "secret": "Wmfv3899gc9"
    }

    while True:
        # Use a random proxy from the list
        proxy_url = random.choice(proxies)
        proxies_dict = {'http': proxy_url, 'https': proxy_url}

        try:
            req = requests.post("http://www.boomlings.com/database/accounts/registerGJAccount.php", data=data, headers=headers, proxies=proxies_dict, timeout=1.5)

            if req.text == "1":
                adduser(gjuser, gjpass, gjemail)
                print("Account Creator Status: " + req.text)
                sys.exit()

            print("Failed - Retrying with a different proxy")

        except requests.exceptions.RequestException as e:
            # Handle proxy or other request errors here
            print("Request Error:", e)

while True:
    myEmail = input("E-mail (@mail.com): ")
    f777 = ''.join(random.choices(string.ascii_letters, k=nameString))
    colbreakz = ''.join(random.choices(string.ascii_letters, k=7))
    myUsername = usernameInput + f777
    myPassword = colbreakz

    print("Creating User: " + myUsername)
    create(myUsername, myPassword, myEmail, proxies)
