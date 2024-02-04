import dns.resolver
import ssl
import whois
import re
from termcolor import colored
from datetime import datetime

def validate_domain_name(domain_name):
    pattern = re.compile(r"^(?:(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+[A-Za-z]{2,6}$")
    return bool(pattern.match(domain_name))

def get_domain_info(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        return domain_info
    except Exception as e:
        print(f"Error fetching information for {domain_name}: {e}")
        return None

def display_domain_info(domain_info):
    if domain_info:
        print(colored("Domain Information:", "green"))
        print(colored(f"Domain Name: {domain_info.domain_name}", "blue"))
        print(colored(f"Registrar: {domain_info.registrar}", "blue"))
        print(colored(f"Creation Date: {domain_info.creation_date}", "blue"))
        print(colored(f"Expiration Date: {domain_info.expiration_date}", "blue"))
        print(colored(f"Name Servers: {domain_info.name_servers}", "blue"))
    else:
        print(colored("No domain information available.", "red"))

def fetch_dns_records(domain_name):
    try:
        answers = dns.resolver.resolve(domain_name, 'A')
        ip_addresses = [answer.address for answer in answers]
        print(colored(f"DNS Records (A): {', '.join(ip_addresses)}", "blue"))
    except dns.resolver.NoAnswer:
        print(colored("No DNS records found.", "red"))
    except dns.exception.DNSException as e:
        print(colored(f"Error fetching DNS records: {e}", "red"))

def fetch_ssl_info(domain_name):
    try:
        cert = ssl.get_server_certificate((domain_name, 443))
        x509 = ssl.load_certificate(ssl.PEM, cert)
        expiration_date = x509.get_notAfter().decode('utf-8')
        expiration_date = datetime.strptime(expiration_date, '%Y%m%d%H%M%SZ')

        print(colored(f"SSL Information - Expiration Date: {expiration_date}", "blue"))
    except ssl.SSLError as e:
        print(colored(f"Error fetching SSL information: {e}", "red"))

def main():
    domain_name = input("Enter the domain name: ")
    if not validate_domain_name(domain_name):
        print("Invalid domain name. Please enter a valid domain.")
        return

    domain_info = get_domain_info(domain_name)
    display_domain_info(domain_info)

    # Interactive menu
    while True:
        print("\nOptions:")
        print("1. Fetch DNS Records")
        print("2. Fetch SSL Information")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            fetch_dns_records(domain_name)
        elif choice == "2":
            fetch_ssl_info(domain_name)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
