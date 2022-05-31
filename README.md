Input data: \20200610_wbs1_macro\gcp\20200609nancypaired_15gcp.csv

I used arcpy.Project_management to project the shp to WGS 1984 (EPSG:4326). Then I used arcpy.AddField_management to add fields. Then I Calculate Geometry. After that I used dbfread to read the dbf into python then used pandas to export to csv.
