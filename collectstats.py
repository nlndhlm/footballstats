import csv

def collect_stats(teams, data_csv, stats_csv):

    ofile = open(stats_csv, 'w')

    home_games = 0
    home_goals = 0
    home_shots = 0
    home_goals_against = 0
    home_shots_against = 0

    away_games = 0
    away_goals = 0
    away_shots = 0
    away_goals_against = 0
    away_shots_against = 0

    ofile.write('Team, H shot/game, H goal/shot, H shot/game against, H goal/shot against, A shot/game, A goal/shot, A shot/game against, A goal/shot against')
    ofile.write('\n')

    for team in teams:
        with open(data_csv) as data:
            read_data = csv.reader(data, delimiter=',')


            next(read_data, None)

            for line in read_data:

                if line[2]==team:
                    home_games += 1
                    home_goals += int(line[4])
                    home_shots += int(line[11])
                    home_goals_against += int(line[5])
                    home_shots_against += int(line[12])
                    #add more home data here

                if line[3]==team:
                    away_games += 1
                    away_goals += int(line[5])
                    away_shots += int(line[12])
                    away_goals_against += int(line[4])
                    away_shots_against += int(line[11])
                    #add more away data here'''
                    
            ofile.write(team)
            ofile.write(',')
            ofile.write(str(round(home_shots / home_games, 4)))
            ofile.write(',')
            ofile.write(str(round(home_goals / home_shots, 4)))
            ofile.write(',')
            ofile.write(str(round(home_shots_against / home_games, 4)))
            ofile.write(',')
            ofile.write(str(round(home_goals_against / home_shots_against, 4)))
            ofile.write(',')

            ofile.write(str(round(away_shots / away_games, 4)))
            ofile.write(',')
            ofile.write(str(round(away_goals / away_shots, 4)))
            ofile.write(',')
            ofile.write(str(round(away_shots_against / away_games, 4)))
            ofile.write(',')
            ofile.write(str(round(away_goals_against / away_shots_against, 4)))          
            ofile.write('\n')

            home_games = 0
            home_goals = 0
            home_shots = 0
            home_goals_against = 0
            home_shots_against = 0

            away_games = 0
            away_goals = 0
            away_shots = 0
            away_goals_against = 0
            away_shots_against = 0
            
    ofile.close()
    print('Stats collected.')
