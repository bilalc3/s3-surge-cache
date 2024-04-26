from pydantic import BaseModel, Field

class AWSCredentials(BaseModel):
    aws_access_key_id: str = Field(..., env='AWS_ACCESS_KEY_ID')
    aws_secret_access_key: str = Field(..., env='AWS_SECRET_ACCESS_KEY')
    region_name: str = Field('us-west-1', env='AWS_DEFAULT_REGION')

class S3ObjectRequest(BaseModel):
    bucket_name: str
    object_key: str

class S3ObjectResponse(BaseModel):
    object_key: str
    data: bytes
    last_modified: str

