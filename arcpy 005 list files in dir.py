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
# this script lists all files in a directory

import arcpy

arcpy.env.workspace = r"c:\data\gdal\NE\110m_cultural"
files = arcpy.ListFiles("")
for file in files:
    print(file)