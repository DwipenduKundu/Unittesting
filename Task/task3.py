import csv
import matplotlib.pyplot as plt
from collections import defaultdict


SEASON = 'season'
ID = 'id'
BOWLING_TEAM = 'bowling_team'
EXTRA_RUNS = 'extra_runs'


def start3(deliveryfile_path, matchfile_path):
    # here I am taking the match csv file
    with open(matchfile_path, mode='r') as match_file:
        match_reader = csv.DictReader(match_file)
        id_list = []  # taking empty list for taking input of all ids of 2016

       # checking for the 2016 season and appended those id's to the list
        for row in match_reader:
            if row[SEASON] == '2016':
                id_list.append(row[ID])

        # here removing the duplicates from the list
        id_list = list(set(id_list))

    # here taking the deliveries csv file
    with open(deliveryfile_path, mode='r') as ipl_file:
        ipl_reader = csv.DictReader(ipl_file)
        ipl_list = list(ipl_reader)  # convert that into list
        ipl_dict = {}  # taking empty dictionary for the bowling team and there extra runs

        # checking rows for the bowling team and there extra runs
        for row in ipl_list:
            if row['match_id'] in id_list:
                if row[BOWLING_TEAM] not in ipl_dict:
                    ipl_dict[row[BOWLING_TEAM]] = int(row[EXTRA_RUNS])
                else:
                    ipl_dict[row[BOWLING_TEAM]] += int(row[EXTRA_RUNS])
        # the list of keys and values are stored into variable and call the graph function to plot the graph
        team = ipl_dict.keys()
        run = ipl_dict.values()
        return team, run


def graph3(team, run):

    # taking the axises
    team_name = team
    extra_runs = run

    # Plotting
    plt.bar(team_name, extra_runs, color='darkblue')

    # giving the title and axis names
    plt.title('Extra runs conceded per team in the year 2016')
    plt.xlabel('Team Names')
    plt.ylabel('Extra Runs conceded')

    # For better view I rotate the X-axis names.
    plt.xticks(rotation=45, ha='right')

    # For better view of that graph I used that.
    plt.tight_layout()
    plt.show()


def execute3():
    matchfile_path = './data/test_matches.csv'
    deliveryfile_path = './data/test_deliveries_lessdata.csv'
    team, run = start3(deliveryfile_path, matchfile_path)
    graph3(team, run)


if __name__ == "__main__":
    execute3()