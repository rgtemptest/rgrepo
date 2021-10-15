from scrapli import Scrapli


def main():
    leaf2 = {
        "host": "172.20.20.22",
        "auth_username": "admin",
        "auth_password": "admin",
        "platform": "arista_eos",
        "transport": "telnet"
    }

    conn = Scrapli(**leaf2)

    conn.open()

    multi_response = conn.send_commands(["show run", "show ip int brief" ])

    for response in multi_response:
        print(response.result)

    print(multi_response.result)


if __name__ == "__main__":
    main()

