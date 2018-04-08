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

'''The Layer and TableView objects also have methods that can be
used to fix broken data links at the individual object level rather than working on all datasets in
a map document file. This recipe discusses the repairing of Layer and TableView objects.

In this recipe, you'll write a script that changes the workspace path and workspace
type for a single layer. The replaceDataSource() method is available for the Layer and
TableView classes. In the case of a layer, it can either be in a map document or layer file. For
a table, it can refer to the map document only, since TableView objects can't be contained
inside a layer file.

Open c:\ArcpyBook\Ch3\Crime_DataLinksLayer.mxd in ArcMap. The Crime data
frame contains a layer called Burglary, which is a feature class in the CityOfSanAntonio
file geodatabase. You're going to replace this feature class with a shapefile layer containing
the same data:
'''

# importing module
import arcpy.mapping as mapping

# reference map doc file:
mxd = mapping.MapDocument(r"c:\ArcpyBook\Ch3\Crime_DataLinksLayer.mxd")

# reference to the crime data frame:
df = mapping.ListDataFrames(mxd, "Crime")[0]

# find the "burglary" layer and store it in a variable
lyr = mapping.ListLayers(mxd,"Burglary",df)[0]

# Call the replaceDataSource() method on the Layer object and pass the path
# to the shapefile
lyr.replaceDataSource(r"c:\ArcpyBook\data","SHAPEFILE_WORKSPACE","Burglaries_2009")

#Save the results to a new map document file
mxd.saveACopy(r"c:\ArcpyBook\Ch3\Crime_DataLinksNewLayer.mxd")
print"new mxd created"


