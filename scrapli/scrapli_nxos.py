from scrapli import Scrapli

def main():
    leaf3 = {
        "host": "172.20.20.21",
        "auth_username": "admin",
        "auth_password": "admin",
        "auth_strict_key": False,
        "platform": "arista_eos",
        "transport": "ssh2"
    }

    conn = Scrapli(**leaf3)
    conn.open()
    
    print(conn, type(conn), dir(conn))

    print(conn.get_prompt())
    
    response = conn.send_command("show version")
    print(response,type(response),dir(response))
    print(response.result)
    print(response.failed)

    fail_response = conn.send_command("hi")
    print(fail_response.result)
    print(fail_response.failed)

    conn.close()

if __name__ == "__main__":
    main()
