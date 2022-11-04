from player_reader import PlayerReader


def sort_by_points(playa):
    return playa.points

def sort_by_assists(playa):
    return playa.assists

def sort_by_goals(playa):
    return playa.goals


class Statistics:
    def __init__(self, playa: PlayerReader):
        reader = playa

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sorting_style=sort_by_points):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sorting_style
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
