import doctest


def area_triangulo(base, altura):
    """ 
        Calcula el area de un triangulo dado
        >>> area_triangulo(3,6)
        'El área del triángulo es: 9.0'
    """
    return "El área del triángulo es: " + str((base*altura)/2)


def compruebaMail(mailUsuario):
    """La funcion compruebaMail evalúa un mail recibido en busca de la @. Si tiene una @ es correcto, si tiene más de una @ es incorrecto, si la @ esta al final es incorrecto

    >>> compruebaMail('juan@cursos.com')
    True

    >>> compruebaMail('juan@cursos.com@')
    False

    >>> compruebaMail('juancursos.com')
    False

    >>> compruebaMail('juan@@cursos.com')
    False




    """
    arroba = mailUsuario.count('@')
    if (arroba != 1 or mailUsuario.rfind('@') == (len(mailUsuario)-1) or mailUsuario.find('@') == 0):
        return False
    else:
        return True


doctest.testmod()


