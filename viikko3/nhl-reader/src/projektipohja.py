import requests
from datetime import datetime
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists'],
            player_dict['nationality'],
            player_dict['penalties'],
            player_dict['games']
        )

        players.append(player)


#standart str kutsun palautus 
    print("Oliot:")
    for player in players:
        print(player)

#pelaajat suomalaisittain
    players.sort(key=lambda x: x.goals + x.assists, reverse=True)
    print('Players from FIN',datetime.now())
    for player in players:
        if player.nationality == "FIN":
            print(player)
main()
