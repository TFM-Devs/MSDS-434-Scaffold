import pandas as pd

# https://cloud.google.com/resource-manager/docs/creating-managing-projects
project_id = 'msds-434-309203'
sample_count = 2000

row_count = pd.io.gbq.read_gbq('''
  SELECT 
    COUNT(*) as total
  FROM bigquery-public-data.ncaa_basketball.mbb_games_sr
''', project_id=project_id).total[0]

df = pd.io.gbq.read_gbq(f'''
  SELECT
    *
  FROM
    bigquery-public-data.ncaa_basketball.mbb_teams_games_sr
  WHERE RAND() < {sample_count}/{row_count}
''', project_id=project_id)

print(f'Full dataset has {row_count} rows')

df = pd.DataFrame(df)

df = df[df["tournament"] == 'NCAA']

df = df[['game_id','market','opp_market','points','opp_points','win','field_goals_pct','opp_field_goals_pct','rebounds','opp_rebounds',
          'assists','opp_assists','steals','opp_steals','blocks','opp_blocks','turnovers','opp_turnovers']]