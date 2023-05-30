#!/usr/bin/python
import boto3
import csv
from decouple import config

AWS_REGION = config('AWS_REGION')

ec2_resource = boto3.resource('ec2', region_name=AWS_REGION)
file_open = open('volumes.csv','w',newline='')
data_obj = csv.writer(file_open, delimiter=",")
data_obj.writerow([ 'volume_Id','volume_size',])
for volume in ec2_resource.volumes.all():
    data_obj.writerow([volume.id,volume.size,])
file_open.close()