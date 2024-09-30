import boto3
import os

class Uploader:
    def __init__(self, config_manager):
        self.s3_client = boto3.client('s3', 
                                      aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'), 
                                      aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
        self.config_manager = config_manager
        self.local_queue = []

    def upload_data(self):
        # Check if there are files to upload (screenshots, logs, etc.)
        files = self.get_files_to_upload()
        for file in files:
            try:
                self.upload_to_s3(file)
            except Exception as e:
                print(f"Failed to upload {file}. Error: {e}")
                self.local_queue.append(file)  # Retry later

    def upload_to_s3(self, file_path):
        bucket_name = self.config_manager.get_s3_bucket_name()
        key = os.path.basename(file_path)
        with open(file_path, 'rb') as f:
            self.s3_client.upload_fileobj(f, bucket_name, key)
        print(f"Uploaded {file_path} to S3")

    def get_files_to_upload(self):
        # Collect files (e.g., screenshots, logs) that need to be uploaded
        return [f for f in os.listdir() if f.endswith(".png") or f.endswith(".log")]
