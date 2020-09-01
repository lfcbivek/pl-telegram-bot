from dotenv import load_dotenv

load_dotenv()
import os
import requests


def getFixtures(matchday):
    url = os.getenv("FIXTURES_URL")
    params = {
        'matchday': matchday
    }
    
    headers = {
        'X-Auth-Token': os.getenv("API_KEY")
    }
    
    result = requests.get(url=url, params = params,headers=headers)
    result = result.json()
    
    
    with open("fixtures.txt", "w") as f:
        f.write("Gameweek {} \n".format(matchday))
        for match in result["matches"]:
            homeTeam = str(match["homeTeam"]["name"])
            awayTeam = str(match["awayTeam"]["name"])
            
            homeTeamScore = str(match["score"]["fullTime"]["homeTeam"]) 
            
            awayTeamScore = str(match["score"]["fullTime"]["awayTeam"])
            if homeTeamScore != "None":
                
                f.write("{} \t {} - {} \t {} \n".format(homeTeam, homeTeamScore, awayTeamScore, awayTeam))
                
            else:
                f.write("{} \t vs \t {} \n".format(homeTeam, awayTeam))
                
    
    
    
# getFixtures(2)