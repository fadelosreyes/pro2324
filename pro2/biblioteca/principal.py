from datetime import datetime
from biblioteca import Lector, Libro, Prestamo


lector1 = Lector(1, "Ana", "García")
lector2 = Lector(2, "Roberto", "Sánchez")

libro1 = Libro(101, "El camino", "Miguel Delibes", "Editorial1")
libro2 = Libro(102, "Cien años de soledad", "Gabriel García Márquez", "Editorial2")
libro3 = Libro(103, "Rayuela", "Julio Cortázar", "Editorial3")

prestamo1 = Prestamo(lector1, libro1, datetime.now())
prestamo2 = Prestamo(lector2, libro2,  datetime.now())
prestamo3 = Prestamo(lector1, libro3, datetime.now())






