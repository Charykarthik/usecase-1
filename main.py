from google.cloud import bigquery
from google.cloud import storage

def load_data_to_bigquery(data, context):
# Extract bucket and file information from Cloud Storage event
bucket_name = data['bucket']
file_name = data['name']

# Set up BigQuery client and table information
client = bigquery.Client()
dataset_id = 'my_dataset'
table_id = 'my_table'
table_ref = client.dataset(dataset_id).table(table_id)

# Construct URI to Cloud Storage file
uri = f"gs://{bucket_name}/{file_name}"

# Load data into BigQuery
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.CSV
job_config.skip_leading_rows = 1
job_config.autodetect = True
load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)
load_job.result()
