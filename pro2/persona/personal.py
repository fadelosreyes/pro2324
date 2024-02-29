"""
compara la edad de otra persona con la tuya
"""
class Persona:
    def __init__(self, edad) -> None:
        self.set_edad(edad)

    def set_edad(self, edad) -> None:
        self.__edad = edad
    
    def edad(self) -> int:
        return self.__edad
    
    def compara_edad(self, otra_persona) -> str:
        if self.edad() < otra_persona.edad():
            return "La primera persona es menor"
        elif self.edad() > otra_persona.edad():
            return "La primera persona es mayor"
        else:
            return "Ambas personas tienen la misma edad"


# Ejemplo de uso:
persona1 = Persona(30)
persona2 = Persona(25)

print(persona1.compara_edad(persona2))  # Salida: La otra persona es menor
