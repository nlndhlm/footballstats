# footballstats

for python3

<b>Dependencies:</b> csv (built-in)

Gets data from football-data.co.uk and outputs average shots and goals for and against to .csv.

<b>NOTE:</b> In order to work on .csv-files with no 'referee'-column, line indexes must be tweaked to fit in collectstats.py.
Works on English leagues, not including Conference.

Instructions:
 - Download all files to the same folder, and run FOOTBALLSTATS.py
 - Downloaded data and generated stats (.csv-files) will show in same folder as script.
 

Output will be to .csv with averages of data input, listed in the following order per line:

[0] Team.

[1] Home: shots per game.

[2] Home: goals per shot (p(shot=goal)).

[3] Home: shots against per game.

[4] Home: goals against per shot against(p(shot against=goal against)).

[5] Away: shots per game.

[6] Away: goals per shot.

[7] Away: shots against per game.

[8] Away: goals against per shot against.

<b>Example:</b>

<i>Liverpool,17.4211,0.136,7.4211,0.1277,16.1579,0.1075,8.7368,0.1446</i>

Liverpool has an average of 17.4211 shots per game.
Liverpool scores on average 0.136 goals for every shot they take.
