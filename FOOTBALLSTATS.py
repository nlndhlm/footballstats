import downloaddata as dd
import getteams as gt
import collectstats as ct

download_url = 'http://www.football-data.co.uk/mmz4281/1617/E0.csv'
download_filename = 'premierleague.csv'
stats_filename = 'stats.csv'

dd.download_data(download_url, download_filename)

teams = gt.get_teams(download_filename)

ct.collect_stats(teams, download_filename, stats_filename)

# URLs for other English leagues (16/17)
# Championship: http://www.football-data.co.uk/mmz4281/1617/E1.csv
# League One: http://www.football-data.co.uk/mmz4281/1617/E2.csv
# League Two: http://www.football-data.co.uk/mmz4281/1617/E3.csv

#NOTE: Will cause wrong numbers/error if there is no 'Referee'-column in the downloaded data.
#This can be avoided by changing index of csv reader in collectstats.py


