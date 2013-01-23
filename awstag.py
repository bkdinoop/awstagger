#!/usr/bin/python 
#EBS volume fetch information
import sys
import connectAws 

def addTag(region, akey, skey, resourceId, tagDict):
  region = "us-west-1"
  ec2 = connectAws()
  ec2Obj = ec2.ec2Instance(akey, skey, region)
  result = ec2Obj.create_tags(resourceId, tagDict)
  if result:
    print "Created Tag for", resourceID
  else:
    print "Error:Not created Tag for", resourceID
    
def removeTag(region, akey, skey, resourceId, tagDict):
  region="us-west-1"
  ec2 = ec2Instance(akey, skey, region)
  result = ec2.create_tags(resourceId,tagDict)
  if result:
    print "Removed tag for", resourceId
  else:
    print "Error:Not Removed for",resourceID

def main():
  print len(sys.argv)
  option = sys.argv[1]
  print option
  if option == '--file':
    fileObj = open(filename,'rw')
    
  elif option == '--help':
    print 'I can help you'
  else:
	  print 'valid options --file | --help'
	  d
if __name__ == '__main__':
  main()
  
