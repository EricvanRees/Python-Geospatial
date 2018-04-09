#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     08/04/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''In this recipe, you will learn how to recursively search directories for map document files, find
any broken data sources within these map documents, and write the names of the broken
data layers to a file.'''

# import the module
import arcpy.mapping as mapping, os

# open a file for writing broken layer names
f = open('BrokenDataList.txt', 'w')

# use os.walk() method with a path and a for loop for walking directory tree
for root,dirs,files in os.walk("C:\ArcPyBook"):
    # create a second for loop that loops through all files returned and
    # create a new filename variable
    for name in files:
        filename = os.path.join(root, name)
        # test the file extension to see if it is a
        # map document file. If so, create a new map document object instance using the path,
        # write the map document name, get a list of broken data sources, loop through each
        # of the broken data sources, and write to the file
        if ".mxd" in filename:
            mxd = mapping.MapDocument(filename)
            f.write("MXD: " + filename + "\n")
            brknList = mapping.ListBrokenDataSources(mxd)
            for brknItem in brknList:
                "Broken data item: " + brknItem.name + " in " + filename
                f.write("\t" + brknItem.name + "\n")
print("All Done")
f.close()