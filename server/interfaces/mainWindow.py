from PyQt5.QtWidgets import QMainWindow

class MainWindow (QMainWindow) :
    def __init__(self, appTitle: str) -> None:
        super().__init__()

        #   setGeometry
        # 1: distancia da esquerda
        # 2: distancia do topo
        # 3: largura
        # 4: altura
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle(appTitle)

