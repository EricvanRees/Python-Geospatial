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
# this script lists all fields of a shapefile, type and length

import arcpy

shp = r"C:\data\gdal\NE\110m_cultural\ne_110m_admin_1_states_provinces_shp.shp"
fields = arcpy.ListFields(shp)
for field in fields:
    print field.name, field.type, field.length