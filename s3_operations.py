import boto3
import json

def upload_to_s3(data_list, aws_access_key, aws_secret_key, bucket_name, prefix):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
    
    for idx, data in enumerate(data_list):
        json_data = json.dumps(data, indent=2)
        s3_key = f"{prefix}/document_{idx + 1}.json"
        s3.put_object(Body=json_data, Bucket=bucket_name, Key=s3_key)
        print(f"Uploaded document_{idx + 1}.json to S3 bucket {bucket_name} with key {s3_key}")