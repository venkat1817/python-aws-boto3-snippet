#!/usr/bin/python
import boto3
from decouple import config

session=boto3.session.Session(profile_name="default")

AWS_REGION = config('AWS_REGION')

ec2_con_re=session.resource(service_name="ec2",region_name=AWS_REGION)
my_inst=ec2_con_re.Instance(id="i-XXXXXXXXXXXXXXXXX")
#print dir(my_inst)
my_inst.start()
#my_inst.stop()