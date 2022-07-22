import sqlite3


def crear():
    miConexion = sqlite3.connect("Horario")

    miCursor = miConexion.cursor()

    miCursor.execute('''
        CREATE TABLE HORAS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ENTRADA TIME(0),
            SALIDA TIME(0),
            TIEMPO TIME(0))
    ''')

    horas = [("08:00:00", "17:00:00"),
             ("07:50:00", "17:20:00"),
             ("08:10:00", "16:50:00"),
             ("07:55:00", "16:40:00"),
             ("08:05:00", "17:10:00")]

    miCursor.executemany("INSERT INTO HORAS VALUES (NULL,?,?,NULL)", horas)

    miConexion.commit()

    miConexion.close()


def leer():
    miConexion = sqlite3.connect("Horario")

    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM HORAS WHERE TIEMPO IS NULL")

    datos = miCursor.fetchall()

    miConexion.commit()

    miConexion.close()

    return datos


def actualizar(datos):
    miConexion = sqlite3.connect("Horario")
    miCursor = miConexion.cursor()

    miCursor.executemany(
        "UPDATE HORAS SET TIEMPO = ? WHERE ID= ?", datos)

    miConexion.commit()

    miConexion.close()

    print("Datos actualizados con exito")
