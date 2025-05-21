import csv
import matplotlib.pyplot as plt


SEASON = 'season'


def start1(file_path):
    # here I take the csv file as f file name
    with open(file_path, mode='r') as file:

        # i read the file and take it as a dictionary
        reader = csv.DictReader(file)

        # convert that dictionary into list here
        matches_list = list(reader)

        # taking the empty dictionary for the year and there count
        sesson_disc = {}

        # here i count the matches played per year
        for row in matches_list:
            if row['season'] not in sesson_disc:
                sesson_disc[row[SEASON]] = 1
            else:
                sesson_disc[row[SEASON]] += 1

        # here i do the sort of year so it will be proper to see in graph
        sorted_sesson = []  # make one empty list
        for years, numbers in sesson_disc.items():
            # appending the keys and values of the sesson_disc i.e year and numbers
            sorted_sesson.append([years, numbers])
        # sorted according to the year
        sorted_sesson = dict(sorted(sorted_sesson, key=lambda x: x[0]))

        # get year and the number of matches played per year
        year = list(sorted_sesson.keys())
        number = list(sorted_sesson.values())
        return year, number


def graph1(year, number):

    # taking the axises
    year = year
    number_of_matches = number

    # Plotting
    plt.bar(year, number_of_matches, color='cyan')

    # giving the title and axis names
    plt.title('Number of matches played per year')
    plt.xlabel('Year')
    plt.ylabel('Number of matches')

    # For better view I rotate the X-axis names.
    plt.xticks(rotation=30)

    # For better view of that graph I used that.
    plt.tight_layout()
    plt.show()


def execute1():
    file_path = './data/test_matches.csv'
    year, number = start1(file_path)
    graph1(year, number)


if __name__ == "__main__":
    execute1()
