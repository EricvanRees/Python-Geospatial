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
In this recipe, you'll learn how to use the Select by Attributes tool to select features from a
feature class. You'll use the skills you learned in previous recipes to build a query, create a
feature layer, and finally call the Select by Attributes tool.

The Select by Attributes tool uses a query along with either a feature layer or table view
and a selection method to select records.

This script uses the option "NEW_SELECTION" from the Select Layer by Atttributes tool:
This is the default selection method and it creates a new selection set
'''

# import module
import arcpy

# save the workspace
arcpy.env.workspace = "c:/ArcpyBook/data/CityOfSanAntonio.gdb"

# start a try block:
try:
    #create a query:
    qry = '"SVCAREA" = \'North\''
    # make an in-memory copy of the Burglary feature class:
    flayer = arcpy.MakeFeatureLayer_management("Burglary","Burglary_layer")
    # call the select layer by attribute tool
    arcpy.SelectLayerByAttribute_management(flayer, "NEW_SELECTION", qry)
    # print the number of selected records
    cnt = arcpy.GetCount_management(flayer)
    print("The number of selected records is: " + str(cnt))
except Exception as e:
    print(e.message)

