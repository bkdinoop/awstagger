#!/usr/bin/python
#Class to check the validation of user's input
#Seperate method for File check, region check and aws credentials.
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
    
  def chkOperation(self,operation):
    available = False
    operations = {'add','remove'}
    for op in operations:
      if op == operation:
        available = True
      
    return available
    
  def customCheck(self,region,ak,sk,fileinfo,operation):
    ckObj = CheckValidation()
    if ckObj.regValidate(region) and ckObj.chkOperation(operation):
      if ckObj.checkAWSkey(ak, sk, region):
        fCheck,fStatus = ckObj.fileExists(fileinfo) 
        if fCheck:
          print fStatus;return True
        else:
          print fStatus;exit()
      else:
        print "Error in Acess and Secret Key"
    else:
      print "Error in the Region-Name or operation should be 'add' or 'remove' "

