#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     05/04/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# script uses UpdateLayer() function to update a number of layer properties,
# and save a file to a layer file (.lyr)

# import the module
import arcpy.mapping as mapping

# reference the currently active map document
mxd = mapping.MapDocument("CURRENT")

# get a reference to the crime data frame
df = mapping.ListDataFrames(mxd, "Crime")[0]

# define the layer that will be updated
updateLayer = mapping.ListLayers(mxd, "Crimes2009", df)[0]

# define the layer that will be used to update the properties
sourceLayer = mapping.Layer(r"C:\ArcpyBook\data\BurglariesNoForcedEntry.lyr")

# call the updatelayer() function to update the symbology
mapping.UpdateLayer(df, updateLayer, sourceLayer, "False")

