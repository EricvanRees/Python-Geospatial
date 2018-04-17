#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     17/04/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''
This recipe will require that you create a feature layer that will serve as a temporary layer, which
will be used with the Select by Location and Select Layer by Attributes tools. The Select by
Location tool will find all burglaries that are within the Edgewood School District and apply a
selection set to these features. The Select Layer by Attributes tool uses the same temporary
feature layer and applies a where clause that finds all burglaries that occurred on a particular
Monday. In addition to this, the tool also specifies that the selection should be a subset of the
currently selected features found by the Select by Location tool. Finally, you'll print the total
number of records that were selected by the combined spatial and attribute query.
'''

# import module
import arcpy

# set the workspace
arcpy.env.workspace = "c:/ArcpyBook/data/CityofSanAntonio.gdb"

# start a try block
try:
    # Create a variable for the query and define the where clause
    qry = '"DOW" = \'Mon\''
    # create a feature layer
    flayer = arcpy.MakeFeatureLayer_management("Burglary", "Burglary_Layer")
    # execute select by location tool to find all burglaries within the Edgewood School District
    arcpy.SelectLayerByLocation_management(flayer, "COMPLETELY_WITHIN", "c:/ArcpyBook/Ch7/EdgewoodSD.shp")
    # Execute the Select Layer by Attributes tool to find all the burglaries that match
    # the query we previously defined in the qry variable
    arcpy.SelectLayerByAttribute_management(flayer, "SUBSET_SELECTION", qry)
    # print the number of records selected
    cnt = arcpy.GetCount_management(flayer)
    print("The total number of selected records is: " + str(cnt))
except Exception as e:
    print(e.message)
