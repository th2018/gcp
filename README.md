EXAMPLE 1:
Input data: \20200610_wbs1_macro\gcp\20200609nancypaired_15gcp.csv

In ArcMap, I added 20200609nancypaired_15gcp_index.csv then exported it to .shp. I used arcpy.Project_management (project.py) to project the shp to WGS 1984 (EPSG:4326). Then I used arcpy.AddField_management to add fields. Then I calculated geometry. After that I used dbfread to read the dbf into python then used pandas to export to csv (read_pdf_ro_csv.ipynb).

EXAMPLE 2:
Input data:  C:\Users\taohuang\Downloads\USDA_ARS-20220627T203346Z-001\USDA_ARS\RTK-for-Tao\2018\rcew ltvr\rcew-ltvr\rcew-ltvr-los1\LOS4-5.shp\uavgcp.shp
Step 1: AddField.py
Step 2: I calculated geometry of x,y,z.
Step 3: I used arcpy.Project_management (project.py) to project the shp to WGS 1984 (EPSG:4326). Then I calculated geometry of lon,lat,ele.
Step 4: After that I used dbfread to read the dbf into python then used pandas to export to csv.
