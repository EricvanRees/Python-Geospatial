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

# this script uses a definition expression to the change the map
# extent in ArcMap. script only runs in ArcMap as it uses loaded map documents and
# map view

#import module
import arcpy.mapping as mapping

#reference current active map document
mxd = mapping.MapDocument("CURRENT")

# create a for loop that will loop through all
# data frames in map document

for df in mapping.ListDataFrames(mxd):
    # find the data frame called "Crime" and a
    # specific layer we?ll apply the definition query against
    if df.name == "Crime":
        layers = mapping.ListLayers(mxd, 'Crime Density by School District', df)
        # create a for loop to loop through the layers
        # in the for loop, create a definition query
        # and set the new extent for the data frame.
        # after running script, map view only shows the
        # features matching the defintion query
        for layer in layers:
            query = '"NAME" =  \'Lackland ISD\''
            layer.definitionQuery = query
            df.extent = layer.getExtent()

