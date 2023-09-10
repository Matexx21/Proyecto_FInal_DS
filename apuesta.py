from jugador import Jugador

class Apuestas:

    def __init__(self) -> None:
        self.__apuestas = {}

    def agregar_apuesta(self, jugador: Jugador, dinero: int):
        """Guarda las apuestas de los jugadores"""
        jugador.apostar(dinero)
        self.__apuestas[jugador] = dinero

    def calcular_total_dinero(self) -> int:
        """Suma todo el dinero de la apuesta."""
        total = 0
        for dinero in self.__apuestas.values():
            total += dinero
        return total

    def __vaciar_apuestas(self):
        """Borra todas las apuestas de los jugadores."""
        self.__apuestas.clear()

    def entregar_todo_el_dinero(self) -> int:
        """Entrega todo el dinero de esta apuesta."""
        dinero = self.calcular_total_dinero()
        self.__vaciar_apuestas()
        return dinero
