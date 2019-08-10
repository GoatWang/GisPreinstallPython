# Introduction
Because Gis package for python generally can not be installed directly through pip. As a result this repo list the installation source for windows. This Repo contains two followings file:
1. README.md: list all frequently used gis python package. Its all from this [website](https://www.lfd.uci.edu/~gohlke/pythonlibs/)
2. generator_req.py: because all this file cannot be installed from pip server, we should download it by hands and change our requirements.txt not to install this file again. This py file can help you to generator new reqirements.txt file. 
3. generator_req_pip_server.py: install from self-built pip server

# Preinstlall
1. [gdal](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal): [Downlaod](https://download.lfd.uci.edu/pythonlibs/t4jqbe6o/GDAL-3.0.0-cp36-cp36m-win_amd64.whl)
1. [shapely](https://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely): [Downlaod](https://download.lfd.uci.edu/pythonlibs/t4jqbe6o/Shapely-1.6.4.post2-cp36-cp36m-win_amd64.whl)
1. [fiona](https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona):  [Downlaod](https://download.lfd.uci.edu/pythonlibs/t4jqbe6o/Fiona-1.8.6-cp36-cp36m-win_amd64.whl)
1. [Rtree](https://www.lfd.uci.edu/~gohlke/pythonlibs/#rtree): [Downlaod](https://download.lfd.uci.edu/pythonlibs/t4jqbe6o/Rtree-0.8.3-cp36-cp36m-win_amd64.whl)
1. [geopandas](https://www.lfd.uci.edu/~gohlke/pythonlibs/#geopandas): [Downlaod](https://download.lfd.uci.edu/pythonlibs/t4jqbe6o/geopandas-0.5.0-py2.py3-none-any.whl)

# Or install from self built pip server (Thinktron Use Only)
```
pip install -U --index-url http://192.168.0.167:28181/simple --trusted-host 192.168.0.167 <pickage_name|fiona gdal, geopandas, pysaga, rtree, shapely, splittedimage>
```



<!-- 1. SplittedImage: ```pip install -U --index-url http://192.168.0.167:28181/simple --trusted-host 192.168.0.167 SplittedImage``` -->
