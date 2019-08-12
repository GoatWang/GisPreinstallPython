# Introduction
Because Gis package for python generally can not be installed directly through pip. As a result this repo list the installation source for windows. This Repo contains two followings file:
1. README.md: list all frequently used gis python package. Its all from this [website](https://www.lfd.uci.edu/~gohlke/pythonlibs/)
2. generator_req_windows.py: because all this file cannot be installed from pip server, we should download it by hands and change our requirements.txt not to install this file again. This py file can help you to generator new reqirements.txt file. 
3. generator_req_windows_pip_server.py: install from self-built pip server
4. generator_req_linux.py: inthe linux system, you should first install gdal in the system, then install GDAL with same versiion with the sys's GDAL.


# Preinstlall
1. [GDAL](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal)
1. [Shapely](https://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely)
1. [Fiona](https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona):
1. [Rtree](https://www.lfd.uci.edu/~gohlke/pythonlibs/#rtree)
1. [geopandas](https://www.lfd.uci.edu/~gohlke/pythonlibs/#geopandas)

# Or install from self built pip server (Thinktron Use Only)
```
pip install -U --index-url http://192.168.0.167:28181/simple --trusted-host 192.168.0.167 <pickage_name|fiona gdal, geopandas, pysaga, rtree, shapely, splittedimage>
```



<!-- 1. SplittedImage: ```pip install -U --index-url http://192.168.0.167:28181/simple --trusted-host 192.168.0.167 SplittedImage``` -->
