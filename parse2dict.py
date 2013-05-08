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
__title__ = 'parse2dict'

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
