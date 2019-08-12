import os

package_names = [
    "Fiona", 
    "GDAL",  
    "Rtree", 
    "Shapely", 
    "geopandas",
    # "SplittedImage", 
    # "PySaga"
]

write_str = """"""
with open("requirements.txt", 'r' , encoding="utf8") as f:
    for line in f:
        if sum([pn in line for pn in package_names]) == 0:
            write_str += line
            
write_str += "--index-url http://rd.thinktronltd.com:28181/simple --trusted-host rd.thinktronltd.com\n"
for pn in package_names:
    write_str += pn + "\n"

with open("requirements_windows.txt", 'w' , encoding="utf8") as f:
    f.write(write_str)