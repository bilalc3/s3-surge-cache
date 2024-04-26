from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AWS Surge Cache"
    admin_email: str
    aws_access_key_id: str = Field(..., env='AWS_ACCESS_KEY_ID')
    aws_secret_access_key: str = Field(..., env='AWS_SECRET_ACCESS_KEY')
    redis_host: str = Field(default="localhost")
    redis_port: int = Field(default=6379)
    s3_bucket_name: str

    class Config:
        # Assuming configuration is read from a `.env` file if available
        env_file = ".env"
        env_file_encoding = 'utf-8'

# Create a settings instance that other parts of the application can import
settings = Settings()

