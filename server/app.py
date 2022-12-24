import sys
from PyQt5.QtWidgets import QApplication

from interfaces import MainWindow
from modules.server import  Server

class ApplicationApp:
    def __init__(self, title: str) -> None:
        self.__server__ = Server()
        self.__app__ = QApplication(sys.argv)
        self.title = title

    def run(self) -> None:
        mainWindow = MainWindow(self.title)
        mainWindow.show()
        sys.exit(self.__app__.exec_())


