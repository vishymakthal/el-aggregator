#!/usr/bin/evn python3
from flask import Flask, request
from flask_cors import CORS
from server import encoder
from server.controllers import player_controller, team_controller

app = Flask(__name__)
CORS(app)

# Player
@app.route("/api/v1/players/<player_id>")
def get_player(player_id):
    return player_controller.get_player_by_id(player_id)

@app.route("/api/v1/players/")
def get_players_by_query():
    if request.args['team']:
        return player_controller.get_players_by_team_name(request.args['team'])

@app.route("/api/v1/players/team/<team_ext>", methods=['GET'])
def get_players_by_team(team_ext):
    return player_controller.get_and_split_players_by_team_id(team_ext)

# Team
@app.route("/api/v1/teams/<team_id>")
def get_team(team_id):
    return team_controller.get_team_by_id(team_id)

@app.route("/api/v1/images/<id>", methods=['GET'])
def get_img(id):
    if request.args['q'] == 'player':
        return player_controller.get_player_img_by_id(id)
    if request.args['q'] == 'team':
        return team_controller.get_team_img_by_id(id)
    return 'no resource type provided', 401

# Bios
@app.route("/api/v1/bios/<subject_type>", methods=['GET'])
def get_player_bio(subject_type):

    if subject_type == 'player':
            return player_controller.get_player_bio_by_name(request.args['name'])

    return 'no resource type provided', 401

# Reddit highlights
@app.route("/api/v1/highlights/reddit", methods=['GET'])
def get_player_highlights():
    
    if request.args['query'] == '':
        return 'no query provided', 401
    
    return player_controller.get_highlights_from_reddit(request.args['query']), 200

@app.errorhandler(404)
def resource_not_found(error):
    return 'resource not found', 404 

@app.errorhandler(500)
def handle_500(error):
    return 'internal server error', 500

def main():
    app.run(port=8080)

if __name__ == '__main__':
    main()