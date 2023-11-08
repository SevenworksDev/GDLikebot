import requests, random, base64, itertools, hashlib, threading, time
from string import ascii_letters, digits

possible_letters = ascii_letters + digits

print("Comment Like/Dislike bot By Sevenworks!!! l m a o  x D D D D D D")
comid = input("Comment ID: ")
levelid = "96134493"
liketype = input("Like/Dislike (0/1): ")

def icedcave_plz_unblock_me(bozo):
    with open(bozo, 'r') as file:
        proxies = [line.strip() for line in file]
    return proxies

def get_proxy(proxies):
    return random.choice(proxies)

proxies = icedcave_plz_unblock_me("proxies.txt")

def SAF(file_path):
    gjuser = []
    gjpass = []
    gjaccid = []
    with open(file_path, 'r') as file:
        for line in file:
            homer, simpson, doh = line.strip().split(' / ')
            gjuser.append(homer)
            gjpass.append(simpson)
            gjaccid.append(doh)
    return gjuser, gjpass, gjaccid

gjuser, gjpass, gjaccid = SAF("accounts.txt")

def xor(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, itertools.cycle(key)))

def gjp_encrypt(data):
    return base64.b64encode(xor(data,"37526").encode()).decode()

def generate_chk(values: [int, str] = [], key: str = "", salt: str = "") -> str:
    values.append(salt)
    string = ("").join(map(str, values))
    hashed = hashlib.sha1(string.encode()).hexdigest()
    xored = xor(hashed, key)
    final = base64.urlsafe_b64encode(xored.encode()).decode()
    return final

def generate_rs(n: int) -> str:
    return ("").join(random.choices(possible_letters, k=n))

def generate_uuid(parts: [int] = (8, 4, 4, 4, 10)) -> str:
    return ("-").join(map(generate_rs, parts))

def generate_udid(start: int = 100_000, end: int = 100_000_000) -> str:
    return "S" + str(random.randint(start, end))

def bot(proxy):
    rand = random.randint(0, len(gjuser) - 1)
    uuid = generate_uuid()
    udid = generate_udid()
    rs = generate_rs(10)
    data = {
        "gameVersion": "21",
        "binaryVersion": "35",
        "gdw": "0",
        "accountID": gjaccid[rand],
        "gjp": gjp_encrypt(gjpass[rand]),
        "udid": udid,
        "uuid": uuid,
        "itemID": comid,
        "like": liketype,
        "type": "2",
        "secret": "Wmfd2893gb7",
        "special": levelid,
        "rs": rs,
        "chk": generate_chk([levelid, comid, liketype, "2", rs, gjaccid[rand], udid, uuid], "58281", "ysg6pUrtjn0J")
    }
    try:
      req = requests.post("http://www.boomlings.com/database/likeGJItem211.php", data=data, headers={"User-Agent": ""}, proxies=proxy)
      if req.text == "1":
          print(f"[SUCCESS]: {str(gjuser[rand])} liked by {str(proxy)}")
      else:
          error_keywords = ["</", "Cloudflare", "error code:", "nginx", "apache"]
          if any(keyword in req.text for keyword in error_keywords):
              pass
          else:
              print(f"[ERROR IN PROXY]: {req.text}")
    except:
      pass

while True:
  try:
    proxy = {"http": get_proxy(proxies), "https": get_proxy(proxies)}
    threading.Thread(target=bot, args=(proxy,)).start()
  except:
    pass