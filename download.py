import requests
from io import BytesIO
import zipfile
import json

def download_zip_file(url, headers):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to download ZIP file. Status code: {response.status_code}")

def extract_json_data(zip_content):
    with zipfile.ZipFile(BytesIO(zip_content), 'r') as zip_ref:
        data_list = [json.loads(zip_ref.open(file_name).read().decode('utf-8')) for file_name in zip_ref.namelist()]
    return data_list