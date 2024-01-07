from download import download_zip_file,extract_json_data
from s3_operations import upload_to_s3
from rds_operations import load_to_rds
from dotenv import load_dotenv
import os

def main():
    url = 'https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip'
    headers = {
        "User-Agent": "Sample Company Name AdminContact@samplecompanydomain.com",
        "Accept-Encoding": "gzip, deflate",
        "Host": "www.sec.gov",
    }

    load_dotenv()

    aws_access_key = os.getenv('access_key')
    aws_secret_key = os.getenv('secret_key')
    s3_bucket = 'bucketlearner'
    s3_folder = 'my'
    rds_connection_string = os.getenv('connection_string')
    table_name = 'EdgarDataTable'

    zip_content = download_zip_file(url,headers)
    data_list = extract_json_data(zip_content)
    upload_to_s3(data_list, aws_access_key, aws_secret_key, s3_bucket, s3_folder)
    load_to_rds(s3_bucket, s3_folder, aws_access_key, aws_secret_key, rds_connection_string, table_name)
    print('Process is successful')

if __name__ == "__main__":
    main()