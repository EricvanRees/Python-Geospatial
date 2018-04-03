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

# this script restricts the list of layers using a wildcard
# and a specific data frame. Only works with inside of ArcGIS Desktop

#import the module
import arcpy.mapping as mapping

# reference currently active map document
mxd = mapping.MapDocument("CURRENT")

# get a list of dataframes and search for specific dataframe names "disputed areas"
for df in mapping.ListDataFrames(mxd):
    if df.name == "Disputed areas":
        # call the listlayers function, pass a reference to the map doc,
        # a wildcard to restrict the search, and the dataframe found to
        # restrict the search
        layers = mapping.ListLayers(mxd, "ne*", df)
        # start a for loop and print out the name of each layer
        for layer in layers:
            print(layer.name)
