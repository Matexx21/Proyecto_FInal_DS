from enum import Enum
import random
from carta import Carta

class Cartas(Enum):
    """
    Una clase que representa los valores de las cartas en una baraja estándar.
    """

    DOS = 2
    TRES = 3
    CUATRO = 4
    CINCO = 5
    SEIS = 6
    SIETE = 7
    OCHO = 8
    NUEVE = 9
    DIEZ = 10
    JOTA = 11
    REINA = 12
    REY = 13
    AS = 14

class Palos(Enum):
    """
    Una clase que representa los palos en una baraja estándar.
    """

    CORAZONES = "Corazones"
    PICAS = "Picas"
    DIAMANTES = "Diamantes"
    TREBOLES = "Treboles"

class Baraja:
    """
    Representa una baraja de cartas estándar.
    """

    def __init__(self):
        """Inicializa una baraja de cartas estándar."""
        self.__cartas = set(
            Carta(carta.name, carta.value, palo.value) for carta in Cartas for palo in Palos
        )

    def reiniciar_baraja(self) -> None:
        """Reinicia la baraja para un nuevo juego"""
        self.__cartas = set(
            Carta(carta.name, carta.value, palo.value) for carta in Cartas for palo in Palos
        )

    def shuffle(self):
        """Baraja las cartas en la baraja."""
        cartas_lista = list(self.__cartas)  # Convertir el conjunto a una lista
        random.shuffle(cartas_lista)
        self.__cartas = cartas_lista

    def deal(self):
        """Reparte una carta de la baraja."""
        return self.__cartas.pop()

    def get_cartas(self, carta_por_encontrar: Carta):
        """Devuelve una lista de cartas específicas de la baraja.

        Args:
            valor (int): El valor de las cartas a buscar.
            palo (str): El palo de las cartas a buscar.

        Returns:
            List[Carta]: Una lista de cartas que coinciden con el valor y el palo especificados.
        """
        mano = [carta for carta in self.__cartas if carta == carta_por_encontrar]
        self.__cartas.remove(carta for carta in mano)
        return mano

    def __repr__(self):
        """Devuelve una representación en cadena de la baraja de cartas."""
        return f"<Baraja estándar: {len(self)} cartas restantes>"

    def __str__(self):
        """Devuelve una representación en cadena de la baraja de cartas."""
        return f"{self.__cartas}"
