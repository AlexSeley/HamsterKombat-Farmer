import asyncio
from source.clicker import availableTaps, maxTaps, tapper, boost
from source.upgrade import best_upgrade


async def clicker():
    while True:
        if availableTaps() <= 200:
            await boost()

        if availableTaps() == maxTaps():
            await tapper()
        else:
            await asyncio.sleep(50)


async def upgrades():
    while True:
        await best_upgrade()
        await asyncio.sleep(100)


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(upgrades())
        tg.create_task(clicker())

if __name__ == "__main__":
    asyncio.run(main())