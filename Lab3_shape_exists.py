Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
This code helps to see if a specific file is in the data or not. It uses a Boolean value to verify the file's existence.
'''

>>> import arcpy #import ArcPy
>>> from arcpy import env #import environment settings for ArcPy

#choose workspace environment
>>> env.workspace = "C:/Users/PhotonUser/My Files/OneDrive/Files/Data-Lab_3_Exploring_Spatial_Data"

#checks if a file exists in the data
>>> shape_exists = arcpy.Exists("cities.shp")
>>> print shape_exists
True

#output shows capitalization of file name does not matter
>>> shape_exists = arcpy.Exists("CITIES.SHP")
>>> print shape_exists
True
>>> 
