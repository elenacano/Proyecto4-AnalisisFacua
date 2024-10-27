# Proyecto4-AnalisisFacua

![Descripción de la imagen](imagenes/img1.jpeg)

Este proyecto está diseñado para recopilar, almacenar, analizar y visualizar datos de precios de productos en diferentes supermercados de España a partir de la web de FACUA. Una vez obtenidos los datos y almacenados en una base de datos se procederá al análisis de los mimsos. Se busca comparar precios, observar que productos presentan mayores aumentos o caida de precios, que días suelen presentarse estas caidas y aumentos, cuales son los productos más baratos en cada supermercado y otras consultas más de interés.


## Estructura del Proyecto

Este proyecto consta de cuatro etapas, cada una en un cuaderno de Jupyter que documenta su implementación:

1. **Scraping de Datos `(1-scrapeo.ipynb)`**: 

    - Extracción de datos de precios y productos desde la web de FACUA usando Selenium y Beautiful Soup.
    
    - Generación de archivos CSV estructurados que almacenan temporalmente los datos extraídos para su posterior procesamiento. Estos archivos se pueden encontrar dentro de la carpeta `datos`.

2. **Creación y Limpieza de Datos `(2-creacion_limpieza_df.ipynb)`**
    - Creación y limpieza de los DataFrames que contienen los precios de productos, eliminando duplicados, gestionando valores nulos y formateando los datos para facilitar su almacenamiento y análisis.

3. **Preparación de Tablas `(3-preparacion_tablas.ipynb)`**

    - Preparación de las tablas que serán insertadas en la base de datos, reestructuración y creación de las columnas necesarias para la inserción directa.

4. **Creación e inserciones en la base de datos + análisis `(4-consultas_bbdd.ipynb)`** 

    - Diseño de la base de datos en PostgreSQL para almacenar de manera eficiente la información recolectada.

    - Creación de tablas SQL que permiten estructurar la información en categorías clave: supermercados, tipo_productos, marcas y comparativas.

    - Análisis exploratorio y consultas SQL para extraer subconjuntos de datos de interés.

    - Generación de visualizaciones con Pandas y Matplotlib para comparar precios, estudiar su evolución temporal y detectar patrones y tendencias de precios.


## Resumen del proyecto

- **Scraping de Datos**:

    -   Extracción detallada de productos y precios de la web FACUA.
    -   Recopilación de datos para múltiples supermercados (Alcampo, Carrefour, Dia, Eroski, Hipercor y Mercadona).

-   **Almacenamiento en Base de Datos**:

    -   Creación de una base de datos relacional en PostgreSQL para almacenar toda la información recolectada.
    -   Población de la base de datos con los datos obtenidos de los archivos CSV.

-   **Análisis de Datos con Python y SQL**:

    -   Comparación de precios entre supermercados.
    -   Análisis de la evolución de precios en distintos periodos.
    -   Generación de gráficos que permitan visualizar las diferencias y tendencias de precios


## Conclusiones 

1. **Vuelos**: En los vuelos a Roma la media del precio de ida y vuelta es de 274 euros, bastante cerca de la mediana con 281 euros. Los precios de los vuelos van desde 80 hasta 415 euros. En el caso de París la media de los precios de los trayectos ida y vuelta es de casi 420 euros, cifra bastante más elevada que para Roma, y los precios de los vuelos van desde 150 hasta los 841 euros. Podemos observarlo de maner más gráfica:

<div align="center">
    <img src="imagenes/boxplot_vuelos.png" alt="Descripción de la imagen" width="400"/>
</div>

Observando el top 5 vuelos más baratos para cada ciudad los de roma oscilan entre 82 y 105 euros mientras que para París van desde 150 hasta 253, por lo que se puede concluir que a nivel económico la mejor opción en cuanto a vuelos sería Roma. Luego pueden entrar a considerarse otros factores como las horas de salida de los vuelos o la comapñía de la aerolínea, si se desea más información en cuanto a los vuelos puede consultar el archivo `1-EDA.ipynb` en la carpeta de `notebooks`.

2. **Hoteles**: En Roma la media de puntuación de los hoteles obtenidos es de 8.6, practicamente igual a la mediana. El precio total por las dos noches del fin de semana es de 496 euros un poco por encima de la mediana que es 425, lo que nos indica que hay algún hotel bastante caro, siendo el precio máximo de 2000 euros y el mínimo unos 90. En cuanto a la distancia a nuestro punto de referencia que es el coliseo, la media está a unos 2km. Para París tenemos una puntuación media en los hoteles de 8.2. El precio medio para las dos noches en París es de 450 euros, bastante por encima de la mediana que son 361. De nuevo esto indica que hay valores muy altos como podemos corroborar viendo que el precio máximo es de 4260 mientras que el mínimo es de 135. Finalmente, al punto de referencia que es el Louvre están todos de media a unos 4.75km, lo cual es bastante, pero cuanto más nos acerquemos al centro más subirán los precios. Podemos ver estos datos de una manera más gráfica oservando la siguiente imagen:

<div align="center">
    <img src="imagenes/boxplot_hoteles.png" alt="Descripción de la imagen" width="400"/>
</div>


También se lleva a cabo un estudio por puntuación y distancia a los puntos de referencia en el notebook anteriormente mencionado. Como la ubicación del hotel respecto a lugares emblemáticos de la ciudad es una de las principales características para elegir un hotel hemos realizado dos gráficas comparando ubicación y precio cuyas explicaciones se pueden encontrar en el EDA.

<div align="center">
    <img src="imagenes/dist_precio_roma.png" alt="Descripción de la imagen" width="700"/>
    <img src="imagenes/dist_precio_paris.png" alt="Descripción de la imagen" width="700"/>
</div>

3. **Actividades**: En cuanto a las actividades hay una gran variedad para ambas ciudades, como se puede observar en la gráfica a continuación.

<div align="center">
    <img src="imagenes/actividades.png" alt="Descripción de la imagen" width="700"/>
</div>

Además, también podemos tener en cuenta el precio de media de las actividades por categorías, siendo las más baratas en Roma los free tours, tours en bus turístico y tours en barco y en París: tours a pie, experiencias gastronómicas y paseos en barco.


Por lo tanto, en cuanto a vuelos la opción más económica es Roma, aunque dependerá también de las horas de los vuelos. En cuanto al hotel depende mucho de la ubicación y puntuación elegida, si se desea más cerca del centro y con mayor puntuación será más caro pero es verdad que tanto para Roma como para París se puede alcanzar un buen equilibrio con un precio de hotel relativamente bajo/medio, buena ubicación y una buena puntuación. Sin embargo, esta decisión queda totalmente en manos del cliente y sus necesidades. Finalmente, en cuanto a actividades, ambas ciudades tienen una amplia gama de opciones y siempre se pueden coger opciones más o menos económicas. Por lo que la principal sección verdaderamente influyente a nivel económico serían los vuelos, ya que tanto los hoteles como las actividades dependiendo de los gustos y necesidades del cliente sus precios van variando.


## Organización del Proyecto

El proyecto está organizado de la siguiente manera:

- **datos/**: Carpeta que contiene los archivos `.csv` de los datos extraídos de la web de Facua y las tablas ya limpias y listas para la inserción en la bbdd. Además de un `.json` con un diccionario de los links de cada producto analizado.

- **notebooks/**: Carpeta que contiene los archivos `.ipynb` sobre los cuales hemos trabajado los datos:
  - `1-scrapeo.ipynb`
  - `2-creacion_limpieza_df.ipynb`
  - `3-preparacion_tablas.ipynb`
  - `4-consultas_bbdd.ipynb`
    
    Estos archivos se deben revisar/ejecutar en orden para una completa comprensión del proyecto.

- **src/**: Carpeta que contiene un archivo `.py` en el cual tenemos funciones auxiliares a las cuales hacemos llamdas desde los notebooks.
  - `funciones_auxiliares.py`


## Instalación y Requisitos
Este proyecto usa Python 3.11 y requiere las siguientes bibliotecas:
- [numpy](https://numpy.org/doc/stable/)
- [pandas](https://pandas.pydata.org/docs/reference/frame.html)
- [matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
- [seaborn](https://seaborn.pydata.org/)
- [requests](https://requests.readthedocs.io/en/latest/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [Selenium](https://www.selenium.dev/documentation/)
- [psycopg2](https://pypi.org/project/psycopg2/)


Para visualizar el proyecto en tu máquina local, sigue estos pasos:

1. **Clona el repositorio**:
   ```bash
   git clone [URL del repositorio]

   Instala las dependencias en tu entorno de Python.
   
2. **Navega a la carpeta del proyecto**:
   ```bash
   cd Proyecto4-AnalisisFacua

2. **Ejecutar o visualizar los archivos**:
   Accede a la carpeta `notebooks` y ejecutar cada archivos en ordén. Además, configura una base de datos PostgreSQL y actualiza las credenciales en los notebooks.
