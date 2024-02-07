"""
Definiciones de clases de la tienda.
"""

class cliente:
    """Un  cliente de la tienda"""

    def __init__(
        self,
        dni: str,
        nombre: str,
        apellidos: str
    ) -> None:
        self.set_dni(dni)
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)

    def set_dni(self, dni: str) -> None:
        #comprobar letra dni
        self.__dni = dni
