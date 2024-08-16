import requests

config = {}

with (open('configuration.txt', "r") as file):
    for line in file:
        key, value = map(str.strip, line.split(':', 1))
        if key == "token":
            config[key] = value
        else:
            if value.isdigit():
                config[key] = int(value)
            else:
                config[key] = float('inf')

def configuration():
    if not config.get("token"):
        print("Invalid token")
        quit()

headers = {
    'Accept': '*    /*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': f'Bearer {config["token"]}',
    'Connection': 'keep-alive',
    'Origin': 'https://hamsterkombatgame.io',
    'Referer': 'https://hamsterkombatgame.io/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'android',
    'Content-Type': 'application/json'
    }

def sync():
    link = "https://api.hamsterkombatgame.io/clicker/sync"
    try:
        return requests.post(link, headers=headers).json()
    except Exception as ex:
        print(sync.__name__, ex)
        print("Sync failed")