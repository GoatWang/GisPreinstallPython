import os
import subprocess

write_str = ""
cmd = 'gdalinfo --version | sed "s/GDAL //" | sed "s/, released [0-9][0-9][0-9][0-9]\/[0-9][0-9]\/[0-9][0-9]//"'
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
gdal_version, err = process.communicate()

with open("requirements.txt", 'r' , encoding="utf8") as f:
    for line in f:
        if not ("GDAL" in line):
            write_str += line

write_str += "GDAL==" + gdal_version
# write_str += "--index-url http://rd.thinktronltd.com:28181/simple --trusted-host rd.thinktronltd.com\n"
# write_str += "PySaga"

with open("requirements_linux.txt", 'w' , encoding="utf8") as f:
    f.write(write_str)