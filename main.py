import asyncio
import requests
from source.clicker import availableTaps, maxTaps, tapper, boost
from source.upgrade import best_upgrade
from source.data import configuration


async def clicker():
    while True:
        try:
            if availableTaps() <= 200:
                await boost()

            if availableTaps() == maxTaps():
                await tapper()
            else:
                await asyncio.sleep(50)

        except Exception as ex:
            print(ex)


async def upgrades():
    while True:
        try:
            await best_upgrade()
        except Exception as ex:
            print(ex)

        await asyncio.sleep(100)

async def internet():
    while True:
        try:
            requests.get("https://google.com")
            print("Connected")
        except requests.ConnectionError:
            print("Not connected")

        await asyncio.sleep(3600)

async def main():
    print("App started")
    async with asyncio.TaskGroup() as tg:
        tg.create_task(internet())
        tg.create_task(upgrades())
        tg.create_task(clicker())

if __name__ == "__main__":
    configuration()
    asyncio.run(main())
