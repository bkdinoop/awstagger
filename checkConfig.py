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
__title__ = 'awstag'

from connectAws import ConnectAws

class CheckValidation():
  def fileExists(self,fName):
    status =""
    try:
      with open(fName) as f: 
        status='File Exists' 
        return True,status
    except IOError as e:
      return False,e

  def regValidate(self, regValue):
    available = False  
    regionList = ['us-west-1','us-east-1','us-west-2','sa-east-1','eu-west-1','ap-southeast-1','ap-northeast-1','ap-southeast-2']
    for rL in regionList:
      if rL == regValue:
        available = True
     
    return available
    
  def checkAWSkey(self, akey, skey, region):
    ec2 = ConnectAws()
    ec2Obj = ec2.ec2Instance(akey, skey, region)
    del ec2Obj
    return True
    
  def checkElmt(self, element):
    if element.__contains__(":"):#this function is to check the first element
		  
  def chkOperation(self,operation):
    available = False
    operations = ['add','remove']
    for op in operations:
      if op == operation:
        available = True
      
    return available
  
  def formatCheck(self,fileinfo):
    content = open(fileinfo)
    contentList = content.readlines()
    ckObj = CheckValidation()
    for crl in contentList:
      if not crl[0] == "#":
        cList = crl.split(',')
        if len(cList) > 10:
          print "Error: Only 10 key-value pair allowed in AWS for a particular resource"
          return False
        else :
          for cL in cList: ckObj.checklen(cL); continue
              
      else: continue
      
    return True 
        	     
  def customCheck(self,region,ak,sk,fileinfo,operation):
    ckObj = CheckValidation()
    if ckObj.regValidate(region) and ckObj.chkOperation(operation):
      if ckObj.checkAWSkey(ak, sk, region):
        fCheck,fStatus = ckObj.fileExists(fileinfo) 
        if fCheck and ckObj.formatCheck(fileinfo):
          print fStatus;return True
        else:
          print fStatus;return False
      else:
        print "Error in Acess and Secret Key"; return False
    else:
      print "Error in the Region-Name or operation should be 'add' or 'remove' "; return False

