apt-get install -y python3-dev 
apt-get install -y python3.6-dev
pip3 install numpy
export LD_LIBRARY_PATH=/usr/local/lib:\$LD_LIBRARY_PATH
gdal_version=$(gdalinfo --version | sed "s/GDAL //" | sed "s/, released [0-9][0-9][0-9][0-9]\/[0-9][0-9]\/[0-9][0-9]//")
pip3 install GDAL==$gdal_version