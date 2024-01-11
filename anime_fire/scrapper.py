from bs4 import BeautifulSoup
from .requisition import get_scraping_page
import re

class AnimeFire:
    def __init__(self):
        self.DOMAIN_URL = 'https://animefire.plus/'
        self.MAIN_PAGE = get_scraping_page(self.DOMAIN_URL)

    def get_animes(self):
        pass
    
    def search_anime(self, anime_name:str):
        def _format_query_args(anime_name:str):
            return anime_name.replace(' ', '-').lower()
        
        def _format_query_url(query_args:str):
            return f'{self.DOMAIN_URL}pesquisar/{query_args}'
        
        def _get_div_container(search_page:BeautifulSoup):
            return search_page.find('div', attrs={'class':'card-group'})

        def _get_anime_list(div_container:BeautifulSoup):
            anime_divs = div_container.find_all('div', attrs={'title':r'.+?Todos os Episódios'})

            for div in anime_divs:
                image = div.find('div', {'alt': re.compile(r'Todos os Episódios$')})['src']
                title = div.find('h3', attrs={'class':'animeTitle'}).text
                print(title)
                print(image)

        query_args = _format_query_args(anime_name)
        query_url = _format_query_url(query_args)
        search_page = get_scraping_page(query_url)
        div_container = _get_div_container(search_page)
        _get_anime_list(div_container)

    def search_movies(self):
        animes = self.soup.find_all('div', class_='anime-card')
        return [Anime(anime) for anime in animes]

    def list_genders(self):
        animes = self.soup.find_all('div', class_='anime-card')
        return [Anime(anime) for anime in animes]

    def list_seasons(self):
        animes = self.soup.find_all('div', class_='anime-card')
        return [Anime(anime) for anime in animes]

    def get_list_anime_categories(self):
        animes = self.soup.find_all('div', class_='anime-card')
        return [Anime(anime) for anime in animes]