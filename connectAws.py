#!/usr/bin/python
#AWS Connnection Class
import boto

class connectAws():
    
  def ec2Instance(self, access_key,secret_key,region):
    """This method is to create ec2 connection object
       It returns the conncection object. It takes two 
       parameter aws access key and aws secret key"""
    ec2Conn = boto.ec2.connect_to_region(region,aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    return ec2Conn


