import downloaddata as dd
import getteams as gt
import collectstats as ct

download_url = 'http://www.football-data.co.uk/mmz4281/1617/E0.csv'
download_filename = 'premierleague.csv'
stats_filename = 'stats.csv'

dd.download_data(download_url, download_filename)

teams = gt.get_teams(download_filename)

ct.collect_stats(teams, download_filename, stats_filename)

