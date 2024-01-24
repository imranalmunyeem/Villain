import socket
import re
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

ip_address_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile(r"([0-9]+)-([0-9]+)")

def validate_ip_address():
    while True:
        ip_address = input("\nPlease enter the IP address or hostname to scan: ")
        if ip_address_pattern.match(ip_address):
            print(f"{ip_address} is a valid IP address.")
            return ip_address
        else:
            print("Invalid IP address. Please try again.")

def validate_port_range():
    while True:
        port_range = input("Please enter the port range to scan (e.g., 60-120): ").replace(" ", "")
        match = port_range_pattern.match(port_range)
        if match:
            port_min, port_max = int(match.group(1)), int(match.group(2))
            if 1 <= port_min <= port_max <= 65535:
                return port_min, port_max
            else:
                print("Invalid port range. Please ensure the ports are within valid boundaries.")
        else:
            print("Invalid port range. Please try again.")

async def resolve_hostname(hostname):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://aiodnsapi.com/lookup?hostname={hostname}") as response:
                data = await response.json()
                return data[0]['ip']
    except Exception as e:
        print(f"Error resolving hostname {hostname}: {e}")
        return None

async def scan_port(ip_address, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, s.connect, (ip_address, port))
            return port
    except (socket.timeout, ConnectionRefusedError):
        return None
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return None

async def grab_banner(ip_address, port, timeout):
    try:
        loop = asyncio.get_event_loop()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = await loop.run_in_executor(None, s.connect, (ip_address, port))
            if result is not None:
                banner = await loop.run_in_executor(None, s.recv, 1024)
                return banner.decode('utf-8').strip()
            else:
                return None
    except (socket.timeout, ConnectionRefusedError):
        return None
    except Exception as e:
        print(f"Error grabbing banner from port {port}: {e}")
        return None

async def scan_ports_with_banner(ip_address, ports, timeout):
    open_ports = []
    banners = {}
    tasks = [scan_port(ip_address, port, timeout) for port in ports]
    results = await asyncio.gather(*tasks)

    for port, result in zip(ports, results):
        if result is not None:
            open_ports.append(port)
            banner = await grab_banner(ip_address, port, timeout)
            banners[port] = banner

    return open_ports, banners

def print_colored(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

async def main():
    ip_address = validate_ip_address()
    port_min, port_max = validate_port_range()
    timeout = 0.5
    concurrency_level = 100

    if ip_address_pattern.match(ip_address):
        # If input is an IP address, use it directly
        ip_to_scan = ip_address
    else:
        # If input is a hostname, resolve it to an IP address
        ip_to_scan = await resolve_hostname(ip_address)
        if not ip_to_scan:
            print("Hostname resolution failed. Exiting.")
            return

    ports_to_scan = list(range(port_min, port_max + 1))
    chunks = [ports_to_scan[i:i + concurrency_level] for i in range(0, len(ports_to_scan), concurrency_level)]

    open_ports = []
    banners = {}
    for chunk in chunks:
        chunk_open_ports, chunk_banners = await scan_ports_with_banner(ip_to_scan, chunk, timeout)
        open_ports.extend(chunk_open_ports)
        banners.update(chunk_banners)

    if not open_ports:
        print_colored("No open ports found.", Fore.GREEN)
    else:
        for open_port in open_ports:
            banner = banners.get(open_port, "No banner available")
            print_colored(f"Port {open_port} is open on {ip_to_scan}. Banner: {banner}", Fore.RED)

if __name__ == "__main__":
    asyncio.run(main())
