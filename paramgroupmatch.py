# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\PAULINKENBRANDT\.spyder2\.temp.py
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
 
data = getDataFromFile("AGRC_PGROUP_MATCH.xlsx")

pgroup = data['paramgroup']
param = data['paraml']

for i in range(len(pgroup)):
    pgroup[i]=str(pgroup[i])    


for i in range(len(param)):
    param[i]=str(param[i])    

print param

d = dict(zip(param,pgroup))
f = (zip(pgroup,param))

inorganics_major_metals = []
inorganics_major_nonmetals = []
inorganics_minor_metals = []
inorganics_minor_nonmetals = []
nutrient = []

print f[1][0]

def fndtyp(f,groupvarname,nametype):
    groupvarname = []    
    for i in range(len(f)):
        if f[i][0] == nametype:
            groupvarname.append(f[i][1])
    return groupvarname

imajnm = fndtyp(f,inorganics_major_nonmetals,'Inorganics, Major, Non-metals')
imajm = fndtyp(f,inorganics_major_metals,'Inorganics, Major, Metals')
iminnm = fndtyp(f,inorganics_minor_nonmetals,'Inorganics, Minor, Non-metals')
iminm = fndtyp(f,inorganics_minor_metals,'Inorganics, Minor, Metals')
nutr = fndtyp(f,nutrient,'Nutrient')

print nutr
