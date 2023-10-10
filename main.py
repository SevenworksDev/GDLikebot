import aiohttp
import asyncio
import concurrent.futures
import random
from threading import Thread
from string import ascii_letters, digits
import requests

threadCount = int(input("How many likebot threads? (Less then 30 recommended): "))

def read_accounts(filename):
    accounts = []
    with open(filename, 'r') as file:
        for line in file:
            account_id, password = line.strip().split(' / ')
            accounts.append((account_id, password))
    return accounts

def download_proxies(proxy_url):
    response = requests.get(proxy_url)
    proxies = response.text.strip().split('\n')
    with open('proxies.txt', 'w') as file:
        for proxy in proxies:
            # Add 'http' scheme if missing
            if not proxy.startswith(('http://', 'https://')):
                proxy = 'http://' + proxy
            file.write(proxy + '\n')

def read_proxies(filename):
    proxies = []
    with open(filename, 'r') as file:
        for line in file:
            proxies.append(line.strip())
    return proxies

possible_letters = ascii_letters + digits

def generate_rs(n: int) -> str:
    return "".join(random.choices(possible_letters, k=n))

def generate_uuid(parts: [int] = (8, 4, 4, 4, 10)) -> str:
    return "-".join(map(generate_rs, parts))

def generate_udid(start: int = 100_000, end: int = 100_000_000) -> str:
    return "S" + str(random.randint(start, end))

def bot_wrapper(account_id, gjp, data, proxy):
    try:
        asyncio.run(bot(account_id, gjp, data, proxy))
    except:
        pass

async def bot(accountID, gjp, data, proxy):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://www.boomlings.com/database/likeGJItem211.php', data=data, headers={"User-Agent": ""}, proxy=proxy) as response:
            if response.status == 200:
                return "Sent"
            else:
                return f"Something went wrong - HTTP status {response.status}"

async def main():
    proxy_url = input("Enter the proxy URL: ")
    download_proxies(proxy_url)

    accounts = read_accounts('accounts.txt')
    proxies = read_proxies('proxies.txt')

    mode = input("Mode (1: Level | 2: Comment | 3: Post): ")
    item = input("ID: ")
    like = input("Like (0: Dislike | 1: Like): ")

    data = {
        "secret": "Wmfd2893gb7",
        "itemID": int(item),
        "type": int(mode),
        "like": int(like),
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "udid": generate_udid(),
        "uuid": generate_uuid()
    }

    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
        while True:
            account_id, gjp = random.choice(accounts)
            proxy = random.choice(proxies)
            print(f"Using account ID: {account_id}, Proxy: {proxy}")
            executor.submit(bot_wrapper, account_id, gjp, data, proxy)

if __name__ == "__main__":
    asyncio.run(main())