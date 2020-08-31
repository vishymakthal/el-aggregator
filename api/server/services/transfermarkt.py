import requests
from bs4 import BeautifulSoup as bs

class PageGetException(Exception):
    """Response from page was not 200"""

class TransfermarktPage(object):
    def __init__(self,url):
        self.url = url
        self._soup = self._get_page_soup()
    
    def _get_page_soup(self):
        markup = self._get_page_markup()
        return bs(markup,'lxml')

    def _get_page_markup(self):
        res = requests.get(self.url,headers={'User-Agent' : 'Mozilla/5.0'})
        if res.status_code != 200:
            raise PageGetException
        return res.text

class PlayerProfile(TransfermarktPage):

    def __init__(self, url):
        super().__init__(url)

    def get_comparable_players(self):
        """Return a list of comparable players from the player's profile.
        """
        cmp_table = self._soup.find('table', class_='table-profil-dreizeilig').tbody
        return [row.td.span.a.string for row in cmp_table if row != '\n']

    def get_url(self):
        return self.url

def has_img(tag):
    return tag.has_attr('title')    

def new_player_profile(player_name):
    url = 'https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query={}&x=0&y=0'.format(('+').join(player_name.lower().split(' ')))
    t = TransfermarktPage(url)
    a = t._soup.find_all('td', class_='hauptlink')
    return PlayerProfile('https://www.transfermarkt.us{}'.format(a[0].a['href']))


if __name__ == '__main__':
    
    # p = PlayerProfile('https://www.transfermarkt.us/jamal-lewis/profil/spieler/346018')
    # print(p.get_comparable_players())

    p = new_player_profile('Leon Goretzka')
    print(p.get_comparable_players())
    print(p.get_url())