#!/usr/bin/python 
#AWS resource Tagger
import sys
import connectAws
from checkConfig import  checkValidation  

def addTag(region, akey, skey, resourceId, tagDict):
  ec2 = connectAws()
  ec2Obj = ec2.ec2Instance(akey, skey, region)
  result = ec2Obj.create_tags(resourceId, tagDict)
  if result:
    print "Created Tag for", resourceID
  else:
    print "Error:Not created Tag for", resourceID
    
def removeTag(region, akey, skey, resourceId, tagDict):
  ec2 = ec2Instance(akey, skey, region)
  result = ec2.create_tags(resourceId,tagDict)
  if result:
    print "Removed tag for", resourceId
  else:
    print "Error:Not Removed for",resourceID

def main():
  print """##############################################################
#Config file should be in same folder where the python script is there
#Config should contain aws region, aws credential details and tagging information filename
#########################################################
  """
  configFile = raw_input('Enter the config file-name : ')
  chkObject =  checkValidation()
  fileCheck, filestatus = chkObject.fileExists(configFile)
  region,akey,skey,infoFile='','','',''
  if fileCheck:
    parsFile = open(configFile)
    confList = parsFile.readlines()
    for cL in confList:
      ccL = cL.strip()
      l = ccL.split(':')
      if l[0] == 'ak':
        akey = l[1]
      elif l[0] == 'sk':
        skey = l[1]
      elif l[0] == 'region':
        region = l[1]
      elif l[0] == 'filename':
        infoFile = l[1]	
        	  
    print region,akey,skey,infoFile
    if chkObject.customCheck(region,akey,skey,infoFile):
      print "Checked the region,aws-key and filename"
    else:
      print "Error in either region or aws-key or filename"
  else:
    print filestatus

if __name__ == '__main__':
  main()
  
