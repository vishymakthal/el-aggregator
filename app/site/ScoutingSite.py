from flask import *
from algoliasearch.search_client import SearchClient
import os 
import dotenv
import RedditInterface
import YouTubeInterface
import wikipedia

SINGLE = 1

app = Flask(__name__)
dotenv.load_dotenv(verbose=True)

client = SearchClient.create(os.getenv('ALGOLIA_APP_ID'), os.getenv('ALGOLIA_APP_KEY'))
team_index = client.init_index(os.getenv('ALGOLIA_TEAM_INDEX'))
player_index = client.init_index(os.getenv('ALGOLIA_PLAYER_INDEX'))

@app.route('/')
def home():
    return render_template('/html/index.html')

@app.route('/player/', methods=['GET'])
def PlayerReport():
    report = player_index.get_object(request.args['id'])
    player_name = report['long_name']
    search_name = report['short_name']
    club = report['club']
    highlights = RedditInterface.searchHighlightsByPlayer(search_name.split(' ')[-1],club)
    youtube_results = YouTubeInterface.searchYouTubeByPlayerName(search_name,club)
    try:
        report['bio'] = wikipedia.summary(player_name)
    except Exception:
        report['bio'] = "No wikipedia entry found."
    return render_template('/html/player.html',player_name=player_name, highlights=highlights,report=report,yt_results=youtube_results)


@app.route('/team/', methods=['GET'])
def SquadReport():
    team_id = request.args['id']
    team = team_index.get_object(team_id)
    team_name = ' '.join(team['name'].split()[:2])
    team_logo = team['img']
    res = player_index.search(team_name)
    squad = res['hits']
    return render_template('/html/squad.html',team=team_name,img=team_logo,squad=squad)

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('/html/500.html'), 500

@app.errorhandler(404)
def internal_server_error(e):
    return render_template('/html/404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
