#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     03/04/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# import arcpy mapping module
import arcpy.mapping as mapping

# reference currently active map document
mxd = mapping.MapDocument("CURRENT")

# Get the active data frame and zoom to selected features
mxd.activeDataFrame.zoomToSelectedFeatures()

# next, go to "selection -> clear selected features"
# drag a box around cluster of burglaries inside Northside ISD boundary

# get a reference to the Crime dataframe
df = mapping.ListDataFrames(mxd, "Crime")[0]

# reference the burglaries layer
layer = mapping.ListLayers(mxd, "Burglaries*", df)[0]

# set the extent of the data frame by getting the extent of the selected features
# map will automaticically zoom into selected features
df.extent = layer.getSelectedExtent()
