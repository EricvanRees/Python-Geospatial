#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     02/04/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# this script lists all feature classes in a directory.
# returns a list shp files
# a shapefile is a feature class: http://www.spatialtimes.com/2014/06/shapefile-vs-feature-class/

import arcpy

env = r"C:\data\gdal\NE\110m_cultural"
fc = arcpy.ListFeatureClasses()
for i in fc:
    print(i)