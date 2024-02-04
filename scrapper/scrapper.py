''' This script fetches a web page, extracts all the links from it, and checks the status of each link. '''
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from termcolor import colored

import requests

def fetch_page(url):
    ''' Fetches the content of a web page. '''
    try:
        response = requests.get(url, timeout=5)
        return response.text if response.status_code == 200 else None
    except requests.RequestException:
        return None

def extract_links(html, base_url):
    ''' Extracts all the links from a web page. '''
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a', href=True):
        yield urljoin(base_url, link['href'])

def check_link_status(url):
    ''' Checks the status of a link. '''
    try:
        response = requests.head(url, timeout=5)
        return response.status_code
    except requests.RequestException:
        return None

def main(site_url):
    ''' Main entry point of the script. '''
    html = fetch_page(site_url)
    if html:
        for link in extract_links(html, site_url):
            status = check_link_status(link)
            if status == 200:
                print(colored(f'{link} -> Status: {status}', 'green'))
            else:
                print(colored(f'{link} -> Status: {status}', 'red'))
    else:
        print(f'Failed to fetch the main page: {site_url}')

# Example usage
if __name__ == "__main__":
    main('https://boardgamegeek.com/browse/boardgame')
