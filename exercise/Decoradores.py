
def funcion_decorador(funcion_parametro):
    def funcion_interior(*args, **kwargs):

        # Acciones adicionales que decoran
        print("Vamos a realizar un cálculo")

        funcion_parametro(*args, **kwargs)

        # Acciones adicionales que decoran
        print("Hemos terminado el calculo")

    return funcion_interior


@funcion_decorador
def suma(num1, num2):
    print(num1+num2)


@funcion_decorador
def resta(num1, num2):
    print(num1-num2)


@funcion_decorador
def potencia(base, exponente):
    print(pow(base, exponente))


suma(7, 5)

resta(12, 10)


potencia(base=5, exponente=3)
