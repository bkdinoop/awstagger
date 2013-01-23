#!/usr/bin/python
#Parse a xls file or a string and store it as a dict 
import sys
import xlrd

def parseXl(workBook):
  wb = xlrd.open_workbook(workBook)
  wb.sheet_names()
  sheets = wb.sheet_by_index(0)
  lsheet = {}
  for rownum in range(sheets.nrows):
    dKey = (sheets.row_values(rownum))[1].strip()
    dValue = (sheets.row_values(rownum))[4].strip()
    #lsheet[dKey] = 
    lsheet.update({dKey:{'Name':dValue}})
  
  return lsheet
  

