from ttp import ttp
from scrapli import Scrapli


leaf1 = {
    "host": "leaf1",
    "auth_username": "admin",
    "auth_password": "admin",
    "auth_strict_key": False,
    "platform": "arista_eos"
}


arista_show_version_template = """ cEOSLab
Hardware version: {{ hw_version }}
Serial number:
Hardware MAC address: 001c.7309.c5fc
System MAC address: {{ sys_mac }}

Software image version: {{ image }} (engineering build)
Architecture: i686
Internal build version: 4.26.1F-22602519.4261F
Internal build ID: d68304e7-3aa6-47a0-ae3a-5354a02f6393
Image format version: 01.00

cEOS tools version: 1.1
Kernel version: 5.11.0-1017-gcp

Uptime: 0 weeks, 0 days, 2 hours and 0 minutes
Total memory: {{ total_memory }} kB
Free memory: {{ free_memory }} kB
"""


def main():
    conn =  Scrapli(**leaf1)
    conn.open()
    response = conn.send_command(command="show version")

    parser = ttp(data=response.result, template=arista_show_version_template)
    parser.parse()

    print(parser.result())


if __name__ == "__main__":
    main()

