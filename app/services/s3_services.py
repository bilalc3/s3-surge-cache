import boto3
from botocore.exceptions import ClientError



class S3Service:
    def __init__(self,  access_key, secret_key, bucket_name):
        self.s3_client = boto3.client('s3',
                                    aws_access_key_id=access_key,
                                    aws_secret_access_key=secret_key)
        self.bucket_name = bucket_name


    def upload_file(self, file_name: str, object_name : str):
        ''' Uploads a file to the bucket self.bucket_name '''
        try:
            response = self.s3_client.upload_file("./file_sample", self.bucket_name, object_name)
            return response
        except ClientError as e:
            print(f"Failed to upload {file_name} to {self.bucket_name}/{object_name}: {e}")
            return None

    def download_file(self, object_name, file_name):
        """Download a file from an S3 bucket"""
        try:
            self.s3_client.download_file(self.bucket_name, object_name, file_name)
        except ClientError as e:
            print(f"Failed to download {object_name} from {self.bucket_name}: {e}")

    def list_objects(self, prefix=None):
        """List files in specific S3 bucket"""
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix)
            return response.get('Contents', [])
        except ClientError as e:
            print(f"Failed to list objects in {self.bucket_name} with prefix {prefix}: {e}")
            return []

    def delete_object(self, object_name):
        """Delete object from an S3 bucket"""
        try:
            response = self.s3_client.delete_object(Bucket=self.bucket_name, Key=object_name)
            return response
        except ClientError as e:
            print(f"Failed to delete {object_name} from {self.bucket_name}: {e}")
            return None
