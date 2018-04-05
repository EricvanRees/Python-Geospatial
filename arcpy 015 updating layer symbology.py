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

# this script uses UpdateLayer() function to update the symbology of a layer
# script runs only in ArcMap as it references currently loaded map data

# import the module
import arcpy.mapping as mapping

# reference currently active map document to a variable
mxd = mapping.MapDocument("CURRENT")

# get a reference to "crime" dataframe
df = mapping.ListDataFrames(mxd, "Crime")[0]

# define the layer that will be updated
updateLayer = mapping.ListLayers(mxd, "Crime Density by School District",df)[0]

# define the layer that will be used to update the symbology
sourceLayer = mapping.Layer(r"C:\ArcpyBook\data\CrimeDensityGradSym.lyr")

# call the UpdateLayer() function to update the symbology
# True is used for updating symbology only, not properties
mapping.UpdateLayer(df, updateLayer, sourceLayer, True)

