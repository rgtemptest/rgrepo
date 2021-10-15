from scrapli import Scrapli


rtr1 = {
    "host": "rtr1",
    "auth_username": "admin",
    "auth_password": "admin",
    "auth_strict_key": False,
#    "transport": "telnet",
    "platform": "cisco_iosxe"
}


def main():
    conn = Scrapli(**rtr1)
    conn.open()

    interact_events = [
        ("clear logging", "Clear logging buffer [confirm]"),
        ("", "rtr1#")
    ]

    response = conn.send_interactive(interact_events=interact_events)

    print(response, type(response), dir(response))

    print(response.result)


if __name__ == "__main__":
    main()

