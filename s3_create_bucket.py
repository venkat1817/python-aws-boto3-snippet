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






#This code execute
import boto3

# Set your desired region
region_name = 'ap-southeast-1'  

# Initialize the S3 resource with the specified region
s3_resource = boto3.resource('s3', region_name=region_name)

# Set your desired bucket name
bucket_name = 'dev-environment-data' 

# Create the bucket using the specified configuration
try:
    bucket = s3_resource.create_bucket(
        ACL='private',  
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region_name  
        }
    )
    print("Amazon S3 bucket has been created")
except Exception as e:
    print("Error creating Amazon S3 bucket:", e)
