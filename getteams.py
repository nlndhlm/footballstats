import csv

def get_teams(ifile):

    teams = []

    with open(ifile) as data:
        read_data = csv.reader(data, delimiter=',')

        next(read_data, None) #skips first line in csv (headings)

        for line in read_data:
            teams.append(line[2])
            teams.append(line[3])

    
    teams = list(set(teams))
    teams.sort()

    return teams
