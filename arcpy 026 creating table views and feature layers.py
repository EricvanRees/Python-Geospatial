#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     16/04/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''
Standalone Python scripts that use the Select by Attributes or Select by Location tool
require that you create an intermediate dataset rather than using feature classes or tables.
These intermediate datasets are temporary in nature and are called feature layers or table
views. Unlike feature classes and tables, these temporary datasets do not represent actual
files on disk or within a geodatabase. Instead, they are an in-memory representation of
feature classes and tables. These datasets are active only while a Python script is running.

Feature layers and table views must be created as a separate step in your Python scripts
before you can call the Select by Attributes or Select by Location tools. The Make Feature
Layer tool generates the in-memory representation of a feature class, which can then be used
to create queries and selection sets as well as join tables. After this step has been completed,
you can use the Select by Attributes or Select by Location tool. Similarly, the Make Table
View tool is used to create an in-memory representation of a table.
'''

# import arcpy module
import arcpy

# save the workspace
arcpy.env.workspace = "c:/ArcpyBook/data/CityOfSanAntonio.gdb"

# start a try block
try:
    # Make an in-memory copy of the Burglary feature class using the Make Feature Layer
    # tool.
    flayer = arcpy.MakeFeatureLayer_management(management("Burglary","Burglary_Layer")
    # make table view works simililarly:
    # tView = arcpy.MakeTableView_management("Crime2009Table","Crime2009TView")
# Add an except block with error message:
except Exception as e:
    print(e.message)

