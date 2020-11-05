Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
This code creates an output of each of the files imported to ArcMap and what type of file it is. 
'''

>>> import arcpy #import ArcPy
>>> from arcpy import env #import environment settings for ArcPy

#choose workspace environment
>>> env.workspace = "C:/Users/PhotonUser/Desktop/OneDrive/Files/Data-Lab_3_Exploring_Spatial_Data"

>>> fclist = arcpy.ListFeatureClasses() #create feature class list from the feature classes input in ArcMap

>>> print fclist #output is a list of each of the feature classes
[u'amtrak_stations.shp', u'cities.shp', u'counties.shp', u'new_mexico.shp', u'railroads.shp'] #u means that the string is represented as Unicode, which can save memory 

>>> for fc in fclist: #function that writes a code to describe the type of file each feature class is
	fcdescribe = arcpy.Describe(fc)
	print "Name: " + fcdescribe.name #name of feature class
	print "Data type: " + fcdescribe.dataType #file type of each feature class

#output is of each file and the file type.	
'''
Name: amtrak_stations.shp
Data type: ShapeFile
Name: cities.shp
Data type: ShapeFile
Name: counties.shp
Data type: ShapeFile
Name: new_mexico.shp
Data type: ShapeFile
Name: railroads.shp
Data type: ShapeFile
'''

