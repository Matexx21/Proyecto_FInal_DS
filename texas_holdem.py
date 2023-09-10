from typing import List
from apuesta import Apuestas
from carta import Carta

from jugador import Jugador
from mesa import Mesa
from ronda import (
    PrimeraRonda, SegundaRonda, TerceraRonda,
    AntesDeLasRondas, DespuesDeLasRondas
)

class TexasHoldem:

    MAXIMO_JUGADORES = 4

    def __init__(self) -> None:
        self.__apuestas: List[Apuestas] = []
        self.__jugadores: List[Jugador] = []
        self.__mesa = Mesa()
        self.__ronda = AntesDeLasRondas()

    @property
    def ronda(self):
        return self.__ronda

    @property
    def apuestas(self):
        return self.__apuestas

    def guardar_apuestas(self, apuestas: Apuestas):
        self.__apuestas.append(apuestas)

    def get_community_cards(self) -> List[Carta]:
        return self.__mesa.community_cards

    def get_cartas_jugador(self, index: int = 0) -> List[Carta]:
        return self.__jugadores[index].hole_cards

    def get_jugador(self, index: int = 0) -> Jugador:
        return self.__jugadores[index]

    def retirar_jugador(self, index: int = 0):
        self.__jugadores[index].retirarse()

    def agregar_jugadores(self, jugadores: List[Jugador]):
        """Agrega los jugadores al juego y reparte las hole cards."""
        n_jugadores = len(jugadores) if len(jugadores) < 4 else 4
        for i in range(n_jugadores):
            self.__jugadores.append(jugadores[i])
        self.__completar_jugadores()
        self.__mesa.repartir_hole_cards(jugadores)

    def __completar_jugadores(self):
        if len(self.__jugadores) == self.MAXIMO_JUGADORES:
            return
        for i in range(self.MAXIMO_JUGADORES - len(self.__jugadores)):
            self.__jugadores.append(Jugador(f"Jugador {i}"))

    def iniciar_rondas(self):
        self.__ronda = PrimeraRonda()
        self.__ronda.mostrar_community_cards(self.__mesa)

    def cambiar_a_segunda_ronda(self):
        """Cambia a la segunda ronda de juego."""
        self.__ronda = SegundaRonda()
        self.__ronda.mostrar_community_cards(self.__mesa)

    def cambiar_a_tercera_ronda(self):
        """Cambia a la tercera ronda de juego."""
        self.__ronda = TerceraRonda()
        self.__ronda.mostrar_community_cards(self.__mesa)

    def finalizar_juego(self):
        """Finaliza el juego."""
        self.__ronda = DespuesDeLasRondas()

    def mostrar_resultados(self):
        pass
