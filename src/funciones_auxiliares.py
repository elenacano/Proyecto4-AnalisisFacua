import pandas as pd
import numpy as np
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors  # type: ignore


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