import boto3
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

def upload_file_to_s3(url, s3_bucket, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        s3_client = boto3.client('s3')
        s3_client.put_object(Bucket=s3_bucket, Key=file_name, Body=response.content)
        print("File uploaded successfully to S3.")
        return True
    else:
        print("Failed to download the file from the URL.")
        return False

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json
    if 'file_url' in data and 'file_name' in data and 's3_bucket' in data:
        file_url = data['https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf']
        file_name = data['gagan']
        s3_bucket = data['shravanm683']

        success = upload_file_to_s3(file_url, s3_bucket, file_name)
        if success:
            s3_link = f"https://{s3_bucket}.s3.amazonaws.com/{file_name}"
            return jsonify({"s3_link": s3_link, "message": "File uploaded successfully and link generated."})
        else:
            return jsonify({"message": "Failed to upload the file or create link."}), 500
    else:
        return jsonify({"message": "Invalid data format. Please provide 'file_url', 'file_name', and 's3_bucket'."}), 400

if __name__ == "__main__":
    app.run(debug=True)