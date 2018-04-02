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
# this script describes some attributes of a shapefile

import arcpy

desc = arcpy.Describe(r"C:\data\gdal\NE\110m_cultural\ne_110m_admin_1_states_provinces_shp.shp")

print "Feature Type is: " + desc.featureType
print "Geometry is m-value enabled: " + str(desc.hasM)
print "Geometry is z-value enabled: " + str(desc.hasZ)
print "Geometry has spatial index: " + str(desc.hasSpatialIndex)
print "Name of Shapefield is: " + desc.ShapeFieldName
print "Shape type is: " + desc.shapeType
