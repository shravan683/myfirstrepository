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
    # You can use the 'mimetypes' module to get the content type based on the file extension.
    # Make sure you import the 'mimetypes' module at the beginning of your code.
    import mimetypes
    content_type, _ = mimetypes.guess_type(filename)
    return content_type or 'application/octet-stream'

if __name__ == "__main__":
    url = 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'  # Replace with the actual URL of the file you want to upload
    name = url.split('/')
    name = name[len(name)-1]
    print(name)
    s3_bucket = 'shravanm683'  # Replace with your S3 bucket name
    s3_key = name  # Replace with the desired destination folder and file name in S3
    filename = name  # Replace with the name of the file (including the extension) you want to save in S3
    upload_file_to_s3(url, s3_bucket, s3_key, filename)
