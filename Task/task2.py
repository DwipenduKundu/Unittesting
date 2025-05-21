import csv
from collections import defaultdict
import matplotlib.pyplot as plt


SEASON = 'season'
WINNER = 'winner'


def start2(file_path):
    match_dict = defaultdict(lambda: defaultdict(int))

    # import files as Match
    with open(file_path, mode='r') as match_file:
        match_reader = csv.DictReader(match_file)  # convert it into dictionary

        # create the dictionary as this format: {year:{winner:count}} here
        for row in match_reader:
            year = row[SEASON]
            winner = row[WINNER]
            match_dict[year][winner] += 1
    return match_dict


def graph2(dictionary):
    # got all the years list
    all_years = sorted(dictionary.keys())
    # got all team names also
    all_teams = sorted({team for year_data in dictionary.values()
                       for team in year_data})

    # create team and there count of wins as per there year like {team:[counts....]}
    matches_by_team = {team: [] for team in all_teams}
    for year in all_years:
        year_data = dictionary[year]
        for team in all_teams:
            matches_by_team[team].append(year_data.get(team, 0))

    # plotting
    x_pos = list(range(len(all_years)))
    bottom = [0] * len(all_years)
    plt.figure(figsize=(12, 6))
    for team in all_teams:
        team_values = matches_by_team[team]
        plt.bar(x_pos, team_values, bottom=bottom, label=team)
        bottom = [bottom[i] + team_values[i] for i in range(len(all_years))]

    plt.xticks(x_pos, all_years, rotation=0)
    plt.xlabel("Year")
    plt.ylabel("Number of Matches Played")
    plt.title("Teams won per Year")
    plt.legend(title="Teams", bbox_to_anchor=(1, 1), loc='upper left')
    plt.tight_layout()
    plt.show()


def execute2():
    file_path = './data/test_matches.csv'
    match_dict = start2(file_path)
    graph2(match_dict)


if __name__ == "__main__":
    execute2()