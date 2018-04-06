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

'''In this script, we'll examine how you can use the
findAndReplaceWorkspacePaths() method in the MapDocument class to perform
global find and replace operations in the layers and tables of a map document.
'''

# import the module
import arcpy.mapping as mapping

# reference map document file
mxd = mapping.MapDocument(r"c:\ArcpyBook\Ch3\Crime_BrokenDataLinks.mxd")

# fix the source path for each data source in map document
# first parameter is old path, second parameter is new path
mxd.findAndReplaceWorkspacePaths(r"C:\ArcpyBook\Ch3\Data\OldData\CityOfSanAntonio.gdb", r"C:\ArcpyBook\Data\CityOfSanAntonio.gdb")

# save the results to a new mxd file
mxd.saveACopy(r"C:\ArcpyBook\Ch3\Crime_DataLinksFixed.mxd")
print "New map document created"

