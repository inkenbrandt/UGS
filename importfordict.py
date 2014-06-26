# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 16:14:51 2014

@author: paulinkenbrandt
"""

import xlrd
 
 
def getDataFromFile(fileName):
    with xlrd.open_workbook(fileName) as wb:
        # we are using the first sheet here
        worksheet = wb.sheet_by_index(0)
        # getting number or rows and setting current row as 0 -e.g first
        num_rows, curr_row = worksheet.nrows - 1, 0
        # retrieving keys values(first row values)
        keyValues = [x.value for x in worksheet.row(0)]
        # building dict
        data = dict((x, []) for x in keyValues)
        # iterating through all rows and fulfilling our dictionary
        while curr_row < num_rows:
            curr_row += 1
            for idx, val in enumerate(worksheet.row(curr_row)):
                if val.value.strip():
                    data[keyValues[idx]].append(val.value)
        return data
 
data = getDataFromFile("C:\\PROJECTS\\EPA EN\\Data\\DOGM_AGRC.xlsx")

for i in range(len(data['paramgroup'])):
    data['paramgroup'][i]=str(data['paramgroup'][i])    

print data['paramgroup']

for i in range(len(data['param'])):
    data['param'][i]=str(data['param'][i])    

print data['param']

a = [1,2,3,4]
b = [5,6,7]

print a+b

#workbook = xlrd.open_workbook('C:\\PROJECTS\\EPA EN\\Data\\DOGM_AGRC.xlsx')
#sheet = workbook.sheet_by_name('DOGM_AGRC')
#
#r = sheet.row(0)
#c = sheet.col_values(0)
#
#data = [] #make a data store
#for i in sheet.col(1):
#  data.append(sheet.row_values(i)) #drop all the values in the rows into data
#
#print data