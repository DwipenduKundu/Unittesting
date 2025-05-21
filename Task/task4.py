import csv
import matplotlib.pyplot as plt


SEASON = 'season'
ID = 'id'
BOWLER = 'bowler'
TOTAL_RUNS = 'total_runs'
NOBALL_RUNS = 'noball_runs'


def start4(deliveryfile_path, matchfile_path):
    # here I am taking the match csv file
    with open(matchfile_path, mode='r') as match_file:

        # taking the data into dictionary format
        match_reader = csv.DictReader(match_file)
        # convert that into list for better access
        match_list = list(match_reader)
        id_list = []  # taking empty list for taking input of all ids of 2015

       # checking for the 2015 season and appended those id's to the list
        for row in match_list:
            if row[SEASON] == '2015':
                id_list.append(row[ID])

    # here taking the deliveries csv file
    with open(deliveryfile_path, mode='r') as ipl_file:
        # taking the data into dictionary format
        ipl_reader = csv.DictReader(ipl_file)
        ipl_list = list(ipl_reader)  # convert that into list

        # taking the run dictionary and balls dictionary
        ipl_runs = {}
        ipl_ball = {}

        # checking rows for the bowling team and there extra runs
        for row in ipl_list:
            # checking for the match id is present in the list or not i.e 2015 season we are taking
            if row['match_id'] in id_list:
                bowler = row[BOWLER]
                runs = int(row[TOTAL_RUNS])

                # If the balls are wide or no balls then we are not counting those as balls
                if row['wide_runs'] == '0' and row[NOBALL_RUNS] == '0':

                    # here adding the balls count per bowler in dictionary format
                    if row['bowler'] not in ipl_ball:
                        ipl_ball[bowler] = 1
                    else:
                        ipl_ball[bowler] += 1

                # here adding the runs count per bowler in dictionary format
                if row['bowler'] not in ipl_runs:
                    ipl_runs[bowler] = runs
                else:
                    ipl_runs[bowler] += runs

        # make one  economic rate dictionary
        economy_rate = {}

        # here calculating the economy rate per bowler and add that to economy_rate dictionary
        for bowler in ipl_runs:
            # rate=runs/over
            # i multiplied that 6 with that beacause we take the ball count but we need the over count of per bowler
            economy_rate[bowler] = 6*(ipl_runs[bowler]/ipl_ball[bowler])

        # simply sorted the 10 eliments
        top_10_economy = sorted(economy_rate.items(), key=lambda x: x[1])[:10:]
        top_names = []
        top_economy = []

        # take top names and rate for bar plotting
        for i in top_10_economy:
            top_names.append(i[0])
            top_economy.append(i[1])
    return top_names, top_economy


def graph4(names, economy):

    # taking the axises
    bowler = names
    economy = economy

    # Plotting
    plt.bar(bowler, economy, color='lightgreen')

    # giving the title and axis names
    plt.title('Top 10 Economical Bowlers in 2015')
    plt.xlabel('Bowlers')
    plt.ylabel('Economy Rate')

    # For better view I rotate the X-axis names.
    plt.xticks(rotation=30)

    # For better view of that graph I used that.
    plt.tight_layout()
    plt.show()


def execute4():
    matchfile_path = './data/test_matches.csv'
    deliveryfile_path = './data/test_deliveries_lessdata.csv'
    top_names, top_economy = start4(deliveryfile_path, matchfile_path)
    graph4(top_names, top_economy)


if __name__ == "__main__":
    execute4()
