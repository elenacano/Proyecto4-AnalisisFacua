import pandas as pd # type: ignore
import numpy as np
import re
import psycopg2 # type: ignore
from psycopg2 import OperationalError, errorcodes, errors  # type: ignore


def extraer_marca_cantidad(nombre):
    marcas_conocidas = ["hacendado", "auchan", "picual casa juncal", "capicua", "carrefour", "coosol", "fontasol", "koipe", "koipesol", "campomar", "ozolife",
                     "la masia", "ybarra", "carbonell", "abaco", "la espanola", "aromas del sur", "natursoy", "dcoop", "arguinano", "oro bailen",
                     "capricho andaluz", "coosur", "de nuestra tierra", "maestros de hojiblanca", "oro de genave", "marques de grinon", "nunez de prado", "oleoestepa",
                      "retama", "maeva", "cantero de letur", "pascual", "puleva", "asturiana", "kaiku", "lauki", "president", "rio", "nestle", "el buen pastor",
                       "danone", "laban", "actimel", "danacol", "noe", "denenes", "blemil", "almiron", "nivea", "ecran", "covap", "delial", "eroski",
                        "borgesol", "borges", "lanisol", "olilan", "urzante", "senorio de segura", "palacio de los olivos", "jaencoop", "carapelli",
                        "cazorliva", "duernas", "oro de genabe", "arrolan", "mendia", "olivar de segura", "saqura", "guillen", "mil olivas", "trujal tudela",
                        "o de la ribera", "sierra de cazorla", "guzman", "elizondo", "ultzama", "beyena", "bomilk", "celta", "euskal herria", "lacturale", 
                        "ram", "bizkaia", "ideal", "lactebal", "gaza", "flora", "diasol", "la almazara del olivar", "dia lactea", "abrisol", 
                        "el corte ingles", "elosol", "primer dia de cosecha", "abril", "casa juncal", "aceites de ardales", "agus", "alhema de queiles",
                        "aljibes", "almaoliva", "amarga y pica", "arboleda", "campo rico", "casas de hualdo", "castillo de canena",
                        "changlot", "conde de benalua", "dominus", "dulcesol", "el lagar del soto", "ester sole", "ferrarini", "finca penamoucho",
                        "flor de arana", "fuenroble", "germanor", "go vegg", "gotas de abril",  "hacienda el palo", "iznaoliva", "jacoliva", "lestornell",
                        "la almazara de canjayar", "la boella", "la laguna de fuente de piedra", "la organic", "la redonda", "hojiblanca", "merula", 
                        "misko", "miro", "molino de la calzada", "molino de olivas de bolea", "mueloliva", "nunez de prado", "oleaurum", "oleodiel",
                        "olibeas", "oliva verde", "olivar del sur", "pago baldios san carlos", "pan de olivo", "parqueoliva", "picualia", 
                        "reales almazaras de alcaniz", "romanico", "santiveri", "somontano", "surinver", "torremilano", "tresces", "unio", "alberto chicote",
                        "valroble", "venta del baron", "altamira", "ato", "clesa", "ecomil", "el castillo", "feiraco", "granja noe", "hipp", "la colmenarena",
                        "la yerbera", "lar", "larsa", "letona", "leyma", "lilibet", "llet nostra", "lletera campllong", "madriz", "pano", "priegola",
                        "senorio de sarria", "tierra de sabor", "unicla", "valles unidos", "villacorona", "cexasol", "ondosol", "alcampo", "ucasol", 
                        "el molino d gines", "fruto del sur", "giralda", "mar de olivos", "monegros", "olivar centenario", "olivo de cambil", "ondoliva",
                        "oro aragon", "oro virgen", "saeta", "suroliva", "valdezarza", "verde segura", "duc", "lr", "la colmenarena", "mntbelle", 
                        "santa gadea", "consorcio", "lorea", "santa teresa", "naturgreen", "mustela", "babaria", "babybio", "sveltesse", "saha", "arronizarbe"]
  
    marca = next((m for m in marcas_conocidas if m in nombre.lower()), np.nan) #va iterando por la lista de marcas y si no coincide ninguna pone nan
    
    cantidad = re.search(r"(\d+(\.\d+)?\s*(x\s*\d+\s*)?[ml|l|cl|g|mg|kg]+)", nombre.lower())
    cantidad = cantidad.group(0) if cantidad else np.nan #Devuelve la cadena macheada por la re
    df = pd.Series([marca, cantidad])
    return df

def conexion_bbdd(nombre):
    try:  
        conexion = psycopg2.connect(
        database = nombre,
        user = "postgres",
        password = "admin",
        host = "localhost",
        port = "5432")
        
    except OperationalError as e:
        if e.pgcode == errorcodes.INVALID_PASSWORD:
            print("La contraseña es erronea")
        elif e.pgcode == errorcodes.CONNECTION_EXCEPTION:
            print("Error de conexion")
        else:
            print(f"Ocurrió el error {e}")

    return conexion



def creacion_tablas(conexion, cursor):
    try:
        # Creación tabla supermercados
        query_creacion_supermercado = """create table if not exists supermercados (
                            id_supermercado int primary key,
                            nombre varchar(100) not null
                            );"""

        cursor.execute(query_creacion_supermercado)
        conexion.commit()

        # Creación tabla tipo_producto
        query_creacion_tipo_producto = """create table if not exists tipo_producto (
                                id_producto int primary key,
                                nombre varchar(100) not null
                                );"""

        cursor.execute(query_creacion_tipo_producto)
        conexion.commit()

        # Creación tabla comparativa
        query_creacion_comparativa = """create table if not exists comparativa (
                                id_comparativa serial primary key,
                                id_supermercado integer not null,
                                id_producto integer not null,
                                nombre varchar(300) not null,
                                tipo varchar(200),
                                fecha date not null,
                                precio numeric(8,4),
                                incremento varchar(50),
                                porcentaje numeric(8,4),
                                foreign key (id_supermercado) references supermercados(id_supermercado),
                                foreign key (id_producto) references tipo_producto(id_producto)
                                );"""

        cursor.execute(query_creacion_comparativa)
        conexion.commit()

    except Exception as e:
        print(f"Error creando tablas: {e}")


def insercion_supermercados(conexion, cursor):
    df_tabla_super = pd.read_csv("../datos/tabla_super.csv", index_col=0)
    lista_tuplas_super = [tuple(fila) for fila in df_tabla_super.values]
    query_insercion = "insert into supermercados (id_supermercado, nombre) values (%s, %s)"
    cursor.executemany(query_insercion, lista_tuplas_super)
    conexion.commit()

def insercion_productos(conexion, cursor):
    df_tabla_productos = pd.read_csv("../datos/tabla_productos.csv", index_col=0)
    lista_tuplas_productos = [tuple(fila) for fila in df_tabla_productos.values]
    query_insercion = "insert into tipo_producto (id_producto, nombre) values (%s, %s)"
    cursor.executemany(query_insercion, lista_tuplas_productos)
    conexion.commit()

def insercion_comparativa(conexion, cursor):
    df_tabla_comparativa = pd.read_csv("../datos/tabla_comparativa.csv", index_col=0)
    lista_tuplas_comparativas = [tuple(fila) for fila in df_tabla_comparativa.values]
    query_insercion = """insert into comparativa 
        (id_supermercado, id_producto, nombre, tipo, fecha, precio, incremento, porcentaje) 
        values (%s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.executemany(query_insercion, lista_tuplas_comparativas)
    conexion.commit()