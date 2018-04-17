#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     17/04/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''
In this recipe, you will learn how to use the Select by Location tool in a Python script to select
features based on a spatial relationship. You'll use the tool to select burglaries that are within
the boundaries of the Edgewood school district.
'''

# import module
import arcpy

# save the workspace
arcpy.env.workspace = "c:/ArcpyBook/data/CityOfSanAntonio.gdb"

# start a try block
try:
    # Make an in-memory copy of the Burglary feature class:
    flayer = arcpy.MakeFeatureLayer_management("Burglary","Burglary_Layer")
    # call the "select layer by location" tool
    arcpy.SelectLayerByLocation_management (flayer, "COMPLETELY_WITHIN", "c:/ArcpyBook/Ch7/EdgewoodSD.shp")
    # print the number of features in the layer
    cnt = arcpy.GetCount_management(flayer)
    print("The number of selected records is: " + str(cnt))
    # add an except block
except Exception as e:
    print e.message
