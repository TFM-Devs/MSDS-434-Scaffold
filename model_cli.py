# TODO(developer): Uncomment and set the following variables
project_id = 'msds-434-309203'
compute_region = 'us-central1'
model_display_name = 'automl-ncaa-v1'
bq_input_uri = 'bq://msds-434-309203.test.ncaa_bucket2'
bq_output_uri = 'bq://msds-434-309203'
params = {}

from google.cloud import automl_v1beta1 as automl

client = automl.TablesClient(project=project_id, region=compute_region)

# Query model
response = client.batch_predict(bigquery_input_uri=bq_input_uri,
                                bigquery_output_uri=bq_output_uri,
                                model_display_name=model_display_name,
                                params=params)
print("Making batch prediction... ")
# `response` is a async operation descriptor,
# you can register a callback for the operation to complete via `add_done_callback`:
# def callback(operation_future):
#   result = operation_future.result()
# response.add_done_callback(callback)
#
# or block the thread polling for the operation's results:
response.result()
# AutoML puts predictions in a newly generated dataset with a name by a mask "prediction_" + model_id + "_" + timestamp
# here's how to get the dataset name:
dataset_name = response.metadata.batch_predict_details.output_info.bigquery_output_dataset

print("Batch prediction complete.\nResults are in '{}' dataset.\n{}".format(
    dataset_name, response.metadata))