import pythonwhois as whois
import re
from termcolor import colored

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
        print(colored(f"Domain Name: {domain_info.get('domain_name', 'N/A')}", "blue"))
        print(colored(f"Registrar: {domain_info.get('registrar', 'N/A')}", "blue"))
        print(colored(f"Creation Date: {domain_info.get('creation_date', 'N/A')}", "blue"))
        print(colored(f"Expiration Date: {domain_info.get('expiration_date', 'N/A')}", "blue"))
        print(colored(f"Name Servers: {domain_info.get('name_servers', 'N/A')}", "blue"))
    else:
        print(colored("No domain information available.", "red"))

def fetch_dns_records(domain_info):
    # Add code to fetch and display DNS records
    pass

def fetch_ssl_info(domain_info):
    # Add code to fetch and display SSL information
    pass

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
            fetch_dns_records(domain_info)
        elif choice == "2":
            fetch_ssl_info(domain_info)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
