#!/usr/bin/env python3
import boto3
from decouple import config

AWS_REGION = config('AWS_REGION')

resource = boto3.resource("s3", region_name=AWS_REGION)
bucket_name = config('BUCKET_NAME')
location = {'LocationConstraint': AWS_REGION}
bucket = resource.create_bucket(
    ACL = 'private',
    Bucket = bucket_name,
    CreateBucketConfiguration = location)
print("Amazon S3 bucket has been created")