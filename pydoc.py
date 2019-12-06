class Saludos:
    """
    Esta es una clase para saludadores,
    Tiene clases de saludos
    BuenDia y Adios
    Ambas reciben un nombre
    """
    def BuenDia(self,nombre):
        """Esta funcion saluda con buenos dias a una persona"""
        print(f"Buenoas dias {nombre}")
    
    def Adios(self,nombre):
        """Esta funcion se despide de una persona"""
        print(f"Adios {nombre}")
        

#desde la terminal pydoc path-del archivo.
#desde la terminal pydoc -w path-del-archivo. Genera el archivo con la doc.
