# El Aggregator - The Simple Soccer Scouting Tool 🔍 ⚽

tl;dr - "I wonder how good this player I used in FIFA Career Mode is in real life?"

### About

Being a soccer fan is fun, but sometimes following a league or team isn't enough. Akin to the heightened sense of being that frequenting microbreweries and/or operating a French press brings oneself, there's nothing like telling your friends about budding talent before an Italian club signs them on a loan-to-buy deal. 

Who will be the next wonderkid? How high is their ceiling? How long has [Harry Styles](http://www.el-aggregator.com/player/225748) played for Norwich City and was he always this good? These are the questions El Aggregator attempts to answer.

### How it works

El Aggregator is a containerized React app deployed on Heroku. Simply search by player name or team name, powered by [Algolia](algolia.com). Team data and player ratings are collected from SoFifa and stored in Google Firebase, and player highlights are obtained via the Reddit and YouTube APIs.


### Features

* Search by team or by player
* Aggregates FIFA ratings and highlights for every player
* Isolate the young studs on each professional team with the intuitive UI.
