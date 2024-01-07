import boto3
import pandas as pd
from sqlalchemy import create_engine

def load_to_rds(s3_bucket, s3_folder, aws_access_key, aws_secret_key, rds_connection_string, table_name):
    engine = create_engine(rds_connection_string)
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
    
    response = s3.list_objects(Bucket=s3_bucket, Prefix=s3_folder)
    json_files = [obj['Key'] for obj in response.get('Contents', [])]
    
    df = pd.DataFrame()
    for json_file in json_files:
        s3_url = f's3://{s3_bucket}/{json_file}'
        data = pd.read_json(s3_url)
        df = df.append(data, ignore_index=True)

    df['facts'] = df['facts'].astype(str)
    df.to_sql(table_name, con=engine, if_exists='append', index=False)