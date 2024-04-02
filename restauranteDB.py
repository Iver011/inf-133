import sqlite3
conn= sqlite3.connect("restaurant.db")

conn.execute (

"""
    CREATE TABLE PLATOS 
    (
    id INTEGER PRIMARY KEY
    nombre TEXT NOT NULL,
    precio INTEGER NOT NULL
    categoria TEXT NOT NULL);
"""

)


conn.execute (

"""
    INSERT INTO PLATOS (nombre,precio,categoria)
    VALUES('milanesa',25,'carne')
"""

)
conn.execute (

"""
    CREATE TABLE MESAS
    (
    id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL);
"""

)


conn.execute (

"""
    INSERT INTO MESAS (numero)
    VALUES('1')
"""

)
conn.execute (

"""
    CREATE TABLE PEDIDOS
    (
    id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL);
"""

)


conn.execute (

"""
    INSERT INTO MESAS (numero)
    VALUES('1')
"""

)