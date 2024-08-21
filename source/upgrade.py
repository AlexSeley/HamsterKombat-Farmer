from source.functions import buy_upgrade, upgrades, _syncUpgrade


async def best_upgrade():
    dic = upgrades()

    upgradeIds = [item["id"] for item in dic]
    elements = ["price", "profitPerHourDelta", "isAvailable", "isExpired"]
    syncedUpgrades = _syncUpgrade(upgradeIds, elements)

    profitItems = []
    for upgrade in syncedUpgrades:
        item = syncedUpgrades[upgrade]
        if item["isAvailable"] and not item["isExpired"] and item["price"]:
            if (item["profitPerHourDelta"] / item["price"]) >= 0.00045:  # The higher, the more profit 0.0005
                profitItems.append(item["id"])

    _syn_cool = _syncUpgrade(profitItems, ["cooldownSeconds"])
    items = [item for item in _syn_cool if not _syn_cool[item].get('cooldownSeconds', None)]

    buy_upgrade(items)