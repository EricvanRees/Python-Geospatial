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
# this script prints a number of raster properties

import arcpy

raster = r"C:\data\gdal\srtm_20_04\srtm_20_04.tif"
desc = arcpy.Describe(raster)
spatialref = desc.spatialReference

print "Data type is: " + str(desc.dataType)
print "File path is: " + str(desc.path)
print "File name is " +  str(desc.file)
print "Compression type is " + str(desc.compressionType)
print "Spatial reference is: " + str(spatialref.name)
print "Spatial datatype is: " + str(desc.dataType)
print "Total band count is: " + str(desc.bandCount)
print "Total amount of rows is: " + str(desc.height)
print "Total amount of columns is: " + str(desc.width)

fieldlist = arcpy.ListFields(raster)
i = 0
for field in fieldlist:
    i += 1
    print "field name " + str(i) + " is " + field.name

