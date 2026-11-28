# Predicción del precio de la vivienda · Idealista18

Proyecto final de **Aprendizaje Automático** (UFV Madrid).

**Autores:** Javier Alacio Vega y Javier Gaudencio Ortega Lucena

Predecimos el precio de venta de viviendas de **Madrid, Barcelona y Valencia** (anuncios de Idealista de 2018) a partir de sus características: superficie, habitaciones, baños, extras (ascensor, terraza, piscina…), antigüedad, distancia al centro y al metro, y ubicación (latitud y longitud).

Tratamos el problema de dos formas:

- **Regresión:** predecir el precio en euros, con una regresión lineal como referencia y un perceptrón multicapa (MLP) en PyTorch. Los hiperparámetros del MLP se optimizan con un **algoritmo genético**.
- **Clasificación:** predecir si la vivienda está en el tramo de precio **bajo, medio o alto**, con regresión logística y un MLP.

## Resultados principales (conjunto de prueba)

| Modelo | MAE (€) | R² (euros) | R² (log-precio) |
|---|---|---|---|
| Regresión lineal, sin ubicación | 86.209 | 0,786 | 0,809 |
| Regresión lineal, con ubicación | 80.104 | 0,805 | 0,839 |
| MLP, sin ubicación | 71.858 | 0,853 | 0,867 |
| MLP, con ubicación | 65.791 | 0,865 | 0,894 |
| MLP, con ubicación y algoritmo genético | 65.056 | 0,861 | 0,896 |

| Clasificación por tramos | Accuracy en prueba |
|---|---|
| Regresión logística | 0,779 |
| MLP | 0,820 |

Las conclusiones y limitaciones están al final de `notebooks/entrega3.ipynb`.

## Estructura del proyecto

```
PROYECTO FINAL/
├── data/
│   └── idealista18_venta_3ciudades.csv   # datos ya preparados (ver más abajo)
├── figuras/               # gráficas que guardan los notebooks
├── notebooks/
│   ├── entrega2.ipynb     # Entrega 2: EDA, preprocesado, regresión lineal y MLP
│   └── entrega3.ipynb     # Entrega 3 (notebook final y completo)
├── resultados/            # tablas de resultados en prueba (.csv)
├── src/
│   └── convertir_datos.py # convierte los .rda de Idealista18 en un único CSV
├── requirements.txt       # librerías necesarias
└── README.md
```

El notebook **`entrega3.ipynb` es el trabajo final**. Incluye todo lo de la Entrega 2 y añade la ubicación, el algoritmo genético, la clasificación por tramos y la evaluación final en prueba.

## Datos

Usamos **Idealista18**, publicado en el paquete de R [idealista18](https://github.com/paezha/idealista18) con licencia **ODbL-1.0** (Open Database License), que permite redistribuir los datos citando la fuente.

El repositorio ya incluye el CSV que leen los notebooks, así que **no hace falta descargar nada**:

- `data/idealista18_venta_3ciudades.csv`: 189.923 anuncios de venta de 2018 (Madrid, Barcelona y Valencia) con 44 columnas. Es la unión de los tres conjuntos de venta originales, con una columna `CITY` que indica la ciudad.

Este CSV lo generamos con `src/convertir_datos.py`. Para volver a crearlo desde los archivos originales:

1. Descargar `Madrid_Sale.rda`, `Barcelona_Sale.rda` y `Valencia_Sale.rda` del paquete idealista18 y guardarlos en la carpeta `data/`.
2. Desde la carpeta del proyecto, ejecutar:

   ```
   python src/convertir_datos.py
   ```

## Cómo ejecutarlo

Desde la carpeta del proyecto:

```
python -m venv .venv
.venv\Scripts\activate          # en Windows (en Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt
```

Después se abre `notebooks/entrega3.ipynb` (en VS Code con el entorno `.venv`, o con `jupyter notebook`) y se ejecuta entero (*Restart & Run All*). Los notebooks deben ejecutarse desde la carpeta `notebooks/`, porque leen los datos con la ruta `../data/`.

- La ejecución completa tarda **unos 10 minutos** en un ordenador normal (sin GPU). La parte más lenta es el algoritmo genético (sección 6), que entrena unas 30 redes.
- Las semillas están fijadas (`random_state=42`, `torch.manual_seed(42)`, `random.seed(42)`), así que los resultados deberían salir iguales en cada ejecución.
