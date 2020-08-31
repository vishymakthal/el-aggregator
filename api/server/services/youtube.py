import requests


class YouTube():

    def __init__(self, key):
        self.key = key
    
    def search_youtube_by_player_name(self, player_name,club):
        '''
        Executes a YouTube query of the passed in player name plus "highlights", pulling a
        maximum of 10 search results, which are organized into key-value pairs, using
        the videoId as the key.
        Args: String player_name
        Returns: List search_results
        '''

        url = "https://www.googleapis.com/youtube/v3/search?q=" + '{}%20{}'.format(player_name.replace(' ',"%20"),club.replace(' ',"%20")) + "%20highlights&maxResults=5&part=snippet&key=" + self.key 
        print(url) 
        search = requests.get(url,headers={'Accept' : 'application/json'})
        search_results = []

        if search.status_code == 200:  #Request is OK
            for result in search.json()['items']:
                search_results.append({ 'video_id' : result['id']['videoId'] , 'video_title' : result['snippet']['title'] , 'img' : result['snippet']['thumbnails']['medium']['url']})
        else:
            print(search.status_code,'\n',search.text)
        return search_results