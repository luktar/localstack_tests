import boto3
import os

def upload_file():
    # Configure boto3 client for LocalStack
    s3_client = boto3.client(
        's3',
        endpoint_url='http://localhost:4566',
        aws_access_key_id='test',
        aws_secret_access_key='test',
        region_name='eu-central-1'
    )

    # File to upload
    file_path = 'file.txt'
    bucket_name = 'my-test-bucket'
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found!")
        return

    try:
        # Upload the file
        s3_client.upload_file(file_path, bucket_name, file_path)
        print(f"Successfully uploaded {file_path} to {bucket_name}")
    except Exception as e:
        print(f"Error uploading file: {str(e)}")

if __name__ == "__main__":
    upload_file() 