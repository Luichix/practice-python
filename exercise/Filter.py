"""def numero_par(num):

    if num % 2 == 0:

        return True"""


numeros = [17, 24, 7, 39, 8, 51, 92]

print(list(filter(lambda n: n % 2 == 0, numeros)))

# -------------------------------------------------------


class Empleado():

    def __init__(self, nombre, cargo, salario):

        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):

        return "{} que trabaja como {} tiene un salario de $ {}".format(self.nombre, self.cargo, self.salario)


listaEmpleados = [
    Empleado("Juan", "Director", 9500),
    Empleado("Ana", "Presidente", 5000),
    Empleado("Maria", "Administrativo", 3500),
    Empleado("Julio", "Secretario", 6700),
    Empleado("Mario", "Sub-Directo", 7200),
    Empleado("Jose", "Ayudante", 4800)

]

"""empleado_Luis = Empleado("Luis", "Jefe", 300000)

print(empleado_Luis.salario)"""

salario_altos = filter(lambda e: e.salario > 5000, listaEmpleados)

for empleado_salario in salario_altos:
    print(empleado_salario)

# ------------------------FUNCION MAP--------------------------------


def calculo_comision(empleado):
    if (empleado.salario >= 5000):

        empleado.salario = empleado.salario*1.03

    return empleado


listaEmpleadosComision = map(calculo_comision, listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)
