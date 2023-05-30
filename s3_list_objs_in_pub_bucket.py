#!/usr/bin/python
import requests
import boto3
from botocore import UNSIGNED
from botocore.client import Config

s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
response = s3.list_objects_v2(Bucket="coderbytechallengesandbox")

for content in response.get('Contents',[]):
  print(content['Key'])