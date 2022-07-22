from tkinter import *
from tkinter import messagebox
import sqlite3

# ------------------------------FUNCIONES---------------------------------------


def conexionBBDD():

    miConexion = sqlite3.connect("Usuarios")

    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE USUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            APELLIDO VARCHAR(50),
            PASSWORD VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIO VARCHAR(50))
            ''')

        messagebox.showinfo("Base de datos", "BBDD creada con éxito")

    except:

        messagebox.showwarning("¡Atención!", "La BBDD ya existe")


def salirAplicacion():

    valor = messagebox.askquestion("Salir", "Desea salir de la aplicacion?")

    if valor == "yes":
        raiz.destroy()


def limpiarDatos():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miPassword.set("")
    miDireccion.set("")
    textComment.delete(1.0, END)


'''
def crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("INSERT INTO USUARIOS VALUES (NULL, '" + miNombre.get() + "', '" + miApellido.get() +
                     "', '" + miPassword.get() + "', '" + miDireccion.get() + "', '" + textComment.get("1.0", END) + "')")

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro creado con exito")'''


def crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    try:
        varGestion = (miNombre.get(), miApellido.get(),
                      miPassword.get(), miDireccion.get(), textComment.get('1.0', END))

        miCursor.execute(
            'INSERT INTO USUARIOS VALUES(NULL,?,?,?,?,?)', varGestion)
        miConexion.commit()

        messagebox.showinfo('Información', '¡Registro creado con éxito!')

    except:
        messagebox.showwarning(
            'Tabla NO existe', 'La tabla GESTION no se encuentra creada')


def leer():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM USUARIOS WHERE ID =" + miId.get())

    elUsuario = miCursor.fetchall()

    for usuario in elUsuario:
        miId.set(usuario[0]),
        miNombre.set(usuario[1]),
        miApellido.set(usuario[2])
        miPassword.set(usuario[3]),
        miDireccion.set(usuario[4]),
        textComment.insert(1.0, usuario[5])

    miConexion.commit()


"""def actualizar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("UPDATE USUARIOS SET NOMBRE= '" + miNombre.get() + "', APELLIDO= '" + miApellido.get() + "', PASSWORD= '" +
                     miPassword.get() + "' , DIRECCION ='" + miDireccion.get() + "', COMENTARIO ='" + textComment.get("1.0", END) + "' WHERE ID=" + miId.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro actualizado con exito")"""


def actualizar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    varGestion = (miNombre.get(), miApellido.get(),
                  miPassword.get(), miDireccion.get(), textComment.get('1.0', END))

    miCursor.execute(
        "UPDATE USUARIOS SET NOMBRE=?, APELLIDO=?, PASSWORD=?, DIRECCION =?, COMENTARIO =? WHERE ID=" + miId.get(), varGestion)

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro actualizado con exito")


def eliminar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("DELETE FROM USUARIOS WHERE ID=" + miId.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro borrado con éxito")

# -------------------------------RAIZ-------------------------------------------


raiz = Tk()

raiz.title("Ejercicio CRUD")

# -----------------------------MENUS-------------------------------------------

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

'''Base de datos'''
archivoMenu = Menu(barraMenu, tearoff=0)

archivoMenu.add_command(label="Conectar", command=conexionBBDD)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

barraMenu.add_cascade(label="BBDD", menu=archivoMenu)

'''Edicion'''
edicionMenu = Menu(barraMenu, tearoff=0)

edicionMenu.add_command(label="Limpiar", command=limpiarDatos)

barraMenu.add_cascade(label="Edicion", menu=edicionMenu)

'''Herramientas'''
herramientaMenu = Menu(barraMenu, tearoff=0)

herramientaMenu.add_command(label="Crear", command=crear)
herramientaMenu.add_command(label="Leer", command=leer)
herramientaMenu.add_command(label="Actualizar", command=actualizar)
herramientaMenu.add_command(label="Eliminar", command=eliminar)

barraMenu.add_cascade(label="CRUD", menu=herramientaMenu)

'''Ayuda'''
infoMenu = Menu(barraMenu, tearoff=0)

infoMenu.add_command(label="Licencia")
infoMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="Ayuda", menu=infoMenu)

# -----------------------------FRAMES------------------------------------------

miFrame = Frame(raiz, width=500, height=500, padx=20, pady=20)
miFrame.pack()

buttonFrame = Frame(raiz, width=100, height=100, padx=10, pady=10)
buttonFrame.pack()


# -----------------------------LABELS-----------------------------------------

labelId = Label(miFrame, text="Id:")
labelId.grid(row=0, column=1, sticky="e", padx=20, pady=10)
labelNombre = Label(miFrame, text="Nombre:")
labelNombre.grid(row=1, column=1, sticky="e", padx=20, pady=10)
labelApellido = Label(miFrame, text="Apellido:")
labelApellido.grid(row=2, column=1, sticky="e", padx=20, pady=10)
labelPassword = Label(miFrame, text="Contraseña:")
labelPassword.grid(row=3, column=1, sticky="e", padx=20, pady=10)
labelDireccion = Label(miFrame, text="Dirección:")
labelDireccion.grid(row=4, column=1, sticky="e", padx=20, pady=10)
labelComent = Label(miFrame, text="Comentario:")
labelComent.grid(row=5, column=1, sticky="e", padx=20, pady=10)

# -------------------------------ENTRYS------------------------------------------

miId = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPassword = StringVar()
miDireccion = StringVar()

entryId = Entry(miFrame, textvariable=miId)
entryId.grid(row=0, column=2, padx=10, pady=10)
entryNombre = Entry(miFrame, textvariable=miNombre)
entryNombre.grid(row=1, column=2, padx=10, pady=10)
entryApellido = Entry(miFrame, textvariable=miApellido)
entryApellido.grid(row=2, column=2, padx=10, pady=10)
entryPassword = Entry(miFrame, textvariable=miPassword)
entryPassword.grid(row=3, column=2, padx=10, pady=10)
entryPassword.config(show="&")
entryDireccion = Entry(miFrame, textvariable=miDireccion)
entryDireccion.grid(row=4, column=2, padx=10, pady=10)

textComment = Text(miFrame, width=15, height=4)
textComment.grid(row=5, column=2)
scrollVert = Scrollbar(miFrame, command=textComment.yview)
scrollVert.grid(row=5, column=3, sticky="nsew")
textComment.config(yscrollcommand=scrollVert.set)


# ------------------------------BUTTONS------------------------------------------

createButton = Button(buttonFrame, text="Create", padx=10, command=crear)
createButton.grid(row=1, column=1)
readButton = Button(buttonFrame, text="Read", padx=10, command=leer)
readButton.grid(row=1, column=2)
updateButton = Button(buttonFrame, text="Update", padx=10, command=actualizar)
updateButton.grid(row=1, column=3)
deleteButton = Button(buttonFrame, text="Delete", padx=10, command=eliminar)
deleteButton.grid(row=1, column=4)


raiz.mainloop()
