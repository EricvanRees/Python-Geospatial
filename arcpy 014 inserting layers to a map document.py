#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     04/04/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#------------------------------------------------------------------------------

# this script uses the InsertLayer() function to add a layer to a map doc
# this function provides more control to where a layer is added within a data frame
# compared to AddLayer() function. InsertLayer() uses a reference layer that places
# the added layer below or above the reference layer.
# script only runs in ArcMap as it references currently loaded map data

# importing the modules
import arcpy.mapping as mapping

# reference currently active document
mxd = mapping.MapDocument("CURRENT")

# reference the crime data frame
df = mapping.ListDataFrames(mxd, "Crime")[0]

# define reference layer
refLayer = mapping.ListLayers(mxd, "Burglaries*", df)[0]

# define the layer to be inserted relative to the reference layer
insertLayer = mapping.Layer(r"C:\ArcpyBook\data\CityOfSanAntonio.gdb\Crimes2009")

# insert the layer into the dataframe
mapping.InsertLayer(df, refLayer, insertLayer, "BEFORE")


