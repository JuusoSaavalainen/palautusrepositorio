import unittest
from statistics import Statistics
from statistics import sort_by_goals, sort_by_assists, sort_by_points
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_sort_goals(self):
        player_ob = self.statistics.top(1,sort_by_goals)
        self.assertEqual(player_ob[0].name, 'Lemieux')  

    def test_sort_assist(self):
        player_ob = self.statistics.top(1,sort_by_assists)
        self.assertEqual(player_ob[0].name, 'Gretzky') 

    def test_sort_def(self):
        player_ob = self.statistics.top(0)
        self.assertEqual(len(player_ob),1)
        self.assertEqual(player_ob[0].name, 'Gretzky')
    
    def test_search_none(self):
        self.assertEqual(self.statistics.search("Noneisnamedlikethis"), None)
    
    def test_search_legit(self):
        self.assertEqual(self.statistics.search("Gretzky").name,"Gretzky")

    def test_team_default_return(self):
        players = self.statistics.team("EDM")
        for p in players:
            self.assertEqual(p.team,"EDM")