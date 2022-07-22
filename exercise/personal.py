import sqlite3


def crearRegimen():
    miConexion = sqlite3.connect("Personal")

    miCursor = miConexion.cursor()

    miCursor.execute('''
        CREATE TABLE REGIMEN (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            REGIMEN VARCHAR(30)
            )
        ''')
    datos = [("Administrativo",),
             ("General",)]

    miCursor.executemany(
        "INSERT INTO REGIMEN VALUES (NULL,?)", datos)

    miConexion.commit()

    miConexion.close()


def crearJornada():
    miConexion = sqlite3.connect("Personal")

    miCursor = miConexion.cursor()

    miCursor.execute('''
        CREATE TABLE JORNADA (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            JORNADA VARCHAR(30)
            )
        ''')
    datos = [("Administrativo_J1",),
             ("General_J1",)]

    miCursor.executemany(
        "INSERT INTO JORNADA VALUES (NULL,?)", datos)

    miConexion.commit()

    miConexion.close()


def crearContrato():
    miConexion = sqlite3.connect("Personal")

    miCursor = miConexion.cursor()

    miCursor.execute('''
        CREATE TABLE CONTRATO (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CONTRATO VARCHAR(30)
            )
        ''')
    datos = [("TEMPORAL",),
             ("PERMANENTE",)]

    miCursor.executemany(
        "INSERT INTO CONTRATO VALUES (NULL,?)", datos)

    miConexion.commit()

    miConexion.close()


def crearPago():
    miConexion = sqlite3.connect("Personal")

    miCursor = miConexion.cursor()

    miCursor.execute('''
        CREATE TABLE PAGO (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            PAGO VARCHAR(30)
            )
        ''')
    datos = [("ACH",),
             ("CK",)]

    miCursor.executemany(
        "INSERT INTO PAGO VALUES (NULL,?)", datos)

    miConexion.commit()

    miConexion.close()


def crearPersonal():
    miConexion = sqlite3.connect("Personal")

    miCursor = miConexion.cursor()

    miCursor.execute('''
        CREATE TABLE PERSONAL (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(30),
            APELLIDO VARCHAR(30),
            CEDULA VARCHAR(20),
            TELEFONO VARCHAR(15),
            AREA VARCHAR(30),
            CARGO VARCHAR(30),
            SALARIO MONEY,
            ID_REGIMEN INTEGER,
            ID_JORNADA INTEGER,
            ID_CONTRATO INTEGER,
            ID_PAGO INTEGER,
            CONTROL BIT,
            INICIO_CONTRATO DATE,
            FIN_CONTRATO DATE,
            ESTADO BIT,
            FOREIGN KEY(ID_REGIMEN) REFERENCES REGIMEN(ID),
            FOREIGN KEY(ID_JORNADA) REFERENCES JORNADA(ID),
            FOREIGN KEY(ID_CONTRATO) REFERENCES CONTRATO(ID),
            FOREIGN KEY(ID_PAGO) REFERENCES PAGO(ID)
            )
        ''')

    empleado = [("Luis Reynaldo", "Pérez Chávez",
                "081-240995-0008M", "8458-4479",
                 "Administracion", "Administrador",
                 5000.55, 1, 1, 1, 1, 1, "2020-01-15",
                 "2021-02-15", 1
                 )]

    miCursor.executemany(
        "INSERT INTO PERSONAL VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", empleado)

    miConexion.commit()

    miConexion.close()

    print("Tabla creada con éxito")


'''crearRegimen()
crearJornada()
crearContrato()
crearPago()
crearPersonal()'''
