import validators
import requests
import requests.exceptions
import urllib.parse
from collections import deque
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from bs4 import BeautifulSoup
import re
import random
import logging

user_url = input('[+] Enter Target URL To Scan: ')
if not validators.url(user_url):
    print("[-] Invalid URL. Please provide a valid URL.")
    exit()

urls = deque([user_url])

scraped_urls = set()
emails = set()

count = 0

# Set up logging configuration
logging.basicConfig(filename='scraping_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    # Add more user-agents
]

max_depth = 3

def process_url(url):
    scraped_urls.add(url)

    parts = urllib.parse.urlsplit(url)
    base_url = '{0.scheme}://{0.netloc}'.format(parts)

    path = url[:url.rfind('/')+1] if '/' in parts.path else url

    print('[%d] Processing %s' % (count, url))

    try:
        headers = {'User-Agent': random.choice(user_agents)}
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'[-] Error processing {url}: {e}')
        return

    new_emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text, re.I))
    emails.update(new_emails)

    soup = BeautifulSoup(response.text, features="html.parser")

    depth = scraped_urls.count(base_url)
    if depth < max_depth:
        for anchor in soup.find_all("a"):
            link = anchor.get('href', '')
            if link and not link.startswith(('http', 'https', 'javascript')):
                link = urllib.parse.urljoin(base_url, link)
                if link not in urls and link not in scraped_urls:
                    urls.append(link)
                    executor.submit(process_url, link)

try:
    with ThreadPoolExecutor(max_workers=10) as executor:
        while len(urls):
            count += 1
            if count == 100:
                break
            url = urls.popleft()
            executor.submit(process_url, url)

except KeyboardInterrupt:
    print('[-] Scanning interrupted by user!')
except concurrent.futures._base.CancelledError:
    pass  # Ignore ThreadPoolExecutor cancellation error

# Display results
print(f'\n[+] Scanning completed. {count} URLs processed. {len(emails)} emails found.')

for mail in emails:
    print(mail)
