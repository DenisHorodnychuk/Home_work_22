from requests import get
from bs4 import BeautifulSoup as bs
import time

block_selector = '.quote'
quotas_find = 'span'
author_find = 'small'
url = 'https://quotes.toscrape.com/'
n = 1

def get_page_content(url):
    response = get(url)
    if response.ok:
        return response.content
    return None

def save_page_content(content, filename):
    with open(filename, 'wb') as file:
        file.write(content)
def parse_and_save_quotes(page_content, n):
    soup = bs(page_content, 'html.parser')
    quotas_blocks = soup.select(block_selector)
    
    if not quotas_blocks:
        return False
    
    for quote in quotas_blocks:
        author = quote.find(author_find).text
        quotas_text = quote.find(quotas_find).text
        with open(f'data/{author}.txt', 'w', encoding='utf-8') as file:
            file.write(quotas_text)
    
    return True

while True:
    page_url = f"{url}page/{n}/"
    page_content = get_page_content(page_url)
    
    if not page_content:
        break
    
    save_page_content(page_content, f'pages/page{n}.html')
    
    if not parse_and_save_quotes(page_content, n):
        break
    
    n += 1
    time.sleep(3 * 10 ** -3)


