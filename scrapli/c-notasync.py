from datetime import datetime

from scrapli import Scrapli


hosts = ["leaf1", "leaf2", "spine1"]


def main():
    conns = [
       Scrapli(
           host=host,
           auth_username="admin",
           auth_password="admin",
           auth_strict_key=False,
           platform="arista_eos"
       )
       for host in hosts
    ]

    start_time = datetime.now()

    for conn in conns:
        conn.open()
        response = conn.send_commands(commands=["show run", "show version", "show run"])

        print(f"{conn.host} took {response[2].finish_time - response[0].start_time} seconds to execute the commands")

    end_time = datetime.now()

    print(f"total execution time was {end_time - start_time} seconds")


if __name__ == "__main__":
    main()

