import boto3
import requests

def upload_file_to_s3(url, s3_bucket):
    response = requests.get(url)
    if response.status_code == 200:
        s3_client = boto3.client('s3')
        s3_client.put_object(Bucket=s3_bucket, Key='basic-link-1.pdf', Body=response.content)
        print("File uploaded successfully to S3.")
    else:
        print("Failed to download the file from the URL.")

if __name__ == "__main__":
    url = 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'  # Replace with the actual URL of the file you want to upload
    s3_bucket = 'shravanm683'  # Replace with your S3 bucket name
    upload_file_to_s3(url, s3_bucket)
