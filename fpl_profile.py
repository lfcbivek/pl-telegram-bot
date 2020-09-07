
import requests

def FPLProfile(id):
    
    teams = {
        '1': 'Arsenal',
        '2': 'Aston Villa',
        '3': 'Brighton and Hove Albion',
        '4':'Burnley',
        '5':'Chelsea',
        '6': 'Crystal Palace',
        '7':'Everton',
        '8': 'Fulham',
        '9':'Leeds United',
        '10':'Leicester City',
        '11':'Liverpool',
        '12':'Manchester City',
        '13':'Manchester United',
        '14':'Newcastle United',
        '15':'Sheffield United',
        '16':'Southampton',
        '17':'Tottenham Hotspur',
        '18':'West Bromwich Albion',
        '19':'West Ham United',
        '20':'Wolverhampton Wanderers',
            
    }
    url = "https://fantasy.premierleague.com/api/entry/{}/".format(str(id))
    data = requests.get(url)
    data = data.json()
    favourite_team_id = data['favourite_team']
    favourite_team = teams['{}'.format(str(favourite_team_id))]
    first_name = data['player_first_name']
    last_name = data['player_last_name']
    region_name = data['player_region_name']
    overall_points = data['summary_overall_points']
    overall_rank = data['summary_overall_rank']
    
    with open("fpl_profile.txt","w") as f:
        f.write("Name: \t {} {} \n".format(first_name,last_name))
        f.write("Region: \t {}  \n".format(region_name))
        f.write("Favourite Team: \t {}  \n".format(favourite_team))
        f.write("Overall Points: \t {}  \n".format(overall_points))
        f.write("Overall Points: \t {}  \n".format(overall_rank))
        
        leagues = data['leagues']
        classic_leagues = []
        h2h_leagues = []
        f.write("\n \n")
        f.write("Classic Leagues \n")
        for league in leagues['classic']:
            league_name = league['name']
            last_rank = league['entry_last_rank']
            current_rank = league['entry_rank'] 
            
            classic_league = {
                'League': league_name,
                'Last Rank': last_rank,
                'Current Rank': current_rank
            }
            classic_leagues.append(classic_league)
            f.write("League: {}  \t".format(league_name))
            f.write("Last Rank: {}  \t".format(last_rank))
            f.write("Current Rank: {}  \n".format(current_rank))
        
        f.write("\n \n")
        f.write("H2H Leagues \n")
        for league in leagues['h2h']:
            league_name = league['name']
            last_rank = league['entry_last_rank']
            current_rank = league['entry_rank'] 
            
            h2h_league = {
                'League': league_name,
                'Last Rank': last_rank,
                'Current Rank': current_rank
            }
            
            h2h_leagues.append(h2h_league)
            
            f.write("League: {}  \t".format(league_name))
            f.write("Last Rank {}  \t".format(last_rank))
            f.write("Current Rank: {}  \n".format(current_rank))
    
