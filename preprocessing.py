"""
In the Units field, make all mg/L and ug/L lowercase while preserving other uppercase letters
Fill the ParamGroup field using the table

"""

if Param == "Nitrate" and Unit == "mg/l as N":	
    ResultValue  =  ResultValue * 4.426802887	
    Unit = "mg/l"

if Param == "Nitrite" and Unit == "mg/l as N":	
    ResultValue  =  ResultValue * 3.284535258	
    Unit = "mg/l"

if Param == "Phosphate" and Unit == "mg/l as P":	
    ResultValue  =  ResultValue * 3.131265779	
    Unit = "mg/l"

if Param == "Bicarbonate as CaCO3" and Unit == "mg/l":	
    ResultValue  =  ResultValue * 1.22
    Param = "Bicarbonate"
    
if Param == "Bicarbonate as CaCO3" and Unit == "mg/l as CaCO3":	
    ResultValue  =  ResultValue * 1.22	
    Unit = "mg/l"
    Param = "Bicarbonate"
    
if Param == "Bicarbonate" and Unit == "mg/l as CaCO3":	
    ResultValue  =  ResultValue * 1.22	
    Unit = "mg/l"

if Param == "Phosphate-phosphorus" and Unit == "mg/l as P":	
    ResultValue  =  ResultValue * 3.131265779	
    Unit = "mg/l"
    Param = "Phosphate"

if Param == "Phosphate-phosphorus" and Unit == "mg/l":	
    ResultValue  =  ResultValue * 3.131265779	
    Param = "Phosphate"  
    
if Param == "Sulfate as S" and Unit == "mg/l":	
    ResultValue  =  ResultValue * 0.333792756	
    Param = "Sulfate"
    
if Param == "Nitrate-Nitrogen" and Unit == "mg/l as N":	
    ResultValue  =  ResultValue * 4.426802887	
    Unit = "mg/l"
    Param = "Nitrate"

if Param == "Nitrate as N" and Unit == "mg/l as N":	
    ResultValue  =  ResultValue * 4.426802887	
    Unit = "mg/l"
    Param = "Nitrate"

if Param == "Nitrite as N" and Unit == "mg/l as N":	
    ResultValue  =  ResultValue * 3.284535258	
    Unit = "mg/l"
    Param = "Nitrite"

if Param == "Nitrate-Nitrogen" and Unit == "mg/l":	
    ResultValue  =  ResultValue * 4.426802887	
    Param = "Nitrite"

if Param == "Nitrate as N" and Unit == "mg/l":	
    ResultValue  =  ResultValue * 4.426802887	
    Param = "Nitrate"

if Param == "Nitrite as N" and Unit == "mg/l":	
    ResultValue  =  ResultValue * 3.284535258	
    Unit = "mg/l"
    Param = "Nitrite"

if Param == "Inorganic nitrogen (nitrate and nitrite) as N" and Unit == "mg/l as N":	
    ResultValue  =  ResultValue * 4.426802887	
    Unit = "mg/l"
    Param = "Inorganic nitrogen (nitrate and nitrite) as NO3"

if Param == "Inorganic nitrogen (nitrate and nitrite) as N" and Unit == "mg/l":	
    ResultValue  =  ResultValue * 4.426802887	
    Unit = "mg/l"
    Param = "Inorganic nitrogen (nitrate and nitrite) as NO3"

if Param == "Phosphate-phosphorus as P" and Unit == "mg/l as P":	
    ResultValue  =  ResultValue * 3.131265779	
    Param = "Phosphate"

if Param == "Orthophosphate as P" and Unit == "mg/l as P":	
    ResultValue  =  ResultValue * 3.131265779	
    Unit = "mg/l"
    Param = "Phosphate"

if Param == "Phosphate-phosphorus as P" and Unit == "mg/l":	
    ResultValue  =  ResultValue * 3.131265779	
    Param = "Phosphate"

if Param == "Orthophosphate as P" and Unit == "mg/l":	
    ResultValue  =  ResultValue * 3.131265779	
    Param = "Phosphate"

if Param == "Orthophosphate" and Unit == "mg/l as P":	
    ResultValue  =  ResultValue * 3.131265779	
    Unit = "mg/l"
    Param = "Phosphate"

if Param == "Ammonia and ammonium" and Unit == "mg/l NH4":	
    ResultValue  =  ResultValue * 1.05918619	
    Unit = "mg/l"
    Param = "Ammonia"

if Param == "Ammonia-nitrogen as N" and Unit == "mg/l as N":	
    ResultValue  =  ResultValue * 1.21587526	
    Unit = "mg/l"
    Param = "Ammonia"

if Param == "Ammonia-nitrogen" and Unit == "mg/l as N":	
    ResultValue  =  ResultValue * 1.21587526	
    Unit = "mg/l"
    Param = "Ammonia"

if Param == "Ammonia-nitrogen as N" and Unit == "mg/l":	
    ResultValue  =  ResultValue * 1.21587526	
    Param = "Ammonia"

if Param == "Ammonia-nitrogen" and Unit == "mg/l":	
    ResultValue  =  ResultValue * 1.21587526	
    Param = "Ammonia"

if Param == "Ammonia" and Unit == "mg/l as N":	
    ResultValue  =  ResultValue * 1.21587526	
    Unit = "mg/l"
    
if Param == "Specific conductance" and Unit == "mS/cm":	
    ResultValue  =  ResultValue * 1000	
    Unit = "uS/cm"
    
if Param == "Specific conductance" and Unit == "umho/cm":		
    Unit = "uS/cm"
  
if ParamGroup == "Inorganics, Major, Metals" and Unit == "ug/l":	
    ResultValue  =  ResultValue * 0.001	
    Unit = "mg/l"

if ParamGroup == "Inorganics, Minor, Metals" and Unit == "mg/l":	
    ResultValue  =  ResultValue * 1000	
    Unit = "ug/l"

if ParamGroup == "Inorganics, Major, Non-metals" and Unit == "ug/l":	
    ResultValue  =  ResultValue * 0.001	
    Unit = "mg/l"

if ParamGroup == "Inorganics, Minor, Non-metals" and Unit == "mg/l":	
    ResultValue  =  ResultValue * 1000	
    Unit = "ug/l"

if ParamGroup == "Nutrient" and Unit == "ug/l":	
    ResultValue  =  ResultValue * 0.001	
    Unit = "mg/l"
  
if Param == "Calcium" and Unit == "ueq/L":	
    ResultValue  =  ResultValue * 20.039	
    Unit = "mg/l"
    
if Param == "Magnesium" and Unit == "ueq/L":	
    ResultValue  =  ResultValue * 12.1525	
    Unit = "mg/l"
    
if Param == "Potassium" and Unit == "ueq/L":	
    ResultValue  =  ResultValue * 39.0983	
    Unit = "mg/l"
    
if Param == "Sodium" and Unit == "ueq/L":	
    ResultValue  =  ResultValue * 22.9897	
    Unit = "mg/l"
    
if Param == "Nitrate" and Unit == "ueq/L":	
    ResultValue  =  ResultValue * 62.0049	
    Unit = "mg/l"
    
if Param == "Chloride" and Unit == "ueq/L":	
    ResultValue  =  ResultValue * 35.453	
    Unit = "mg/l"
    
if Param == "Hydroxide" and Unit == "ueq/L":	
    ResultValue  =  ResultValue * 17.0073	
    Unit = "mg/l"
    
if Param == "Sulfate" and Unit == "ueq/L":	
    ResultValue  =  ResultValue * 24.01565	
    Unit = "mg/l"

