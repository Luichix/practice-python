# -------------funcion normal--------------------------

def area_triangulo(base, altura):
    return (base*altura)/2


triangulo1 = area_triangulo(9, 6)

print(triangulo1)

# -------------funcion lambda-------------------------


lambda_triangulo= lambda base, altura: base*altura/2

triangulo3 = lambda_triangulo(9, 6)

print(triangulo3)


al_cubo = lambda numero: pow(numero, 3)

print(al_cubo(3))

destacar_valor=lambda comision: "¡{}! $".format(comision)

comision_Ana=15585

print(destacar_valor(comision_Ana))