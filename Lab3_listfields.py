Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
This code moves files into the NM.gdb geodatabase workspace. It also outputs the fieldlist of the cities.shp shapefile and the type of file each of the categories is. 
'''

>>> import arcpy #import ArcPy
>>> from arcpy import env #import environment settings for ArcPy
>>> env.overwriteOutput = True #allows for code to overwrite files
#choose workspace environment
>>> env.workspace = "C:/Users/PhotonUser/Desktop/OneDrive/Files/Data-Lab_3_Exploring_Spatial_Data"
>>> fclist = arcpy.ListFeatureClasses() #create feature class list from the feature classes input in ArcMap
>>> for fc in fclist:
	fcdesc = arcpy.Describe(fc) 
	#function moves the feature class to the Results folder under the New Mexico geodatabase
	arcpy.CopyFeatures_management(fc, "C:/Users/PhotonUser/My Files/OneDrive/Files/Data-Lab_3_Exploring_Spatial_Data/Results/NM.gdb/" + fcdesc.basename) 

#filepaths of each output
<Result 'C:\\Users\\PhotonUser\\My Files\\OneDrive\\Files\\Data-Lab_3_Exploring_Spatial_Data\\Results\\NM.gdb\\amtrak_stations'>
<Result 'C:\\Users\\PhotonUser\\My Files\\OneDrive\\Files\\Data-Lab_3_Exploring_Spatial_Data\\Results\\NM.gdb\\cities'>
<Result 'C:\\Users\\PhotonUser\\My Files\\OneDrive\\Files\\Data-Lab_3_Exploring_Spatial_Data\\Results\\NM.gdb\\counties'>
<Result 'C:\\Users\\PhotonUser\\My Files\\OneDrive\\Files\\Data-Lab_3_Exploring_Spatial_Data\\Results\\NM.gdb\\new_mexico'>
<Result 'C:\\Users\\PhotonUser\\My Files\\OneDrive\\Files\\Data-Lab_3_Exploring_Spatial_Data\\Results\\NM.gdb\\railroads'>

>>> import arcpy #import ArcPy
>>> from arcpy import env #import environment settings for ArcPy
>>> env.overwriteOutput = True #allows for code to overwrite files
#choose workspace environment
>>> env.workspace = "C:/Users/PhotonUser/My Files/OneDrive/Files/Data-Lab_3_Exploring_Spatial_Data/"
>>> fieldlist = arcpy.ListFields("cities.shp") #fieldlist is displayed from the cities.shp shapefile
>>> for field in fieldlist: #function outputs category data in the cities.shp shapefile and what type of file it is
	print field.name + " " + field.type #displays the field name and the file type

'''	
FID OID
Shape Geometry
CITIESX020 Double
FEATURE String
NAME String
POP_RANGE String
POP_2000 Integer
FIPS55 String
COUNTY String
FIPS String
STATE String
STATE_FIPS String
DISPLAY SmallInteger
'''

