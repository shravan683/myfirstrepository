import boto3
import requests
def upload_file_to_s3(url, s3_bucket, s3_key):
    response = requests.get(url)
    if response.status_code == 200:
        s3_client = boto3.client('s3')
        s3_client.put_object(Bucket=s3_bucket, Key=s3_key, Body=response.content)
        print("File uploaded successfully to S3.")
    else:
        print("Failed to download the file from the URL.")
if __name__ == "__main__":
    url = 'https://app.hubspot.com/file-preview/7472893/file/127379836002'  # Replace with the actual URL of the file you want to upload
    s3_bucket = 'shravanm683'  # Replace with your S3 bucket name
    s3_key = 'shravan13'  # Replace with the desired destination folder and file name in S3
    upload_file_to_s3(url, s3_bucket, s3_key)