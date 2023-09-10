import random
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QSpinBox, QPushButton
from apuesta import Apuestas
from jugador import Jugador
from mesa_ui import Ui_Mesa
from interfaz import Ui_MainWindow
from ronda import AntesDeLasRondas, DespuesDeLasRondas, PrimeraRonda, SegundaRonda, TerceraRonda
from texas_holdem import TexasHoldem

class TexasHoldemPantalla:

    def __init__(self) -> None:
        self.__texas_holdem = TexasHoldem()
        self.__interfaz = Ui_Mesa()
        self.__dialog = QDialog()
        self.__texas_holdem.agregar_jugadores([
            Jugador("jugador 1"),
            Jugador("jugador 2"),
            Jugador("jugador 3"),
            Jugador("jugador 4"),
        ])

    def __mostrar_cartas_jugador(self):
        cartas = self.__texas_holdem.get_cartas_jugador()
        for carta in cartas:
            if not isinstance(self.__texas_holdem.ronda, AntesDeLasRondas):
                carta.mostrar_carta()
                continue
            carta.ocultar_carta()
        pixmap_1 = QtGui.QPixmap(cartas[0].image_path)
        self.__interfaz.carta_7.setPixmap(pixmap_1)
        pixmap_2 = QtGui.QPixmap(cartas[1].image_path)
        self.__interfaz.carta_8.setPixmap(pixmap_2)

    def __cambiar_ronda(self):
        ronda_actual = self.__texas_holdem.ronda
        if isinstance(ronda_actual, AntesDeLasRondas):
            self.__texas_holdem.iniciar_rondas()
            self.__mostrar_cartas_jugador()
            self.__interfaz.ronda_label.setText("Primera Ronda")
        elif isinstance(ronda_actual, PrimeraRonda):
            cartas = self.__texas_holdem.get_cartas_jugador()
            self.__texas_holdem.cambiar_a_segunda_ronda()
            self.__interfaz.ronda_label.setText("Segunda Ronda")
            cartas = self.__texas_holdem.get_community_cards()
            self.__interfaz.carta_1.setPixmap(QtGui.QPixmap(cartas[0].image_path))
            self.__interfaz.carta_2.setPixmap(QtGui.QPixmap(cartas[1].image_path))
            self.__interfaz.carta_3.setPixmap(QtGui.QPixmap(cartas[2].image_path))
        elif isinstance(ronda_actual, SegundaRonda):
            self.__texas_holdem.cambiar_a_tercera_ronda()
            self.__interfaz.ronda_label.setText("Tercera Ronda")
            cartas = self.__texas_holdem.get_community_cards()
            self.__interfaz.carta_4.setPixmap(QtGui.QPixmap(cartas[3].image_path))
        elif isinstance(ronda_actual, TerceraRonda):
            self.__texas_holdem.finalizar_juego()
            self.__interfaz.ronda_label.setText("Juego Finalizado")
            cartas = self.__texas_holdem.get_community_cards()
            self.__interfaz.carta_5.setPixmap(QtGui.QPixmap(cartas[4].image_path))
        elif isinstance(ronda_actual, DespuesDeLasRondas):
            return

    def __ingresar_apuesta_inicial(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ingrese una apuesta inicial:"))
        spinbox = QSpinBox()
        spinbox.setMinimum = 1
        spinbox.setMaximum = 1000
        layout.addWidget(spinbox)
        ingresar_apuesta_boton = QPushButton("Ingresar")
        layout.addWidget(ingresar_apuesta_boton)
        ingresar_apuesta_boton.clicked.connect(
            lambda: [
                self.__guardar_apuesta_jugador(spinbox.value()),
                self.__dialog.close()
            ]
        )
        self.__dialog.setLayout(layout)
        self.__dialog.exec_()

    def __guardar_apuesta_jugador(self, valor: int):
        apuestas = Apuestas()
        jugador = self.__texas_holdem.get_jugador()
        apuestas.agregar_apuesta(jugador, valor)
        apuestas.agregar_apuesta(
            self.__texas_holdem.get_jugador(random.randint(1,3)),
            random.randint(1,500)
        )
        self.__texas_holdem.guardar_apuestas(apuestas)
        self.__interfaz.dinero_actual.setText(f"Dinero: {jugador.dinero}")

    def __guardar_apuestas(self, cantidad: int = 2, apuesta_jugador: int = 0):
        apuestas = Apuestas()
        jugador = self.__texas_holdem.get_jugador()
        apuestas.agregar_apuesta(
            jugador, apuesta_jugador
        )
        self.__interfaz.dinero_actual.setText(f"Dinero: {jugador.dinero}")
        for i in range(1, cantidad + 1):
            apuestas.agregar_apuesta(
                self.__texas_holdem.get_jugador(i),
                random.randint(1,500)
            )
        self.__texas_holdem.guardar_apuestas(apuestas)

    def __jugador_pasa(self):
        ronda_actual = self.__texas_holdem.ronda
        if isinstance(ronda_actual, PrimeraRonda):
            self.__guardar_apuestas(3)
        elif isinstance(ronda_actual, SegundaRonda):
            self.__guardar_apuestas(3)
        elif isinstance(ronda_actual, TerceraRonda):
            self.__guardar_apuestas(3)
        else:
            return

    def __jugador_apuesta(self):
        ronda_actual = self.__texas_holdem.ronda
        apuesta = self.__interfaz.input_apuesta.value()
        if isinstance(ronda_actual, PrimeraRonda):
            self.__guardar_apuestas(3, apuesta)
        elif isinstance(ronda_actual, SegundaRonda):
            self.__guardar_apuestas(3, apuesta)
        elif isinstance(ronda_actual, TerceraRonda):
            self.__guardar_apuestas(3, apuesta)
        else:
            return

    def __conectar_senales(self):
        self.__interfaz.apostar_boton.clicked.connect(
            lambda: [
                self.__cambiar_ronda(),
                self.__jugador_apuesta()
            ]
        )
        self.__interfaz.pasar_boton.clicked.connect(
            lambda: [
                self.__cambiar_ronda(),
                self.__jugador_pasa()
            ]
        )
        self.__interfaz.retirarse_boton.clicked.connect(
            lambda: [
                self.__retirar_jugador(),
                self.__cambiar_ronda()
            ]
        )

    def __retirar_jugador(self):
        self.__interfaz.apostar_boton.setDisabled(True)
        self.__interfaz.retirarse_boton.setDisabled(True)
        self.__texas_holdem.retirar_jugador()

    def show(self):
        self.__texas_holdem = TexasHoldem()
        self.__texas_holdem.agregar_jugadores([
            Jugador("jugador 1"),
            Jugador("jugador 2"),
            Jugador("jugador 3"),
            Jugador("jugador 4"),
        ])
        form = QDialog()
        self.__interfaz.setup_ui(form)
        self.__conectar_senales()
        self.__mostrar_cartas_jugador()
        random_num = random.randint(0,3)
        if random_num == 0:
            self.__ingresar_apuesta_inicial()
        else:
            self.__guardar_apuestas()
        form.exec_()

class MenuPrincipal:

    def __init__(self) -> None:
        self.__interfaz = Ui_MainWindow()
        self.__conectar_botones()
        self.__pantalla = TexasHoldemPantalla()
        self.__creditos = QDialog()
        self.__setup_creditos()

    def __iniciar_juego(self):
        self.__pantalla.show()

    def __mostrar_creditos(self):
        self.__creditos.exec_()

    def __setup_creditos(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Creado por:"))
        layout.addWidget(QLabel("Mateo Dávalos"))
        self.__creditos.setLayout(layout)

    def __conectar_botones(self):
        self.__interfaz.iniciar_boton.clicked.connect(
            self.__iniciar_juego
        )
        self.__interfaz.creditos_boton.clicked.connect(
            self.__mostrar_creditos
        )

    def run_game(self):
        self.__interfaz.setup_ui()
        self.__interfaz.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.style = "Fusion"
    game = MenuPrincipal()
    game.run_game()
    sys.exit(app.exec_())
