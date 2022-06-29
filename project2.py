import arcpy

out=r"C:\Users\taohuang\Downloads\USDA_ARS-20220627T203346Z-001\USDA_ARS\RTK-for-Tao\2018\rcew ltvr\rcew-ltvr\rcew-ltvr-los1\LOS4-5.shp\uavgcp2.shp"

out_coordinate_system = arcpy.SpatialReference(4326)

arcpy.Project_management("uavgcp",out,out_coordinate_system)
