import requests
from bs4 import BeautifulSoup
from random import choice
from requests_html import HTMLSession

def _get_source_html(url):
    user_agents = requests.get('https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt').text
   
    lines = [linha.strip() for linha in user_agents.split('\n')[:1000]]
    user_agent = choice(lines)
    
    headers = requests.utils.default_headers()
    
    headers.update(
        {
            'User-Agent' : user_agent
        }
    )
    
    # session = HTMLSession()
    
    # response = session.get(url, headers=headers)

    # response.raise_for_status()

    # response.html.render()

    # html_source = response.html.html

    # return html_source

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f'requests failed: {response.status_code}')




def get_scraping_page(url):
    source_html = _get_source_html(url)
    return BeautifulSoup(source_html, 'html.parser')