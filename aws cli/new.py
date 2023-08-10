import boto3
import requests
import os

def upload_file_to_s3(url, s3_bucket, s3_key, filename):
    response = requests.get(url)
    if response.status_code == 200:
        s3_client = boto3.client('s3')
        content_type = get_content_type(filename)
        s3_client.put_object(Bucket=s3_bucket, Key=s3_key, Body=response.content, ContentType=content_type)
        print("File uploaded successfully to S3.")
    else:
        print("Failed to download the file from the URL.")

def get_content_type(filename):
    import mimetypes
    content_type, _ = mimetypes.guess_type(filename)
    return content_type or 'application/octet-stream'

if __name__ == "__main__":
    url = 'https://filesamples.com/formats/txt'  
    name = url.split('/')
    name = name[len(name)-1]
    print(name)
    s3_bucket = 'shravanm683'  
    s3_key = name  
    filename = name  
    upload_file_to_s3(url, s3_bucket, s3_key, filename)