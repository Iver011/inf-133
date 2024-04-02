#construir informacion de carrera(nombre,duracion) estudiantes(nombre,apellido,fecha_nac),matricula(estudiante,carrera,fecha)

import sqlite3

conn= sqlite3.connect("instituto.db")
###
###conn.execute (
###
###"""
###    CREATE TABLE CARRERAS 
###    (id INTEGER PRIMARY KEY,
###    nombre TEXT NOT NULL,
###    duracion INTEGER NOT NULL);
###"""
###
###)
###
###
###conn.execute (
###
###"""
###    INSERT INTO CARRERAS (nombre,duracion)
###    VALUES('Ingenieria de Sistemas',5)
###"""
###
###)
###conn.execute (
###
###"""
###    INSERT INTO CARRERAS (nombre,duracion)
###    VALUES('ADMINISTRACION DE EMPRESAS',4)
###"""
###
###)
###
###print("CARRERAS: ")
###cursor=conn.execute("SELECT * FROM CARRERAS")
###for row in cursor:
###    print(row)
###
###conn.execute (
###
###"""
###    CREATE TABLE ESTUDIANTES 
###    (id INTEGER PRIMARY KEY,
###    nombre TEXT NOT NULL,
###    apellido TEXT NOT NULL,
###    fecha_nacimiento DATE NOT NULL);
###    
###"""
###
###)
###
###
###conn.execute (
###
###"""
###    INSERT INTO ESTUDIANTES (nombre,apellido,fecha_nacimiento)
###    VALUES('Juan','Fernandez','2000-06-29')
###"""
###
###)
###conn.execute (
###
###"""
###    INSERT INTO ESTUDIANTES (nombre,apellido,fecha_nacimiento)
###    VALUES('Carlos','Cordero','1999-05-19')
###"""
###
###)
###print("\nESTUDIANTES: ")
###cursor=conn.execute("SELECT * FROM ESTUDIANTES")
###for row in cursor:
###    print(row)
###
###
###conn.execute (
###
###"""
###    CREATE TABLE MATRICULAS 
###    (id INTEGER PRIMARY KEY,
###    estudiante_id INTEGER NOT NULL,
###    carrera_id INTEGER NOT NULL,
###    fecha DATE NOT NULL,
###    FOREIGN KEY (estudiante_id) REFERENCES ESTUDIANTES(id),
###    FOREIGN KEY (carrera_id) REFERENCES CARRERAS(id));
###    
###"""
###
###)
###
###
###conn.execute (
###
###"""
###    INSERT INTO MATRICULAS (estudiante_id,carrera_id,fecha)
###    VALUES(1,1,'2023-01-15')
###"""
###
###)
###conn.execute (
###
###"""
###    INSERT INTO MATRICULAS (estudiante_id,carrera_id,fecha)
###    VALUES(2,2,'2024-01-30')
###"""
###
###)
###
###conn.execute (
###
###"""
###    INSERT INTO MATRICULAS (estudiante_id,carrera_id,fecha)
###    VALUES(1,2,'2020-01-09')
###"""
###
###)
###
###print("\nMATRICULACION: ")
###cursor=conn.execute("SELECT * FROM MATRICULAS")
###for row in cursor:
###    print(row)
###
###
###
###print("\nMATRICULAS: ")
###cursor=conn.execute(
###    """
###    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULAS.fecha
###    FROM MATRICULAS
###    JOIN ESTUDIANTES ON MATRICULAS.estudiante_id=ESTUDIANTES.id
###    JOIN CARRERAS ON MATRICULAS.carrera_id = CARRERAS.id
###"""
###)
###for row in cursor:
###    print(row)
###
###
###conn.execute(
###    """
###    UPDATE MATRICULAS
###    SET fecha = '2024-01-29'
###    WHERE id=2
###    """
###)
###
###
###conn.execute(
###    """
###    DELETE FROM MATRICULAS
###    WHERE id=1
###    """
###)
###
###print("\nMATRICULACION: ")
###cursor=conn.execute("SELECT * FROM MATRICULAS")
###for row in cursor:
###    print(row)
###
conn.close()
