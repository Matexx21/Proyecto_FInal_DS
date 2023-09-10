import os

class Carta:
    """Una clase que representa una carta de juego estándar.

    Atributos:
        nombre (str): El nombre de la carta (por ejemplo, 'As', 'Dos', 'Rey').
        valor (int): El valor de la carta.
        palo (str): El palo de la carta 
        (por ejemplo, 'Corazones', 'Picas', 'Tréboles', 'Diamantes').
        es_visible (bool): Si la carta está boca arriba (Verdadero) o boca abajo (Falso).
    """

    def __init__(self, nombre: str, valor: int, palo: str) -> None:
        self.__nombre = nombre
        self.__valor = valor
        self.__palo = palo
        self.__es_visible = True
        self.__imagen_filename = f"{self.__nombre.capitalize()} de {self.__palo}.png"
        self.__image_path = None
        self.ocultar_carta()

    @property
    def es_visible(self) -> bool:
        """Retorna el nombre de la carta"""
        return self.__es_visible

    @property
    def nombre(self) -> str:
        """Retorna el nombre de la carta"""
        return self.__nombre

    @property
    def palo(self) -> str:
        """Retorna el palo de la carta"""
        return self.__palo

    @property
    def valor(self) -> int:
        """Retorna el valor de la carta"""
        return self.__valor

    @property
    def image_path(self) -> str:
        """Retorna la ubicacion de la imagen dentro del equipo."""
        return self.__image_path

    def __cargar_imagen(self) -> None:
        """Carga la imagen de la carta utilizando Pygame."""
        resources_folder = os.path.join("resources", "cartas")
        self.__image_path = os.path.join(resources_folder, self.__imagen_filename)

    def mostrar_carta(self) -> None:
        """Hace visible una carta en el juego y carga su imagen."""
        self.__es_visible = True
        self.__cargar_imagen()

    def ocultar_carta(self) -> None:
        """Muestra boca abajo una carta en el juego y carga una imagen de dorso."""
        self.__es_visible = False
        resources_folder = os.path.join("resources", "cartas")
        self.__image_path = os.path.join(resources_folder, "Carta.png")

    def __eq__(self, other: object) -> bool:
        """Compara dos objetos Carta por su nombre y valor.

        Args:
            other (Carta): El otro objeto Carta a comparar.

        Returns:
            bool: True si los dos objetos Carta tienen el mismo nombre y valor,
            False en caso contrario.
        """
        if not isinstance(other, Carta):
            return False
        carta: Carta = other
        return self.__palo == carta.palo and self.__valor == carta.valor

    def __hash__(self):
        """Define el hash de la instancia de Carta."""
        return hash((self.__nombre, self.__valor, self.__palo))

    def __repr__(self) -> str:
        """Devuelve una representación en string de una Carta.

        - Si la carta está boca arriba, 
        la representación en cadena está en el formato 'nombre de palo'.
        - Si la carta está boca abajo, la representación en cadena es 'Carta'.
        """
        return f"{self.__nombre} de {self.__palo}" if self.__es_visible else "Carta"

    def __str__(self) -> str:
        return f"{self.__nombre} de {self.__palo}" if self.__es_visible else "Carta"
