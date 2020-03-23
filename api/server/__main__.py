#!/usr/bin/evn python3
# import connexion
from flask import Flask
from server import encoder
from server.controllers import player_controller, team_controller
# app = connexion.App(__name__, specification_dir='./swagger/')
# app.app.json_encoder = encoder.JSONEncoder
# app.add_api('api.yaml', arguments={'title': 'El Aggregator API'})

app = Flask(__name__)

@app.route("/api/v1/player/<player_id>")
def get_player(player_id):
    return player_controller.get_player_by_id(player_id)

@app.route("/api/v1/team/<team_id>")
def get_team(team_id):
    return team_controller.get_team_by_id(team_id)

def main():
    app.run(port=8080)

if __name__ == '__main__':
    main()