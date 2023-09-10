from carta import Carta

class ApuestaInvalida(Exception):

    def __init__(self, cantidad: int) -> None:
        super().__init__(f"No se puede apostar {cantidad} de dinero.")

class Jugador:
    """Clase que representa a un jugador en el juego de Texas Hold'em.

    Cada jugador tiene un nombre y puede recibir cartas, tanto hole cards como comunity cards.

    Attributes:
        __nombre (str): El nombre del jugador.
        __hole_cards (list[Carta]): Lista de hole cards del jugador.
        __dinero (int): Cantidad de dinero del jugador.
    """

    def __init__(self, nombre):
        """Inicializa un jugador con su nombre.

        Args:
            nombre (str): El nombre del jugador.
        """
        self.__nombre = nombre
        self.__hole_cards: list[Carta] = []
        self.__dinero = 1000
        self.__esta_en_juego = True

    @property
    def hole_cards(self):
        """Devuelve las hole cards del jugador."""
        return self.__hole_cards

    @property
    def dinero(self) -> int:
        """Retorna la cantidad de dinero actual del jugador."""
        return self.__dinero

    @property
    def puede_seguir_jugando(self) -> bool:
        """Indica si el jugador ya se ha retirado o no."""
        return self.__esta_en_juego

    @hole_cards.setter
    def hole_cards(self, hole_cards):
        """Recibe las hole cards del jugador.

        Args:
            hole_cards (list[Carta]): Lista de cartas hole cards.
        """
        self.__hole_cards = None
        self.__hole_cards = hole_cards

    def apostar(self, cantidad):
        """Realiza una apuesta por una cantidad específica."""
        if cantidad > self.dinero:
            return
        self.__dinero -= cantidad

    def pasar(self):
        """Pasa el turno al siguiente jugador."""

    def retirarse(self):
        """Se retira de la ronda actual."""
        self.__esta_en_juego = False

    def mostrar_hole_cards(self):
        """Muestra las hole cards del jugador en la pantalla."""
        for carta in self.__hole_cards:
            carta.mostrar_carta()

    def __eq__(self, obj):
        if not isinstance(obj, Jugador):
            return False
        jugador: Jugador = obj
        return str(jugador) == self.__nombre

    def __hash__(self):
        return hash(self.__nombre)

    def __str__(self):
        """Devuelve una representación en cadena del jugador."""
        return self.__nombre
