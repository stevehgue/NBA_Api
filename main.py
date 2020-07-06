## WELCOME IN THE NBA TWITTER BOT##

import tweepy
import json
import http.client

def tweet(api, time, firstTeam, secondTeam):
    status = api.update_status(status= "at {}: {} - {}".format(time, firstTeam, secondTeam))

def remove(s):
    
    s = str(s).replace(":00+00:00", '')
    s = s.replace("T", "\n at ")
    s = s.replace("['", "")
    s = s.replace("']", "")
    return s

def main():
    conn = http.client.HTTPSConnection("api.sportradar.us")
    with open('info.json') as json_file:
        data = json.load(json_file)
        for p in data['my_info']:
            auth = tweepy.OAuthHandler(p['consumer_key'], p['consumer_secret'])
            auth.set_access_token(p['access_token'], p['access_token_secret'])
            nba_key = p['nba_api']

    api = tweepy.API(auth)

    #conn.request("GET", "/nba/trial/v7/en/games/2020/08/01/schedule.json?api_key={}".format(nba_key))
    #res = conn.getresponse()
    #data = res.read()
    #answer = json.loads(data.decode("utf-8"))
    with open("data.json") as data_file:
        match = json.load(data_file)
        for m in match["games"]:
            if (match["games"][0]["away"]["alias"]):
                away = []
                away.append(m["away"]["alias"])

            if (match["games"][0]["home"]["alias"]):
                home = []
                home.append(m["home"]["alias"])
            
            if (match["games"][0]["scheduled"]):
                schedule = []
                schedule.append(m["scheduled"])
                schedule = remove(schedule)
            print(away[0] + " @ " + home[0] + " on " + schedule)
            print("there is some changes on my program")
    #tweet(api,"1am PEST", "LAC", "LAL")


if __name__ == "__main__":
    main()