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
    url = 'https://www.google.com/search?sca_esv=553388756&q=image+public+access+link&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiHqaiZm8CAAxUIUGwGHfmWDsUQ0pQJegQICRAB&biw=1366&bih=611&dpr=1#imgrc=kg4_dm5Yr9tt-M'  
    s3_bucket = 'shravanm683' 
    s3_key = 'shravan136'  
    upload_file_to_s3(url, s3_bucket, s3_key)