#!/usr/bin/python
# Copyright (c) 2013 Dinoop Balakrishnan
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

__author__ = 'Dinoop Balakrishnan'
__title__ = 'connectAws'

import boto
import boto.ec2

class ConnectAws():
    
  def ec2Instance(self, access_key,secret_key,region):
    """This method is to create ec2 connection object
       It returns the conncection object. It takes two 
       parameter aws access key and aws secret key"""
    try:       
      ec2Conn = boto.ec2.connect_to_region(region,aws_access_key_id=access_key, aws_secret_access_key=secret_key)
      return ec2Conn
    except boto.exception.EC2ResponseError as e:
      print e
      exit()
