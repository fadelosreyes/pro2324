"""
Biblioteca con socios.
"""
import datetime

class Lector:
    """Clase de los socios"""
    def __init__(self, numero,  nombre, apellidos) -> None:
        self.__numero = numero
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__moroso = False

    def set_nombre(self, nombre) -> None:
        """Cambia el nombre"""
        self.__nombre = nombre

    def set_apellidos(self, apellidos) -> None:
        """Cambia el apellido"""
        self.__apellidos = apellidos

    def numero(self) -> int:
        """Numero del socio"""
        return self.__numero

    def nombre(self) -> str:
        """Devuelve nombre"""
        return self.__nombre

    def apellidos(self) -> str:
        """Devuelve apellidos"""
        return self.__apellidos

    def es_moroso(self) -> bool:
        """Dice si es moroso o no"""
        return self.__moroso
    
    def marcar_moroso(self) -> None:
        """Marca como moroso a un cliente"""
        self.__moroso = True

class Libro:
    """Clase con los libros"""
    def __init__(self, codigo, titulo, autor, editorial) -> None:
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__prestado = False

    def set_codigo(self, codigo) -> None:
        """Cambia el codigo"""
        self.__codigo = codigo

    def set_titulo(self, titulo) -> None:
        """cambia titulo"""
        self.__titulo = titulo

    def set_autor(self, autor) -> None:
        """cambia autor"""
        self.__autor = autor

    def set_editorial(self, editorial) -> None:
        """cambia editorial"""
        self.__editorial = editorial

    def codigo(self) -> int:
        """Devuelve el codigo"""
        return self.__codigo

    def titulo(self) -> str:
        """Devuelve el titulo"""
        return self.__titulo

    def autor(self) -> str:
        """Devuelve el autor"""
        return self.__autor

    def editorial(self) -> str:
        """Devuelve editorial"""
        return self.__editorial

    def esta_prestado(self) -> bool:
        """Indica si el libro está prestado"""
        return self.__prestado

    def prestar(self) -> None:
        """Marca el libro como prestado"""
        self.__prestado = True

    def devolver(self) -> None:
        """Marca el libro como no prestado"""
        self.__prestado = False

class Prestamo:
    """Prestamos de libros a socios"""
    def __init__(self, lector, libro, fecha_prestamo) -> None:
        self.__lector = lector
        self.__libro = libro
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = None

    def set_lector(self, lector) -> None:
        """Cambia el codigo"""
        self.__lector = lector

    def set_libro(self, libro) -> None:
        """cambia titulo"""
        self.__libro = libro

    def lector(self) -> str:
        """Devuelve el lector"""
        return self.__lector

    def libro(self) -> str:
        """Devuelve el libro"""
        return self.__libro

    def get_fecha_prestamo(self) -> datetime.date:
        """Devuelve la fecha de prestamo"""
        return self.__fecha_prestamo

    def get_fecha_devolucion(self) -> datetime.date:
        """Devuelve la fecha de devolucion"""
        return self.__fecha_devolucion

    def devolver_libro(self, fecha_devolucion) -> None:
        """Devuelve el libro y establece la fecha de devolucion"""
        self.__fecha_devolucion = fecha_devolucion
        if (fecha_devolucion - self.__fecha_prestamo).days > 15:
            self.__lector.marcar_moroso() 