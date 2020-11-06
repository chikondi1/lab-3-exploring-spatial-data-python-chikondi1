#selects the shapefile 
myshape = arcpy.Describe("C:/Users/PhotonUser/Desktop/OneDrive/Files/Data-Lab_3_Exploring_Spatial_Data/cities.shp")
myshape.dataType #displays what type of file cities.shp is
u'ShapeFile'
mylayer = arcpy.Describe("cities")
mylayer.dataType #displays what type of layer cities.shp is
u'FeatureLayer'
mylayer.datasetType
mylayer.catalogPath #displays the file path of the shapefile
u'C:/Users/PhotonUser/Desktop/OneDrive/Files/Data-Lab_3_Exploring_Spatial_Data/cities.shp'
mylayer.basename #displays the file's basename
u'cities'
mylayer.file #displays the file's name
u'cities.shp'
mylayer.isVersioned #This shows if the dataset is versioned or not
False
mylayer.shapeType #displays what type of shapes are displayed in the shape file.
u'Point'
mylayer.spatialReference #reference value of the object
<geoprocessing spatial reference object object at Ox195DBOF8>
mylayer.spatialReference.name #Shows what geographic coordinate system the data is from
u'GCS_North_American_1983'
mylayer.spatialReference.type #Shows what type of GCS it is
u'Geographic'
mylayer.spatialReference.domain #Output lists the smallest and largest x and y coordinates of the data
'-400 -400 400 400'

