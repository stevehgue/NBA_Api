## WELCOME IN THE NBA TWITTER BOT##

import tweepy
import json
import http.client
import os

"""
    Will post a tweet on Twitter
"""
def tweet(api, time, firstTeam, secondTeam):
    status = api.update_status(status= "at {}: {} - {}".format(time, firstTeam, secondTeam))

"""
    Will authenticate to the Twitter API and NBA API
"""
def auth():
    conn = http.client.HTTPSConnection("api.sportradar.us")
    with open('info.json') as json_file:
        data = json.load(json_file)
        for p in data['my_info']:
            auth = tweepy.OAuthHandler(p['consumer_key'], p['consumer_secret'])
            auth.set_access_token(p['access_token'], p['access_token_secret'])
            nba_key = p['nba_api']
    api = tweepy.API(auth)

    refresh_data()
    conn.request("GET", "/nba/trial/v7/en/games/2021/02/06/schedule.json?api_key={}".format(nba_key))
    res = conn.getresponse()
    data = res.read()
    answer = json.loads(data.decode("utf-8"))
    with open ("data.json", "w") as games_file:
        games_file.write(json.dumps(answer))

"""
    Will refresh data.json about games
"""
def refresh_data():
    if os.path.exists("data.json"):
        os.remove("data.json")

def remove(s):
    
    s = str(s).replace(":00+00:00Z", '')
    s = s.replace("T", "\n at ")
    s = s.replace("['", "")
    s = s.replace("']", "")
    return s

def main():
    
    auth()
    """
        checker dans le fichier su un match est joué dans 1h
    """
    with open("data.json") as games_file:
        match = json.load(games_file)
        for game in match["games"]:
            if (match["games"][0]["away"]["alias"]):
                away = []
                away.append(game["away"]["alias"])

            if (match["games"][0]["home"]["alias"]):
                home = []
                home.append(game["home"]["alias"])
            
            if (match["games"][0]["scheduled"]):
                schedule = []
                """
                    A faire:
                    une boucle qui va checker ma liste schedule pour voir
                    si un match sera dans moins d'une heure et le poster
                    si oui
                """
                schedule.append(game["scheduled"])
                schedule = remove(schedule)
            print(away[0] + " @ " + home[0] + "\n on " + schedule)
    #tweet(api,"1am PEST", "LAC", "LAL")

if __name__ == "__main__":
    main()