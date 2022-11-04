from statistics import Statistics
from player_reader import PlayerReader
from statistics import sort_by_points, sort_by_assists, sort_by_goals
def main():
    stats = Statistics(
      PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt")
    )

    # järjestetään kaikkien tehopisteiden eli maalit+syötöt perusteella
    print("Top point getters:")
    for player in stats.top(10, sort_by_points):
        print(player)

    # metodi toimii samalla tavalla kuin yo. kutsu myös ilman toista parametria
    for player in stats.top(10):
        print(player)

    # järjestetään maalien perusteella
    print("Top point goal scorers:")
    for player in stats.top(10, sort_by_goals):
        print(player)

    # järjestetään syöttöjen perusteella
    print("Top by assists:")
    for player in stats.top(10, sort_by_assists):
        print(player)

if __name__ == "__main__":
    main()