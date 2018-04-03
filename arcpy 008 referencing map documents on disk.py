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

#import modules
import arcpy.mapping as mapping

#reference copy of map document
mxd = mapping.MapDocument("c:/ArcPyBook/Ch2/crime_copy.mxd")

#print title of map document, prints "Crime Project"
print(mxd.title)
