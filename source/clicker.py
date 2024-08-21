import requests
from source.data import headers, sync
import time
import json

def syncTaps():
    try:
        return sync().get("clickerUser")
    except Exception as ex:
        print("SyncTaps failed")
        print(syncTaps.__name__, ex)
        return {}


def availableTaps(): return syncTaps().get("availableTaps", 0)
def maxTaps(): return syncTaps().get("maxTaps", 0)

async def tapper():
    link = "https://api.hamsterkombatgame.io/clicker/tap"
    data = {
        "availableTaps": 0,
        "count": maxTaps(),
        "timestamp": int(time.time())}

    data = json.dumps(data)

    try:
        requests.post(link, headers=headers, data=data)
        print("Click")
    except Exception as ex:
        print(tapper.__name__, ex)


async def boost():
    link = "https://api.hamsterkombatgame.io/clicker/buy-boost"

    data = {
        "boostId": "BoostFullAvailableTaps",
        "timestamp": int(time.time())}
    data = json.dumps(data)

    try:
        res = requests.post(link, headers=headers, data=data)
        if res.status_code == 200:
            print("Boost")
    except Exception as ex:
        print("Boost failed")
        print(boost.__name__, ex)
        return {}