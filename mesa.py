from typing import List
from baraja import Baraja
from carta import Carta
from jugador import Jugador

class Mesa:

    def __init__(self):
        """Inicializa una mesa de juego."""
        self.__baraja = Baraja()
        self.__baraja.shuffle()
        self.__community_cards: list[Carta] = []

    @property
    def community_cards(self):
        return self.__community_cards

    def repartir_hole_cards(self, jugadores: List[Jugador]):
        """Reparte las hole cards a los jugadores."""
        for jugador in jugadores:
            hole_card1 = self.__baraja.deal()
            hole_card2 = self.__baraja.deal()
            jugador.hole_cards = [hole_card1, hole_card2]

    def mostrar_primeras_tres_cartas(self):
        """Muestra las primeras 3 community cards."""
        for _ in range(3):
            community_card = self.__baraja.deal()
            community_card.mostrar_carta()
            self.__community_cards.append(community_card)

    def mostrar_cuarta_carta(self):
        """Muestra las cuarta community card."""
        cuarta_carta = self.__baraja.deal()
        cuarta_carta.mostrar_carta()
        self.__community_cards.append(cuarta_carta)

    def mostrar_quinta_carta(self):
        """Muestra las quinta community card."""
        quinta_carta = self.__baraja.deal()
        quinta_carta.mostrar_carta()
        self.__community_cards.append(quinta_carta)
