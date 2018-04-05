#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     05/04/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#import module
import arcpy.mapping as mapping, os

#reference currently active map document
mxd = mapping.MapDocument("CURRENT")

# retrieve the crime data frame
df = mapping.ListDataFrames(mxd, "Crime")[0]

# generate DataFrameTime object
dft = df.time

# set current time property to start time property
dft.currentTime = dft.startTime

# start a while loop while current time is less than or equal to end time
while dft.currentTime <= dft.endTime:
    # create a file for each PDF to be created
    # and reset current time property
    fileName = str(dft.currentTime).split(" ")[0] + ".pdf"

    mapping.ExportToPDF(mxd, os.path.join(r"c:\ArcPyBook\Ch2", fileName),df)
    print("Exported " + fileName)
    dft.currentTime = df.time.currentTime + dft.timeStepInterval