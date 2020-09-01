from dotenv import load_dotenv

load_dotenv()
import os
import requests


def getStandings():
    url = os.environ["STANDINGS_URL"]
    headers = {
        "X-Auth-Token" : os.environ["API_KEY"]
    }
    
    result = requests.get(url = url, headers=headers)
    result = result.json()
    
    for standing in result["standings"]:
        if standing["type"] == 'TOTAL':
            with open("standings.txt", "w") as f:
                f.write("Position \t \t Teams \t \t Points \n")
                for position in standing["table"]:
                    
                        current_position = position["position"]
                        team = position["team"]["name"]
                        played = position["playedGames"]
                        won = position["won"]
                        draw = position["draw"]
                        loss = position["lost"]
                        points = position["points"]
                        
                        f.write("{} \t \t {} \t \t {} \n".format(current_position,team,points))
            
            
