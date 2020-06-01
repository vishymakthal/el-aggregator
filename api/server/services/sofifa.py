import requests
from bs4 import BeautifulSoup as bs


def get_full_squad_list(team_id):
    resp = requests.get('https://sofifa.com/team/{}'.format(team_id), headers={'User-Agent' : 'Mozilla/5.0'})
    if resp.status_code != 200:
        print("ERROR: non 200 status code")

    soup = bs(resp.text, 'lxml')
    table = soup.find_all('tr', class_='starting') + soup.find_all('tr', class_='sub')

    players = []
    for row in table:
        cells = row.find_all('td')
        pl = {}
        pl['short_name'] = cells[1].a.div.get_text().lstrip()
        pl['position'] = cells[1].a.next_sibling.span.get_text()
        pl['age'] = cells[2].get_text()
        pl['overall'] = cells[3].span.get_text()
        players.append(pl)

    return players