import asyncio
from datetime import datetime

from scrapli import AsyncScrapli

hosts = ["leaf1", "leaf2", "spine1"]


async def main():
    conns = [
        AsyncScrapli(
            host=host,
            auth_username="admin",
            auth_password="admin",
            auth_strict_key=False, 
            transport="asyncssh",
            platform="arista_eos",
        )
        for host in hosts
    ]
    
    start_time = datetime.now()
    
    await asyncio.gather(*[conn.open() for conn in conns])
    results = await asyncio.gather(
        *[
            conn.send_commands(commands=["show run", "show version", "show run"])
            for conn in conns
        ]
    )
    
    end_time = datetime.now()
    
    for result in results:
        print(f"{result.host} took {result[2].finish_time - result[0].start_time} seconds to execute the commands")

    print(f"total execution time was {end_time - start_time} seconds")

if __name__ == "__main__":
    asyncio.run(main())


