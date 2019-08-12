# gdal
cd ~/Downloads
wget http://download.osgeo.org/gdal/2.3.1/gdal-2.3.1.tar.gz
tar xzf gdal-2.3.1.tar.gz
mv ./gdal-2.3.1 ~/gdal-2.3.1
cd ~/gdal-2.3.1
./configure
make
sudo make install
export LD_LIBRARY_PATH=/usr/local/lib:\$LD_LIBRARY_PATH
echo "export LD_LIBRARY_PATH=/usr/local/lib:\$LD_LIBRARY_PATH" >> ~/.profile