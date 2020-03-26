# El Aggregator - The Simple Soccer Scouting Tool 🔍 ⚽

tl;dr - "I wonder how good this player I used in FIFA Career Mode is in real life?"

### About

I love soccer, I love using Python, and I'm learning about microservices. This project was a great way to combine all of these worlds, and opened the doors to create something that people can actually use.

Following soccer is fun, but following a league or team is not enough. Akin to the heightened sense of being that frequenting microbreweries and coffee roasteries brings to oneself, so does spotting budding talent in professional soccer. Who will be the next wonderkid? How high is their ceiling? Who is the guy on Norwich City who looks like Justin Bieber and is he always this good? These are the questions El Aggregator attempts to answer.

### How it works

El Aggregator is a containerized Flask app that is deployed on Heroku. Simply search by player name or team name. Team data and player ratings are collected from SoFifa and stored in an Algolia database, and player highlights are obtained via the Reddit API, as well as the YouTube API.


### Features

* Search by team or by player
* Aggregates FIFA ratings and highlights for every player
* Isolate the young studs on each professional team with the intuitive UI.
