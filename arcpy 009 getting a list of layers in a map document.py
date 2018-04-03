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
# this script is supposed to be run in ArcGIS, not in an IDLE
# script references map document and prints a list of all layers

# load module
import arcpy.mapping as mapping

# reference currently active map document and assign reference to a variable
mxd = mapping.MapDocument("CURRENT")

# call the ListLayers() fuction and a pass a reference to the map document
layers = mapping.ListLayers(mxd)

# start a for loop and print out the name of earch layer in the map document
for lyr in layers:
    print(lyr.name)