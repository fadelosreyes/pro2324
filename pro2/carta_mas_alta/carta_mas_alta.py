class Numero:
    @staticmethod
    def validos() -> """list[str]""":
        return [str(x) for x in range(2, 11)] + ['J', 'Q', 'K', 'As']

    @staticmethod
    def valido(_numero: str) -> bool:
        return _numero in Numero.validos()

    def __init__(self, _numero: str) -> None:
        if not Numero.valido(_numero):
            raise ValueError('El número no es válido')
        self.__numero: str = str(_numero)
        assert Numero.valido(self.numero())

    def __repr__(self) -> str:
        return f'Numero({self.numero()!r})'

    def __str__(self) -> str:
        return self.numero()

    def numero(self) -> str:
        return self.__numero

    def valor(self) -> int:
        try:
            num = self.numero()
            return int(num)
        except ValueError:
            return {'J': 11, 'Q': 12, 'K': 13, 'As': 14}[num]

class Palo:
    def __init__(self, _palo: str, _valor: int) -> None:
        self.__palo = _palo
        self.__valor = _valor

    def __repr__(self) -> str:
        return f'Palo({self.palo()!r})'

    def __str__(self) -> str:
        return self.palo()

    def palo(self) -> str:
        return self.__palo

    def valor(self) -> int:
        return self.__valor

class Carta:
    def __init__(self, _numero: Numero, _palo: Palo) -> None:
        self.__numero = _numero
        self.__palo = _palo

    def __repr__(self) -> str:
        return f'Carta({self.numero()!r}, {self.palo()!r})'

    def __str__(self) -> str:
        return f'{self.numero()} de {self.palo()}'

    def __eq__(self, __value: object) -> bool:
        if type(self) != type(__value):
            return NotImplemented
        return self.numero() == __value.numero() and \
            self.palo() == __value.palo()

    def __hash__(self) -> int:
        return hash((self.numero(), self.palo()))

    def numero(self) -> Numero:
        return self.__numero

    def palo(self) -> Palo:
        return self.__palo

    # def valor(self) -> int:
    #     return self.numero().valor()

    # def comparar(self, otra) -> int:
    #     if self.valor() < otra.valor():
    #         return -1
    #     if self.valor() > otra.valor():
    #         return +1
    #     if self.valor() == otra.valor():
    #         if self.palo().valor() < otra.palo().valor():
    #             return -1
    #         if self.palo().valor() > otra.palo().valor():
    #             return +1
    #         assert self.palo().valor() != otra.palo().valor()
    #     return 0


class Coleccion:
    def __init__(self, elementos=None) -> None:
        if elementos is None:
            elementos = set()
        self.__elementos = set(elementos)

    def __str__(self) -> str:
        return str([str(x) for x in self.__elementos])

    def __iter__(self):
        return iter(self.__elementos)

    def conjunto(self):
        return set(self.__elementos)

    def copiar(self) -> 'Coleccion':
        return Coleccion(self.__elementos)

    # def elementos(self):
    #     return self.__elementos.copy()

    def mover(self, elem):
        if elem not in self.__elementos:
            raise ValueError('El elemento no existe.')
        self.__elementos.remove(elem)
        self.__elementos.add(elem)

    def sacar(self, elem=None):
        if elem is None:
            return self.__elementos.pop()
        self.__elementos.remove(elem)
        return elem

    def meter(self, elem):
        self.__elementos.add(elem)
        return elem


class Jugador:
    def __init__(self, _nombre, _cartas) -> None:
        self.__nombre = _nombre
        self.__cartas = Coleccion(_cartas)
        self.__puntos = 0

    def __str__(self) -> str:
        return self.nombre()

    def __repr__(self) -> str:
        conjunto = self.__cartas.conjunto()
        return f'Jugador({self.nombre()!r}, {conjunto!r})'

    def nombre(self):
        return self.__nombre

    def puntos(self):
        return self.__puntos

    def cartas(self):
        return iter(self.__cartas)

    def soltar_una(self) -> Carta:
        return self.__cartas.sacar()

    def incr_puntos(self) -> int:
        self.__puntos += 1
        return self.__puntos


class Mazo(Coleccion):
    pass

class Jugada:
    def __init__(self, _cartas=None) -> None:
        if _cartas is None:
            _cartas = {}
        else:
            _cartas = _cartas.copy()
        self.__cartas: """dict[Jugador,Carta]""" = _cartas

    def meter(self, _carta: Carta, _jugador: Jugador):
        self.__cartas[_jugador] = _carta

    def quien_gana(self) -> """tuple[Jugador, Carta]""":
        ganadores: """dict[Jugador,Carta]""" = {}
        carta_ganadora = max(self.__cartas.values(), key=lambda x: x.numero().valor())
        for jugador, carta in self.__cartas.items():
            if carta.numero().valor() == carta_ganadora.numero().valor():
                ganadores[jugador] = carta
        assert len(ganadores) > 0
        if len(ganadores) == 1:
            return tuple(ganadores.items())[0]
        ganador, carta_ganadora = max(ganadores.items(), key=lambda t: t[1].palo().valor())
        return (ganador, carta_ganadora)


