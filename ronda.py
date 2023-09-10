from abc import ABC

from mesa import Mesa

class Ronda(ABC):
    """Clase abstracta que representa una ronda de juego."""

    def mostrar_community_cards(self, mesa: Mesa):
        """Método abstracto para jugar la ronda."""

class AntesDeLasRondas(Ronda):
    """Clase que representa el momento antes de iniciar las rondas."""

class DespuesDeLasRondas(Ronda):
    """Clase que representa el juego finalizado."""

class PrimeraRonda(Ronda):
    """Clase que representa la primera ronda de juego."""

    def mostrar_community_cards(self, mesa: Mesa):
        """Juega la primera ronda."""
        mesa.mostrar_primeras_tres_cartas()

class SegundaRonda(Ronda):
    """Clase que representa la segunda ronda de juego."""

    def mostrar_community_cards(self, mesa: Mesa):
        """Juega la segunda ronda."""
        mesa.mostrar_cuarta_carta()

class TerceraRonda(Ronda):
    """Clase que representa la tercera ronda de juego."""

    def mostrar_community_cards(self, mesa: Mesa):
        """Juega la tercera ronda."""
        mesa.mostrar_quinta_carta()
