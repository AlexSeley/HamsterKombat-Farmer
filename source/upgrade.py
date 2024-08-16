from source.functions import buy_upgrade, upgrades, _syncUpgrade


async def best_upgrade():
    dic = upgrades()

    upgradeIds = [item.get("id") for item in dic]
    elements = ["price", "profitPerHourDelta", "isAvailable", "isExpired"]
    syncedUpgrades = _syncUpgrade(upgradeIds, elements)

    profitItems = []
    for upgrade in syncedUpgrades:
        item = syncedUpgrades[upgrade]
        if item["isAvailable"] and not item["isExpired"] and item["price"]:
            if (item["profitPerHourDelta"] / item["price"]) >= 0.0005:  # The higher, the more profit
                profitItems.append(item["id"])

    _syn_cool = _syncUpgrade(profitItems, ["cooldownSeconds"])
    items = [item for item in _syn_cool if not _syn_cool[item].get('cooldownSeconds', None)]

    buy_upgrade(items)