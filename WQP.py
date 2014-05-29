# -*- coding: utf-8 -*-
"""
Created on Wed May 21 14:55:02 2014

@author: paulinkenbrandt
"""

# Import system modules
import arcpy

 
# Set workspace
arcpy.env.workspace = "C:/Temp/test.gdb"
fc = "C:/Temp/test.gdb/Stations"
tb = "C:/Temp/test.gdb/Results" 
# Set local variables
Results = "Results"
Stations = "Stations"
StationID = "StationID"
Unit = "Unit"

"""Remove _WQX string from stationID
_WQX separates legacy EPA data from modern EPA data
the addition of this suffix creates unecessary station duplicates""" 
#arcpy.CalculateField_management(Results,fieldName,"!StationID!.lstrip('_WQX')", "PYTHON_9.3")
#arcpy.CalculateField_management(Results,fieldName,"!StationID!.strip('')", "PYTHON_9.3")
#print 'Results _WQX and whitespace removal complete'
#arcpy.CalculateField_management(Stations,fieldName,"!StationID!.lstrip('_WQX')", "PYTHON_9.3")
#arcpy.CalculateField_management(Stations,fieldName,"!StationID!.strip('')", "PYTHON_9.3")
#print 'Stations _WQX removal complete'
#
## remove duplicates
#arcpy.DeleteIdentical_management(Stations,fieldName,"100 meters","")
#print 'Duplicates deleted'
#
## remove trailing white space in all fields
#arcpy.CalculateField_management(Results,fieldName,"!Unit!.strip()", "PYTHON_9.3")
#print 'unit spaces stripped'

with arcpy.da.Editor("C:/Temp/test.gdb") as edit:
    """Remove _WQX string from stationID
    _WQX separates legacy EPA data from modern EPA data
    the addition of this suffix creates unecessary station duplicates""" 
    quer = "StationID LIKE '%_WQX%'"    
    cursor= arcpy.UpdateCursor(fc,quer)
    for row in cursor:
        row.setValue(StationID, StationID.strip('_WQX'))
    print 'station WQX stripped'
    cursor= arcpy.UpdateCursor(tb,quer)
    for row in cursor:
        row.setValue(StationID, StationID.strip('_WQX'))
    print 'result WQX stripped'
    
with arcpy.da.Editor("C:/Temp/test.gdb") as edit:
    arcpy.DeleteIdentical_management(Stations,StationID,"100 meters")
    print 'Duplicate Stations Removed'    

with arcpy.da.Editor("C:/Temp/test.gdb") as edit:
    # remove white space
    quer = "StationID LIKE '% %'"    
    cursor= arcpy.UpdateCursor(fc,quer)
    for row in cursor:
        row.setValue(StationID, StationID.strip())
    print 'Station Whitespace stripped'
    cursor= arcpy.UpdateCursor(tb,quer)
    for row in cursor:
        row.setValue(StationID, StationID.strip())
    print 'Result whitespace stripped'
    
    #fix units
    quer = "Unit LIKE '% %'"
    cursor= arcpy.UpdateCursor(tb, quer)
    for row in cursor:        
        row.setValue(Unit, Unit.strip())
    quer = "Unit = 'mg/L'"
    cursor= arcpy.UpdateCursor(tb,quer)    
    for row in cursor:
        row.setValue(Unit, 'mg/l')
    print 'mg/l fixed'
    
    
       


print 'done'


## convert to micrograms per liter for metals
#if (Param == 'Aluminum' or Param == 'Arsenic' or Param == 'Barium' or Param == 'Beryllium' 
#or Param == 'Boron' or Param == 'Cadmium' ) and Unit == 'mg/l':
#    ResultValue = ResultValue*1000
#
#Chromium
#Copper
#
#
#
## convert Nitrate as NO3 to Nitrate as N; correct Param field for conversion
#if Param == 'Nitrate' and Unit == 'mg/l':    
#    ResultValue = ResultValue*0.2259 
#    Param = Param + 'as N'
#
## standardize Nitrate as N units
#if Param == 'Nitrate' and Unit =='mg/l as N':
#    Unit = 'mg/l'
#    Param = 'Nitrate as N'
#
## standardize alkalinity Param fields
#if Param == 'Alkalinity, total' and SampFrac is None:
#    Param = 'Alkalinity'
#    SampFrac = 'Total'
#elif Param == 'Alkalinity, total' and SampFrac == 'Dissolved':
#    Param = 'Alkalinity'
#    SampFrac = 'Dissolved'
#
## standardize E coli Param fields
#if 'Escherichia' in Param and Unit == 'cfu/1ml':
#    Param = 'Escheriachia coli'
#    
#    

