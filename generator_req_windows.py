import os

write_str = """"""
with open("requirements.txt", 'r' , encoding="utf8") as f:
    for line in f:
        if not (
            "Fiona" in line or 
            "GDAL" in line or 
            "geopandas" in line or 
            # "opencv" in line or
            "Rtree" in line or 
            "Shapely" in line
            ):
            write_str += line

# write_str += "--index-url http://rd.thinktronltd.com:28181/simple --trusted-host rd.thinktronltd.com\n"
# write_str += "PySaga"

with open("requirements_windows.txt", 'w' , encoding="utf8") as f:
    f.write(write_str)