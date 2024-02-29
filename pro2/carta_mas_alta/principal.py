from carta_mas_alta import Numero, Palo, Carta, Jugador, Mazo, Jugada

PICAS = Palo('picas', 1)
DIAMANTES = Palo('diamantes', 2)
TREBOLES = Palo('tréboles', 3)
CORAZONES = Palo('corazones', 4)

baraja = set()

for palo in [CORAZONES, DIAMANTES, TREBOLES, PICAS]:
    for numero in Numero.validos():
        baraja.add(Carta(Numero(numero), palo))

baraja = Mazo(baraja)

jugador1 = Jugador('Pepe', [baraja.sacar() for _ in range(4)])
jugador2 = Jugador('María', [baraja.sacar() for _ in range(4)])

jugadores = [jugador1, jugador2]

print(f'Jugadores: {jugador1}, {jugador2}')

# combinaciones = [(Carta(Numero('5'), x), Carta(Numero('5'), y))
#                   for x in [PICAS, DIAMANTES, TREBOLES, CORAZONES]
#                   for y in [PICAS, DIAMANTES, TREBOLES, CORAZONES]
#                   if x != y]

# for x, y in combinaciones:
#     mi_jugada = Jugada({jugador1: x, jugador2: y})
#     print(x, y, mi_jugada.quien_gana()[1])

while True:
    try:
        carta1 = jugador1.soltar_una()
        carta2 = jugador2.soltar_una()

        print(f'{jugador1} juega la carta {carta1}')
        print(f'{jugador2} juega la carta {carta2}')

        jugada = Jugada({jugador1: carta1, jugador2: carta2})
        ganador, carta_ganadora = jugada.quien_gana()
        print(f'Gana {ganador} con la carta {carta_ganadora}')
        ganador.incr_puntos()
    except KeyError:
        break

print(f'{jugador1} tiene {jugador1.puntos()} puntos.')
print(f'{jugador2} tiene {jugador2.puntos()} puntos.')
ganador = max(jugadores, key=lambda x: x.puntos())
puntos = [x.puntos() for x in jugadores]
maximo_puntos = max(x.puntos() for x in jugadores)
cuantos = sum(1 for x in jugadores if x.puntos() == maximo_puntos)
if cuantos > 1:
    print('Empate.')
else:
    print(f'El ganador es {ganador}.')