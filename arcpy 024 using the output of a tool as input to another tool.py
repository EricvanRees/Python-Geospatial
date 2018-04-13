#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     13/04/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# this recipe shows how
# to obtain the output of a tool and use it as input to another tool.
# script runs inside ArcMap

# import module
import arcpy

# save workspace
arcpy.env.workspace = "c:/ArcpyBook/data/TravisCounty"

# Start a try statement and add variables for the streams, buffered streams layer,
# distance, and schools
try:
    # buffer areas of impact around major roads
    streams = "Streams.shp"
    streamsBuffer = "StreamsBuffer.shp"
    distance = "2640 Feet"
    schools2mile = "Schools.shp"
    schoolsLyrFile = 'Schools2Mile_lyr'
    # execute buffer tool
    arcpy.Buffer_analysis(streams, streamsBuffer,distance,'FULL','ROUND','ALL')
    # create a temporary layer for the schools
    arcpy.MakeFeatureLayer_management(schools2mile, schoolsLyrFile)
    # select all school within a half mile of a stream
    arcpy.SelectLayerByLocation_management(schoolsLyrFile, 'intersect', streamsBuffer)
#add except block to catch errors
except Exception as e:
    print(e.message)
