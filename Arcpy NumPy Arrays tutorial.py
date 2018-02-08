###############################################################################################
### Script for NumPy tutorial for Eric Pimpler's website www.geospatialtraining.com
### It consists of creating a NumPy array from a shapefile and performing basic data operations
### with it.
### created 6/4/2017 by Eric van Rees
###############################################################################################

import arcpy
import numpy
from operator import itemgetter, attrgetter, methodcaller

input = "C:/data/Creating-maps-in-R-master/data/londonBoroughs.shp"
arr = arcpy.da.TableToNumPyArray(input, ('name', 'Pop_2001', 'PopDensity', 'AREA', 'PERIMETER'))

# List column values by header name:

print 'the Population 2001 column contains the followning values: '
print arr['Pop_2001']
print '\n'

# Sum the total population of 2001, total area size and mean area size:

a = arr["Pop_2001"].sum()
b = arr["AREA"].sum()
mas = arr["AREA"].mean()
print 'The total population of 2001 is {}.\n'.format(a)
print 'The total area size is {}.\n'.format(b)
print 'The mean area size is {}.\n'.format(mas)

# Sum the population for the Westminster area

c = arr[arr['name'] == "Westminster"]['Pop_2001'].sum()
print 'The total population of the Westminster area is {}. \n'.format(c)

# Calculate mean value for population density:

mpopden = arr['PopDensity'].mean()
print 'The mean (rounded) population density is {}.\n'.format(int(mpopden))


#access one particular cell value in numpy array:
d = arr[1][4]
print 'The perimeter value for Richmond upon Thames is {}\n'.format(d)

# Print the column names of the numpy array:
colnames = arr.dtype.names
print 'The Numpy array has the following column names:  \n' + str(colnames)
print '\n'

# Accessing all values of one specific column, for example population density:

for i in arr:
    print i[2]

print '\n'

# "select by attribute": print all Borough names where population density exceeds 3000:
print'The following Boroughs have a population density that exceeds 8000: \n'
for t in arr:
    if t[2] > 8000:
        print t[0]

print '\n'

# The same query notated as a list comprehension:

m = [t[0] for t in arr if t[2] > 8000]
print m
print '\n'

# Numpy array slicing for individual rows.
# The following code returns row nrs. 1 to 4:

subarray = arr[1:5]
print subarray
print '\n'

# selecting elements from subarray, for example returning Borough names where population density > 2000

for i in subarray:
    if subarray[2] > 2000:
        print b[0]

# convert 2D Numpy array to 2D Numpy matrix - The main advantage of numpy matrices
# is that they provide a convenient notation for matrix multiplication:

matrix = numpy.asmatrix(arr)
print matrix
print '\n'

# Sort the new matrix by perimeter column - output shows lowest values first:

z = numpy.sort(matrix, order='PERIMETER')
print z


