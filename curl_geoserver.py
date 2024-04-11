# -*- coding: utf-8 -*-
__author__ = 'JosefinaOtero'
import os
import sys
import time
import glob
from datetime import datetime
import logging
import subprocess


# lista de nombres de capas a subir
#"path a las carpeta donde estan los mosaicos"
path_mosaicos = '/mosaicos/' #"path donde estan las carpetas de las piramides generadas"
#------------------------------------------------------------------------------------------------------------------
#crear las piramides   
lista_layers = glob.glob(os.path.join(path_mosaicos, '*.tif'))
#lista_layers = glob.glob(os.path.join(carpeta_txt, '*.txt'))
# for layer in lista_layers:
#     layername = layer.split('\\')[1][:-4]
#     print(layername)
# link dentro del geoserver donde se cuardan las piramides deszipeadas

#from leerPath import urlgeoserver
import urllib.parse

urlgeoserver = 'xxxxxx'

#link del geoserver

#espacio de trabajo 
workspace="mosaicos" 

##geoserver credentials
user="xx"
password="xx"
geoserverurl="https://xxxx"

#---------------------------------------------------------------------
#definicion del archivo log----------------------------------------
FILENAME_LOGGING = 'log_geoserver.txt'
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.addHandler(logging.FileHandler(FILENAME_LOGGING))

#----------------------------------------------
hoy = datetime.now()
logger.info("---------------------------------------------------------------------------------")
logger.info("inicio del proceso de subir piramides al geoserver")
logger.info("---------------------------------------------------------------------------------")

logger.info(hoy)
#------------------------------------------------------------------------

for layer in lista_layers:
    layername = layer.split('\\')[1][:-4]
   # print(layername)
    urlGeo = ('"'+ urlgeoserver +'/'+ layername +'"')
    #print(urlGeo)
    urlWorkSpace =( '"'+ geoserverurl + '/rest/workspaces/'+ workspace + '/coveragestores/' + layername +'/external.imagepyramid"')
    curl_capa ='E:/servidorImpactar/curl/curl.exe -v -u ' + user +':' + password + ' -XPUT -H "Content-type: text/plain" -d ' + urlGeo +' '+ urlWorkSpace 
    print(curl_capa)
        

    try: 
     logger.info(subprocess.check_output(curl_capa, shell=True) )
     logger.info("se subio correctamente " +layername ) 
    except: 
     logger.info("NO se subio correctamente "+layername)
      
    logger.info(os.system(curl_capa))
    
    time.sleep(30)


fin =   datetime.now()      
duracion = str(fin - hoy)
logger.info("Duracion del proceso: " + duracion)
logger.info("---------------------------------------------------------------------------------")
logger.info("FIN del proceso")
logger.info("---------------------------------------------------------------------------------")
