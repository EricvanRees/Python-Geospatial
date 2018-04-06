#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     06/04/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# import module
import arcpy.mapping as mapping

# reference map document file
mxd = mapping.MapDocument(r"c:\ArcpyBook\Ch3\Crime_BrokenDataLinks.mxd")

# get a list of broken data sources
listBrokenDS = mapping.ListBrokenDataSources(mxd)

# iterate over the list and print out the layer names
for i in listBrokenDS:
    print i.name

