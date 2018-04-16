#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Eric
#
# Created:     16/04/2018
# Copyright:   (c) Eric 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''
In this recipe, you'll learn how to construct valid query syntax and understand the nuances of how
different data types alter the syntax as well as some Python-specific constructs.
'''

# import module
import arcpy

'''
If you're working with data from a personal geodatabase, the
field names will need to be enclosed by square brackets instead of double quotes, as shown
in the following code example. This can certainly leads to confusion for script developers:
qry = [SVCAREA] = 'North'

Quotes along with a number of other characters must be escaped with a forward slash
followed by the character being escaped. In this case, the escape sequence would be \' as
shown in the following steps:

qry = "SVCAREA" = \'North\'

Finally, the entire query statement should be enclosed with quotes:
qry = '"SVCAREA" = \'North\''

Wildcard characters, including % and _, can also be used for shapefiles, file geodatabases,
and ArcSDE geodatabases. These include % that represents any number of characters. The
LIKE operator is often used with wildcard characters to perform partial string matching. For
example, the following query would find all records with a service area that begins with N and
has any number of characters after it:

qry = '"SVCAREA" LIKE \'N%\''
'''

# create query and store it in a variable
qry = '"SVCAREA" = \'North\''


