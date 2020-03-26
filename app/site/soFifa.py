from bs4 import BeautifulSoup as bs
import re
import json
from unidecode import unidecode
import collections
import db

# teamIDs = collections.OrderedDict(json.load(open('app/TeamDictionary.json')))
SINGLE = 1

"""
Extract the Team ID from the JSON database.

:param str team: String of team name to search.
:rtype: str, list

"""
def extract_team_id(team):
    team_ID = teamIDs.get(team,None)
    if(team_ID is None):
        team_names = teamIDs.keys()
        team_name_matches = []
        for name in team_names:
            if(team.lower() in name.lower()):
                team_name_matches.append(name)
        return team_name_matches
    return team_ID


class soFifaProfile:

    searchLink = 'https://sofifa.com/players?keyword='
    profileLink = 'https://sofifa.com/player/'

    #                        CONSTRUCTOR HELPER METHODS
    #-------------------------------------------------------------------------------

    '''
    A method called by the constructor to retrieve the playerID for the player
    being searched up.

    Args:
    playerIDFromUser : An optinal string argument containing a player's ID. If
    a playerID is present, the retrieval process is skipped.

    Returns:
    String playerID
    '''
    def getPlayerID(self,playerIDFromUser):
        if(playerIDFromUser):
            self.profileLink += playerIDFromUser
            return playerIDFromUser


        request = urllib2.Request(self.searchLink + self.playerName, headers = {'User-Agent' : 'Mozilla/5.0'})
        page = urllib2.urlopen(request)
        html = bs(page.read(),'html5lib')
        searchResults = html.select('a[href*="/player/"]')

        if(len(searchResults) != 1):
            player_id = [(result.string, re.search(r'(?<=/)[0-9]+',result['href']).group()) for result in searchResults]
            return player_id
        playerID = re.search(r'(?<=/)[0-9]+',str(searchResults[0])).group()
        return [SINGLE, playerID]

    '''
    Creates a hashmap of player information.

    Args: none
    Returns: Dictionary
    '''
    def scrape_player_page(self):

        request = urllib2.Request(self.profileLink, headers = {'User-Agent' : 'Mozilla/5.0'})
        page = urllib2.urlopen(request)
        html = bs(page.read(),'html5lib')
        player_name = unicode(html.find('div',class_='meta').contents[0])
        known_as = html.find('div', class_='info').h1.string.split('(')[0]
        nation = html.find('div',class_='meta').a['title']
        age = int(re.search(r'(?<=Age )[0-9]+' , html.find('div',class_='meta').contents[-1].string).group())
        position = str(html.find('div',class_='meta').span.string)
        club = unicode(html.find_all('a',href= re.compile('/team/[0-9]+'))[0].contents[0])
        rating = int(html.find('div',class_='card-body stats').div.span.string)
        potential = int(html.find('div',class_='card-body stats').find_all('div')[1].span.string)
        self.json =  {
            'name' : player_name,
            'known_as' : known_as,
            'age' : age ,
            'nation' : nation ,
            'club' : club ,
            'position' : position ,
            'rating' : rating ,
            'potential' : potential
        }


    def __init__(self,playerID=None):
        self.profileLink += playerID
        self.scrape_player_page()


class soFifaSquad:
    teamLink = 'https://sofifa.com/team/'

    def __str__(self):
        '''

        toString method returns the teamID.

        '''
        return 'Team ID: ' + str(self.teamID)

    def __init__(self,team_id):
        self.teamID = team_id
        self.teamLink += str(self.teamID)

    def parsePlayerTable(self,response,player_rows,loan_rows=False):

        '''
        Parses the player table row by row and grabs the info for each player. Player
        data is saved in JSON format.

        Args:
        response : A Dictionary containing the generateReport response results in JSON formatself.
        player_rows: A list of html rows containing player data.
        loan_rows: A boolean value indicating whether or not the player_rows are from the loanee
        table. Defaults to false.

        Returns:
        none

        '''

        if(not player_rows):
            return  #If there are no loanees, then skip this function.

        for i in range(len(player_rows)):

            row = player_rows[i].find_all('td')
            infoCell = row[1].div.find_all('a')
            nation = re.search(r'(?<=title\=\")[A-Za-z ]+', str(infoCell[0])).group()
            name = str(unidecode(unicode(infoCell[1])))
            try:
                name = re.search(r'(?<=title\=\")[^\"]+', name).group()
            except Exception as e:
                print('Failed on ' + str(infoCell), str(e))
            position = str(infoCell[2].span.contents[0])
            age = str(row[2].div.contents[0]).replace('\n', '')
            rating = int(row[3].div.span.contents[0])
            potential = int(row[4].div.span.contents[0])
            growth = potential - rating
            if(not loan_rows):
                loaned = False
                loanedTo = None
            else:
                loaned = True
                loanedTo = row[5].a.contents[0]

            response["players"].append(
                {"Age": age, "Name": name, "Position": position, 'Nation': nation, "Rating": rating,
                 "Potential": potential, "Growth": growth, "Loaned": loaned, "LoanedTo": loanedTo})

    def get_player_ids(self):

        request = urllib2.Request(self.teamLink, headers={'User-Agent': 'Mozilla/5.0'})
        page = urllib2.urlopen(request)
        html = bs(page.read(), 'html5lib')

        mainSquadTable = html.find_all('table', class_="table table-hover persist-area")[0].tbody

        #Check to see if the team has a loanee table.
        try:
            loaneeTable = html.find_all('table', class_="table table-hover persist-area")[1].tbody
            loaneeRows = loaneeTable.find_all('tr')
        except:
            loaneeRows = False

        teamName = re.search(r'[A-Za-z0-9\. ]+',str(unidecode(html.find('div', class_="info").h1.contents[0]))).group().strip()
        mainRows = mainSquadTable.find_all('tr')

        if(loaneeRows):
            mainRows += loaneeRows


        ids = []

        for i in range(len(mainRows)):
            row = mainRows[i].find_all('td')
            infoCell = row[1].div.find_all('a')
            id = infoCell[1]
            ids.append(id['href'].split('/')[2])

        return ids




    def generateReport(self):

        '''
        Compiles the data of all of the players on a team's squad into a python
        Dictionary/JSON object.

        Args: none
        Returns: Dictionary response

        '''

        request = urllib2.Request(self.teamLink, headers={'User-Agent': 'Mozilla/5.0'})
        page = urllib2.urlopen(request)
        html = bs(page.read(), 'html5lib')

        mainSquadTable = html.find_all('table', class_="table table-hover persist-area")[0].tbody

        #Check to see if the team has a loanee table.
        try:
            loaneeTable = html.find_all('table', class_="table table-hover persist-area")[1].tbody
            loaneeRows = loaneeTable.find_all('tr')
        except:
            loaneeRows = False

        teamName = re.search(r'[A-Za-z0-9\. ]+',str(unidecode(html.find('div', class_="info").h1.contents[0]))).group().strip()
        mainRows = mainSquadTable.find_all('tr')

        response = {"teamName": teamName, "players": []}

        self.get_player_ids(mainRows)
        self.get_player_ids(loaneeRows,True)

        return response

def generate_squad_report(club):
    dbase = db.Database()

    return res

if __name__ == '__main__':
    dbase = db.Database()
    res = dbase.query_players_by_id('138412')

    # teams = []
    # with open('teams.txt','r') as t_file:
    #     t = t_file.readlines()
    #     for ln in t:
    #         teams.append(int(ln.split(' ')[0]))
    #
    # print teams
    #
    #
    # for t in teams[15:]:
    #     print 'On team {}'.format(t)
    #     s = soFifaSquad(t)
    #     ids = s.get_player_ids()
    #     print ids
    #     for id in ids:
    #         p = soFifaProfile(id)
    #         dbase.create(id, p.json)
