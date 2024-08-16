import requests
import json
import time
from source.data import headers, config

def buy_upgrade(idUpgrade: list, price=config["upgrade_priceMax"], return_seconds=False):
    link = 'https://api.hamsterkombatgame.io/clicker/buy-upgrade'

    priceId = _syncUpgrade(idUpgrade, ["price"])

    for i in priceId:
        priceItem = priceId.get(i).get("price")
        if priceItem >= price:
            print(f"Price {priceItem} is too high, should be lower than {price}")
            if return_seconds:
                return "Price is too high"

        else:
            continue

    for i in idUpgrade:
        data = {"timestamp": int(time.time()),
                "upgradeId": i}

        data = json.dumps(data)

        try:
            res = requests.post(link, headers=headers, data=data)
        except Exception as ex:
            print(buy_upgrade.__name__, ex)
            return False

        if return_seconds:
            if res.status_code == 400:
                print("400")
                cooldownSeconds = (_syncUpgrade([i], ["cooldownSeconds"]))
                return cooldownSeconds.get(i).get('cooldownSeconds')

        print(f"{i} - {res.status_code}")

def upgrades():    # Get information about all upgrades of the user
    link = "https://api.hamsterkombatgame.io/clicker/upgrades-for-buy"
    try:
        res = requests.post(link, headers=headers)
        upgradesForBuy = res.json()
        upgradesForBuy = upgradesForBuy.get("upgradesForBuy")
        dic = [ele for ele in upgradesForBuy if isinstance(ele, dict)]

        return dic

    except Exception as ex:
        print(upgrades.__name__, ex)
        return {}


def _syncUpgrade(upgradeId: list, elements: list):    # Get information about specific upgrades of the user and elements
    dic = upgrades()
    return_dic = {}

    for item in dic:
        if item.get("id") in upgradeId:
            item_dic = {'id': item.get("id")}
            for element in elements:
                item_dic[element] = item.get(element)
                return_dic[item["id"]] = item_dic

    return return_dic
