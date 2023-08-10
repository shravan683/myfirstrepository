import boto3
import requests

def upload_file_to_s3(file_url, file_name, s3_bucket):
    response = requests.get(file_url)
    if response.status_code == 200:
        s3_client = boto3.client('s3')
        s3_client.put_object(Bucket=s3_bucket, Key=file_name, Body=response.content)
        print("File uploaded successfully to S3.")
    else:
        print("Failed to download the file from the URL.")

if __name__ == "__main__":
    api_endpoint = 'https://ovsqhm1ck5.execute-api.ap-south-1.amazonaws.com'  # Replace with the actual API endpoint URL
    s3_bucket = 'shravanm683'  # Replace with your S3 bucket name
    file_url = 'https://app.hubspot.com/file-preview/7472893/file/127379836002'  # Replace with the actual URL of the file you want to upload
    file_name = 'hi'  # Replace with the desired file name for S3

    payload = {
        'file_url': file_url,
        'file_name': file_name,
        's3_bucket': s3_bucket
    }

    response = requests.post(api_endpoint, json=payload)

    if response.status_code == 200:
        print("File upload request sent successfully.")
    else:
        print("Failed to send the file upload request.")
