#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     04/04/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# this script adds layers to a map using the AddLayer function
# script only runs in ArcMap as it references currently loaded map documents

# import the module
import arcpy.mapping as mapping

# reference the currently active document
mxd = mapping.MapDocument("CURRENT")

# get a reference to the "Crime" dataframe
df = mapping.ListDataFrames(mxd)[0]

# create a layer object that references a Layer file
layer = mapping.Layer(r"C:\ArcpyBook\data\School_Districts.lyr")

# add the layer to the dataframe
mapping.AddLayer(df, layer, "AUTO_ARRANGE")

