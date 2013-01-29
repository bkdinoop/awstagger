#!/usr/bin/python 
#AWS resource Tagger
import sys
from connectAws import ConnectAws
from checkConfig import  CheckValidation 
from parse2dict import parsefile 

def addTag(ec2Obj, resourceId, tagDict):
  """Tag the aws resource with aws-connection object, resource-id and tagging(dict) as input."""
  result = ec2Obj.create_tags(resourceId, tagDict)
  if result:
    print "Created Tag for", resourceId
  else:
    print "Error:Not created Tag for", resourceId
    
def removeTag(ec2Obj, resourceId, tagDict):
  """Remove a tag in aws with aws-connection object, resource-id and tagging(dict) as input."""
  result = ec2Obj.delete_tags(resourceId,tagDict)
  if result:
    print "Removed tag for", resourceId
  else:
    print "Error:Not Removed for",resourceId

def main():
	
  """Main function asks the config file where all the needed information are mentioned
     Checks the validity of the file and content then sent to tag as per the operation. 
  """
	
  print """##############################################################
#Config file should be in same folder where the python script is there
#Config should contain aws region, aws credential details and tagging information filename
#########################################################
  """
  configFile = raw_input('Enter the config file-name : ')
  chkObject =  CheckValidation()
  fileCheck, filestatus = chkObject.fileExists(configFile)
  region,akey,skey,infoFile,operation='','','','',''
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
      elif l[0] == 'operation':
        operation = l[1]
      elif l[0] == 'filename':
        infoFile = l[1]	

    if chkObject.customCheck(region,akey,skey,infoFile,operation):
      taggerVal = parsefile(infoFile)
      ec2 = ConnectAws()
      ec2Obj = ec2.ec2Instance(akey, skey, region)
      for tv in taggerVal.items():
        if operation == "add":
          addTag(ec2Obj, tv[0],tv[1])
        elif operation == "remove":
          removeTag(ec2Obj, tv[0],tv[1])
        else:
          print "Error in Word operation usage: small letter <add> or <remove>"
    else:
      print "Error in either region or aws-key or filename"
  else:
    print filestatus

if __name__ == '__main__':
  main()
  
