import boto3
import os

BUCKET_NAME = os.getenv('S3_BUCKET_NAME', 'd3-baseball-data')

s3_client = boto3.client('s3')

def upload_file_to_s3(local_path: str, s3_key: str):
    """
    Uploads a local file to S3.

    :param local_path: path to the file on local disk
    :param s3_key: path you want to store the file inside s3 bucket
    """
    try:
        s3_client.upload_file(local_path, BUCKET_NAME, s3_key)
        print(f"Uploaded {local_path} to s3://{BUCKET_NAME}/{s3_key}")
    except Exception as e:
        print(f"Error uploading {local_path} to S3: {e}")