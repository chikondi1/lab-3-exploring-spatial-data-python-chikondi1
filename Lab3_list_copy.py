Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
This code copies the shapefiles imported to ArcMap without changing their names and moves them to the Results folder.
'''

>>> import arcpy #import ArcPy
>>> from arcpy import env #import environment settings for ArcPy

#choose workspace environment
>>> env.workspace = "C:/Users/PhotonUser/Desktop/OneDrive/Files/Data-Lab_3_Exploring_Spatial_Data"

>>> fclist = arcpy.ListFeatureClasses() #create feature class list from the feature classes input in ArcMap

>>> for fc in fclist:
	arcpy.CopyFeatures_management (fc, "/Results/" + fc) #function moves the feature class to the Results folder and keeps its name

	
<Result 'C:/Users/PhotonUser/Desktop/OneDrive/Files/Data-Lab_3_Exploring_Spatial_Data\\\\Results\\amtrak_stations.shp'>
<Result 'C:/Users/PhotonUser/Desktop/OneDrive/Files/Data-Lab_3_Exploring_Spatial_Data\\\\Results\\cities.shp'>
<Result 'C:/Users/PhotonUser/Desktop/OneDrive/Files/Data-Lab_3_Exploring_Spatial_Data\\\\Results\\counties.shp'>
<Result 'C:/Users/PhotonUser/Desktop/OneDrive/Files/Data-Lab_3_Exploring_Spatial_Data\\\\Results\\new_mexico.shp'>
<Result 'C:/Users/PhotonUser/Desktop/OneDrive/Files/Data-Lab_3_Exploring_Spatial_Data\\\\Results\\railroads.shp'>

