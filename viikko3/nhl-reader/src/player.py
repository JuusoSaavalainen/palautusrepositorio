class Player:
    def __init__(self, name, team, goals, assists, nationality, games, penalties):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
        self.penalties = penalties
        self.games = games

    def __str__(self):
        
        return (f"{self.name:21} {self.team:^3} {self.goals:^3}+ {self.assists:^3}={self.goals+self.assists:>3}")
