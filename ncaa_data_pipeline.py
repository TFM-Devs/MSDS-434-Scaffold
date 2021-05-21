def hello_pubsub(event, context):
  import pandas as pd
  from datalab.context import Context
  import google.cloud.storage as storage
  import google.cloud.bigquery as bq
  client = bq.Client()
  
  project_id = 'msds-434-309203'
  sample_count = 300000000

  row_count = pd.io.gbq.read_gbq('''SELECT COUNT(*) as total
      FROM bigquery-public-data.ncaa_basketball.mbb_games_sr''', project_id=project_id).total[0]

  df = pd.io.gbq.read_gbq(f'''SELECT *
    FROM bigquery-public-data.ncaa_basketball.mbb_teams_games_sr
    WHERE RAND() < {sample_count}/{row_count}''', project_id=project_id)

  print(f'Full dataset has {row_count} rows')

  df = pd.DataFrame(df)

  #df = df[df["tournament"] == 'NCAA']

  df = df[['game_id','market','opp_market','points','opp_points','field_goals_pct','opp_field_goals_pct','rebounds','opp_rebounds',
          'assists','opp_assists','steals','opp_steals','blocks','opp_blocks','turnovers','opp_turnovers']]

  df = df.dropna()
    # Dataframe to write
  simple_dataframe = df

  sample_bucket_name = Context.default().project_id + '-ncaa_bucket2'
  sample_bucket_path = 'gs://' + sample_bucket_name
  sample_bucket_object = sample_bucket_path + 'ncaa_bucket2.txt'
  bigquery_dataset_name = 'test'
  bigquery_table_name = 'ncaa_bucket2'

  # Define storage bucket
  sample_bucket = storage.Bucket(sample_bucket_name)
  
  # Create storage bucket if it does not exist
  #if not sample_bucket.exists():
  #  sample_bucket.create()

  # Define BigQuery dataset and table
  dataset = bq.Dataset('msds-434-309203.ncaa_bucket2')
 
  #table = bq.Table(project_id + '.' + bigquery_dataset_name + '.' + bigquery_table_name)
  
  # Create BigQuery dataset
  #if not dataset.exists():
  #  dataset.create()

  # Create or overwrite the existing table if it exists
  #table_schema = bq.schema.from_data(simple_dataframe)

  table_schema=[
      bq.SchemaField("game_id", "STRING"),
      bq.SchemaField("market", "STRING"),
      bq.SchemaField("opp_market", "STRING"),
      bq.SchemaField("points", "INTEGER"),
      bq.SchemaField("opp_points", "INTEGER"),
      bq.SchemaField("field_goals_pct", "FLOAT"),
      bq.SchemaField("rebounds", "INTEGER"),
      bq.SchemaField("opp_rebounds", "INTEGER"),
      bq.SchemaField("assists", "INTEGER"),
      bq.SchemaField("opp_assists", "INTEGER"),
      bq.SchemaField("steals", "INTEGER"),
      bq.SchemaField("opp_steals", "INTEGER"),
      bq.SchemaField("blocks", "INTEGER"),
      bq.SchemaField("opp_blocks", "INTEGER"),
      bq.SchemaField("turnovers", "INTEGER"),
      bq.SchemaField("opp_turnovers", "INTEGER"),
    ]

  job_config = bq.LoadJobConfig(
    write_disposition=bq.WriteDisposition.WRITE_TRUNCATE
  )

  table = bq.Table(project_id + '.' + bigquery_dataset_name + '.' + bigquery_table_name, schema=table_schema)
  #table = client.create_table(table)

  # Write the DataFrame to GCS (Google Cloud Storage)
  #%storage write --variable simple_dataframe --object $sample_bucket_object

  # Write the DataFrame to a BigQuery table
  client.load_table_from_dataframe(simple_dataframe, table, job_config=job_config)

  if __name__ == "__main__":
    hello_pubsub()
   