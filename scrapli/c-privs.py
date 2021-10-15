from scrapli import Scrapli


leaf1 = {
    "host": "leaf1",
    "auth_username": "admin",
    "auth_password": "admin",
    "auth_strict_key": False,
    "platform": "arista_eos"
}


def main():
    conn = Scrapli(**leaf1)
    conn.open()

    print(conn.get_prompt())

    print(conn.privilege_levels)

    print(conn.privilege_levels["privilege_exec"])

    print(dir(conn.privilege_levels["privilege_exec"]))

    print(conn.default_desired_privilege_level)

    conn.acquire_priv(desired_priv="exec")

    response = conn.send_command(command="show run")
    print(response.result)


if __name__ == "__main__":
    main()

