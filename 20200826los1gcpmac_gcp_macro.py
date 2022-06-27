import arcpy

out=r"C:\Users\taohuang\Downloads\USDA_ARS-20220627T203346Z-001\USDA_ARS\RTK-for-Tao\2020\ltvr_rtk_2020\20200826los1gcpmac.shp\out\gcp_macro_pj.shp"

out_coordinate_system = arcpy.SpatialReference(4326)

arcpy.Project_management("gcp macro",out,out_coordinate_system)

arcpy.AddField_management("gcp_macro_pj","lat","DOUBLE")
arcpy.AddField_management("gcp_macro_pj","lon","DOUBLE")
arcpy.AddField_management("gcp_macro_pj","ele","DOUBLE")

