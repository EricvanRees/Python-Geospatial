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

'''You can automate the process of updating your datasets to a different
format with MapDocument.replaceWorkspaces(). MapDocument.replaceWorkspaces() is similar to
MapDocument.findAndReplaceWorkspacePaths(), but it also allows you to switch from one
workspace type to another. In this recipe, we'll use MapDocument.replaceWorkspaces()
to switch our data source from a file geodatabase to a personal geodatabase.
'''

# import module
import arcpy.mapping as mapping

# reference map document file
mxd = mapping.MapDocument(r"c:\ArcpyBook\Ch3\Crime_DataLinksFixed.mxd")

# Call the replaceWorkspaces() method and pass in old and new geodatabase type
mxd.replaceWorkspaces(r"c:\ArcpyBook\data\CityOfSanAntonio.gdb", "FILEGDB_WORKSPACE",
                     r"c:\ArcpyBook\New_Data\CityOfSanAntonio_Personal.mdb", "ACCESS_WORKSPACE")
print "Finished replacing workspaces"