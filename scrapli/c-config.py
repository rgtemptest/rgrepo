from scrapli import Scrapli


leaf3 = {
    "host": "leaf3",
    "auth_username": "admin",
    "auth_password": "admin",
    "auth_strict_key": False,
    "platform": "cisco_nxos"
}


dumb_acl = """ip access-list tacocat
  10 deny ip 8.8.8.8/32 any
  20 deny tcp 9.9.9.9 0.0.255.255 eq 22 any
  1000 permit ip any any"""


def main():
    conn = Scrapli(**leaf3)
    conn.open()

    print(conn.get_prompt())

    responses = conn.send_configs(configs=["interface loopback0", "description tacocat"])
    print(responses)

    print(conn.get_prompt())

    response = conn.send_command(command="show run interface loopback0")
    print(response.result)

    cfg_response = conn.send_config(config=dumb_acl)
    print(cfg_response)
    print(cfg_response.result)
    print(cfg_response.elapsed_time)

    cfg_from_file_response = conn.send_configs_from_file(file="intf_configs")
    print(cfg_from_file_response)


if __name__ == "__main__":
    main()

