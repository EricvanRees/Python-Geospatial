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
#this script describes the spatial reference name and type of a shp file

import arcpy

desc = arcpy.Describe(r"C:\data\gdal\NE\110m_cultural\ne_110m_admin_1_states_provinces_shp.shp")
SR = desc.spatialReference
print "Name: \t\t" + SR.name
print "Type: \t\t" + SR.type