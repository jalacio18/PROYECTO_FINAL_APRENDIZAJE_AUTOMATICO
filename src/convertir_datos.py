"""Convierte los archivos .rda de Idealista18 (Madrid, Barcelona y Valencia)
en un único CSV con una columna CITY.

Uso (desde la carpeta del proyecto):
    python src/convertir_datos.py
Entrada : data/Madrid_Sale.rda, data/Barcelona_Sale.rda, data/Valencia_Sale.rda
Salida  : data/idealista18_venta_3ciudades.csv
"""
import warnings
from pathlib import Path

import pandas as pd
import rdata

warnings.filterwarnings("ignore")   # rdata avisa de clases geográficas que no necesitamos

DATA = Path("data")
CIUDADES = ["Madrid", "Barcelona", "Valencia"]

tablas = []
for ciudad in CIUDADES:
    objetos = rdata.read_rda(DATA / f"{ciudad}_Sale.rda")
    tabla = list(objetos.values())[0].drop(columns="geometry")   # ya hay LONGITUDE y LATITUDE
    tabla["CITY"] = ciudad
    tabla["ASSETID"] = tabla["ASSETID"].astype(str)
    print(ciudad, tabla.shape)
    tablas.append(tabla)

total = pd.concat(tablas, ignore_index=True)
total.to_csv(DATA / "idealista18_venta_3ciudades.csv", index=False)
print("Guardado:", total.shape)