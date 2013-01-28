#!/usr/bin/python
#A module to parse a file and create the dict of resource-id as key
#and tagging value as its value 


def parsefile(fileName):
  fileObj = open(fileName)
  fList = fileObj.readlines()
  contDict = {}
  for fL in fList:
    if not fL[0] == "#":
      tagInfo = fL.strip().split(',')
      resKey = tagInfo[0]
      resVal = {}
      for tI in tagInfo[1:]:
        tagList = tI.split(':')
        resVal.update({tagList[0]:tagList[1]})
      
      contDict.update({resKey:resVal})
    else:
      continue   
      
  return contDict
