import requests,random,time
from string import ascii_letters, digits

possible_letters = ascii_letters + digits

def generate_rs(n: int) -> str:
    return "".join(random.choices(possible_letters, k=n))

def generate_uuid(parts: [int] = (8, 4, 4, 4, 10)) -> str:
    return "-".join(map(generate_rs, parts))

def login_to_account(username, password):
    time.sleep(1.5)
    print("Logging in...")
    url = "http://www.boomlings.com/database/accounts/loginGJAccount.php"
    data = {
        "udid": generate_uuid(),
        "userName": username,
        "password": password,
        "secret": "Wmfv3899gc9"
    }

    headers = {
        "User-Agent": ""
    }

    response = requests.post(url, data=data, headers=headers)
    account_id = response.text.split(',')[0]
    print(account_id)
    return account_id

def main():
    updated_lines = []
    with open("accounts.txt", "r") as file:
        for line in file:
            username, password, email = line.strip().split(' / ')
            account_id = login_to_account(username, password)
            updated_lines.append(f"{username} / {password} / {account_id}\n")

    with open("accounts.txt", "w") as file:
        file.writelines(updated_lines)

if __name__ == "__main__":
    main()

