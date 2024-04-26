from fastapi import APIRouter, Depends, HTTPException
from .schemas import S3ObjectRequest, S3ObjectResponse, AWSCredentials
from app.services.s3_services import S3Service
from app.services.cache_service import RedisCache

router = APIRouter()

# Creating our Quick S3 get_object implementation
@router.post("/s3/get-object", response_model=S3ObjectResponse)
def get_s3_object(request: S3ObjectRequest, creds: AWSCredentials = Depends()):
    cache = RedisCache()
    s3_service = S3Service(creds.aws_access_key_id, creds.aws_secret_access_key, creds.region_name)

    # First, try to get the object from the cache
    cached_data = cache.get(request.object_key)
    if cached_data:
        return S3ObjectResponse(object_key=request.object_key, data=cached_data, last_modified="From Cache")

    # If not cached, fetch from S3 and cache it
    object_data = s3_service.download_file(request.bucket_name, request.object_key)
    if object_data:
        cache.set(request.object_key, object_data, ttl=3600)  # cache for 1 hour
        return S3ObjectResponse(object_key=request.object_key, data=object_data, last_modified="Now")
    else:
        raise HTTPException(status_code=404, detail="Object not found in S3")

