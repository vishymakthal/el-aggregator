#!/usr/bin/evn python3
from flask import Flask, request
from flask_cors import CORS
from server import encoder
from server.controllers import player_controller, team_controller

app = Flask(__name__)
CORS(app)

@app.route("/api/v1/players/<player_id>")
def get_player(player_id):
    return player_controller.get_player_by_id(player_id)

@app.route("/api/v1/players/")
def get_players_by_query():
    if request.args['team']:
        return player_controller.get_players_by_team_name(request.args['team'])

@app.route("/api/v1/players/team/<team_id>")
def get_players_by_team(team_id):
    team_name = team_controller.get_team_by_id(team_id)['name']
    return player_controller.get_and_split_players_by_team_name(team_name)

@app.route("/api/v1/teams/<team_id>")
def get_team(team_id):
    return team_controller.get_team_by_id(team_id)

@app.route("/api/v1/images/<id>", methods=['GET'])
def get_img(id):
    if request.args['q'] == 'player':
        return player_controller.get_player_img_by_id(id)
    return 'no resource type provided', 401

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