import ssl
import socket
from datetime import datetime

def getsslexpirydate(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                expiry_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                return expiry_date
    except Exception as e:
        return f"Error fetching SSL info for {domain}: {e}"

def sslread():
    with open("ssl_checker\domain_list.txt", "r") as file:
        ssl_domain = file.read().splitlines()
        for domain in ssl_domain:
            expiry_date = getsslexpirydate(domain)
            print(f"Domain: {domain}, SSL Expiry Date: {expiry_date}")

if __name__ == "__main__":
    sslread()