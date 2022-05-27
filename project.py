import arcpy
out=r"C:\Users\taohuang\Downloads\20200609nancypaired6.shp-20220526T193845Z-001\20200609nancypaired_15gcp_pj.shp"
out
out=r"C:\Users\taohuang\Downloads\20200609nancypaired6.shp-20220526T193845Z-001\output\20200609nancypaired_15gcp_pj.shp"
#https://pro.arcgis.com/en/pro-app/2.8/arcpy/classes/spatialreference.htm
wkt = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],\
              PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],\
              VERTCS["WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],\
              PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]];\
              -400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;\
              0.001;0.001;IsHighPrecision'
              
wtk
wkt
out_coordinate_system = arcpy.SpatialReference(wkt)
out_coordinate_system = arcpy.SpatialReference(115700)
out_coordinate_system = arcpy.SpatialReference(4326)
out_coordinate_system
arcpy.Project_management("20200609nancypaired_15gcp_index",out,out_coordinate_system)
arcpy.AddField_management("20200609nancypaired_15gcp_pj","lat","DOUBLE")
arcpy.AddField_management("20200609nancypaired_15gcp_pj","lon","DOUBLE")

