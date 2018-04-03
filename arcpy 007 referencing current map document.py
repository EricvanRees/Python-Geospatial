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
# this script accesses a map document loaded in ArcMap. This script does not work when
# running from an IDLE as it rerefences active map documents in ArcMap

#import module and assign it it to a variable called mapping to save space
import arcpy.mapping as mapping

#reference currently active map document and assign it to a variable
mxd = mapping.MapDocument("CURRENT")

# set a title for map document
mxd.title = "Crime Project"

# save a copy of map document using saveACopy() method
mxd.saveACopy("c:/ArcPyBook/Ch2/crime_copy.mxd")


