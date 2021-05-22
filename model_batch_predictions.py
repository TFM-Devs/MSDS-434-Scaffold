def run_predict(event, context):
  from google.cloud import automl_v1beta1 as automl
  from google.cloud import bigquery
  
  PROJECT_ID = 'msds-434-309203'
  COMPUTE_REGION = 'us-central1'
  automl_client = automl.AutoMlClient()
  tables_client = automl.TablesClient(project=PROJECT_ID, region=COMPUTE_REGION)
  bq_client = bigquery.Client()

  list_datasets = tables_client.list_datasets()
  datasets = { dataset.display_name: dataset.name for dataset in list_datasets }
  print(datasets)

  dataset = 'msds-434-309203:test.ncaa_bucket2'

  list_models = tables_client.list_models()
  models = {model.display_name: model.name for model in list_models }
  print(models)

  model = 'ncaa_model'
  output_table = 'msds-434-309203:test.ncaa_bucket2_copy'

  response = tables_client.batch_predict(model_display_name=model, bigquery_input_uri=dataset, bigquery_output_uri=output_table)
