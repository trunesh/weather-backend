from google.cloud import storage
import json
import os

BUCKET_NAME = os.getenv('GCS_BUCKET_NAME')

def get_bucket():
    client = storage.Client()
    return client.bucket(BUCKET_NAME)

def upload_to_gcs(file_name, data):
    bucket = get_bucket()
    blob = bucket.blob(file_name)
    blob.upload_from_string(json.dumps(data), content_type='application/json')

def list_files():
    bucket = get_bucket()
    return [blob.name for blob in bucket.list_blobs()]

def download_from_gcs(file_name):
    bucket = get_bucket()
    blob = bucket.blob(file_name)
    content = blob.download_as_text()
    return json.loads(content)
