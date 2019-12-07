def sumar(n1,n2):
    """
    Esta es la documentacion de la funcion sumar:
    Recibe 2 numeros y retorna la suma
    
    Ahora escribo los tests
    
    >>> sumar(4,3)
    7
    
    >>> sumar(3,5)
    8
    
    """
    return n1 + n2

import doctest
doctest.testmod()

#desde la terminal: python doctestdes_terminal.py -v
