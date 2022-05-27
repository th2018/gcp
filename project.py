import arcpy


out=r"C:\Users\taohuang\Downloads\20200609nancypaired6.shp-20220526T193845Z-001\output\20200609nancypaired_15gcp_pj.shp"


out_coordinate_system = arcpy.SpatialReference(4326)


arcpy.Project_management("20200609nancypaired_15gcp_index",out,out_coordinate_system)
arcpy.AddField_management("20200609nancypaired_15gcp_pj","lat","DOUBLE")
arcpy.AddField_management("20200609nancypaired_15gcp_pj","lon","DOUBLE")

