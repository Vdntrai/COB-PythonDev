import re

def is_valid_ipv4(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

    if re.match(pattern, ip):
        octets = ip.split('.')
        for octet in octets:
            if not (0 <= int(octet) <= 255):
                return False
        return True
    else:
        return False

while True:
    ip_address = input("Enter an IPv4 address (TO QUIT, TYPE 'exit'): ")

    if ip_address.lower() == 'exit':
        break

    if is_valid_ipv4(ip_address):
        print(f"{ip_address} is a valid IPv4 address.")
    else:
        print(f"{ip_address} is not a valid IPv4 address.")
