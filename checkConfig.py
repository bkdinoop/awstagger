#!/usr/bin/python
#Class to check the validation of user's input
#Seperate method for File check, region check and aws credentials.
from connectAws import connectAws

class checkValidation():
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
    ec2 = connectAws()
    ec2Obj = ec2.ec2Instance(akey, skey, region)
    del ec2Obj
    return True
    
  def customCheck(self,region,ak,sk,fileinfo):
    ckObj = checkValidation()
    if ckObj.regValidate(region):
      if ckObj.checkAWSkey(ak, sk, region):
        fCheck,fStatus = ckObj.fileExists(fileinfo) 
        if fCheck:
          print fStatus;return True
        else:
          print fStatus;exit()
      else:
        print "Error in Acess and Secret KEY"
    else:
      print "Error in the Region-Name"

