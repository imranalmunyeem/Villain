import subprocess
import re
from prettytable import PrettyTable
from cryptography.fernet import Fernet
import concurrent.futures
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

netsh_path = r"C:\Windows\System32\netsh"

# Run the command to get the list of all wifi profiles
try:
    command_output = subprocess.run([netsh_path, "wlan", "show", "profiles"], capture_output=True, text=True, check=True).stdout
except subprocess.CalledProcessError as e:
    print(f"{Fore.RED}Error executing command: {e}{Style.RESET_ALL}")
    exit()

# Extract profile names
profile_names = [line.strip() for line in command_output.splitlines() if "All User Profile" in line]

# Create a list to store WiFi information
wifi_list = []

# Function to check if Security key is present and get password
def get_password(profile_info_command):
    password_output = subprocess.run(profile_info_command, capture_output=True, text=True).stdout

    if "Security key           : Absent" not in password_output:
        password_command = profile_info_command + ["key=clear"]
        password_output = subprocess.run(password_command, capture_output=True, text=True).stdout

        password_match = re.search("Key Content            : (.*)", password_output)
        if password_match:
            password = password_match.group(1).strip()

            # Encrypt the password
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            encrypted_password = encrypt(password, cipher_suite)
            return encrypted_password
        else:
            return None
    else:
        print(f"\n{Fore.YELLOW}Security key is absent for {profile_info_command[-1]}.{Style.RESET_ALL}")
        return None

# Encrypt and decrypt functions
def encrypt(text, cipher_suite):
    return cipher_suite.encrypt(text.encode())

def decrypt(ciphertext, cipher_suite):
    return cipher_suite.decrypt(ciphertext).decode()

# Use ThreadPoolExecutor for parallel execution
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Use executor.map to execute the function concurrently
    results = list(executor.map(get_password, [[netsh_path, "wlan", "show", "profile", name] for name in profile_names]))

# Create a dictionary for each WiFi profile and add it to the list
for i, name in enumerate(profile_names):
    wifi_profile = {"ssid": name, "password": decrypt(results[i], Fernet.generate_key()) if results[i] else None}
    wifi_list.append(wifi_profile)

# Display the final WiFi information using PrettyTable
table = PrettyTable(["SSID", "Password"])
for wifi_profile in wifi_list:
    table.add_row([wifi_profile["ssid"], wifi_profile["password"]])

print(f"\n{Fore.GREEN}WiFi Profiles:{Style.RESET_ALL}")
print(table)
