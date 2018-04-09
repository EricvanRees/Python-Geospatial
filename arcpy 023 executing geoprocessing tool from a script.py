#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     08/04/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# this script executes a geoprocessing tool from a script

# import module
import arcpy

# reference input feature class
in_features = "c:/ArcpyBook/data/CityOfSanAntonio.gdb/Burglary"

# create a variable that references the layer to be used for the clip:
clip_features = "c:/ArcpyBook/Ch5/EdgewoodSD.shp"

# create a variable that references the output feature class:
out_feature_class = "c:/ArcpyBook/Ch5/ClpBurglary.shp"

# execute the Clip tool from the Analysis Tools toolbox:
arcpy.Clip_analysis(in_features,clip_features, out_feature_class)

