from scrapli import Scrapli
from ntc_templates.parse import parse_output


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
    response = conn.send_command(command="show version")

    parsed_output = parse_output(platform="arista_eos", command="show version", data=response.result)
    print(parsed_output)


if __name__ == "__main__":
    main()

