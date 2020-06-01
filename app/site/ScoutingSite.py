from flask import *
from algoliasearch.search_client import SearchClient
import os 
import dotenv
import RedditInterface
import YouTubeInterface
import wikipedia
import requests

app = Flask(__name__)
dotenv.load_dotenv(verbose=True)

client = SearchClient.create(os.getenv('ALGOLIA_APP_ID'), os.getenv('ALGOLIA_APP_KEY'))
team_index = client.init_index(os.getenv('ALGOLIA_TEAM_INDEX'))
db = os.getenv('DATABASE_URL')

@app.route('/')
def home():
    return render_template('/html/index.html')

@app.route('/player/', methods=['GET'])
def PlayerReport():
    r = requests.get(db + '/api/v1/players/' + request.args['id'])
    if r.status_code != 200:
        return render_template('html/500.html'), 500
    player_img = db + '/api/v1/images/' + request.args['id'] + '?q=player'
    print(player_img)
    report = r.json() 
    player_name = report['long_name']
    search_name = report['short_name']
    club = report['club']
    highlights = RedditInterface.searchHighlightsByPlayer(search_name.split(' ')[-1],club)
    youtube_results = YouTubeInterface.searchYouTubeByPlayerName(search_name,club)
    try:
        report['bio'] = wikipedia.summary(player_name)
    except Exception:
        report['bio'] = "No wikipedia entry found."
    return render_template('/html/player.html',player_name=player_name, player_img=player_img, highlights=highlights,report=report,yt_results=youtube_results)


@app.route('/team/', methods=['GET'])
def SquadReport():
    team_id = request.args['id']
    team_name = request.args['name'] 
    r = requests.get(db + '/api/v1/players/?team=' + team_name)
    if r.status_code != 200:
        return render_template('html/500.html'), 500
    squad = r.json()
    return render_template('/html/squad.html',team=team_name,img=None,squad=squad)

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('/html/500.html'), 500

@app.errorhandler(404)
def internal_server_error(e):
    return render_template('/html/404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
