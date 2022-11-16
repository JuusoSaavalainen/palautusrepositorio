import requests
from datetime import datetime
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        
    def get_players(self):
        response = requests.get(self.url).json()
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
        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader.get_players()

    def top_scorers_by_nationality(self,nat):
        player_list = []
        print(f'Players from {nat}',datetime.now())
        self.reader.sort(key=lambda x: x.goals + x.assists, reverse=True)
        for player in self.reader:
            if player.nationality == nat:
                player_list.append(player)
        return player_list

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)
main()