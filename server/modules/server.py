import socket
from threading import Thread
from .configs import SERVER_MAX_CONNECTIONS, SERVER_PORT

class Server:
    def __init__(self) -> None:
        self.__thread__ = Thread(target=self.__packetProcessor__)
    

    def init(self) -> None:
        self.__thread__.start()


    def __packetProcessor__(self):
        self.__host__ = socket.gethostname()
        self.__port__ = SERVER_PORT
        self.__socket__ = socket.socket()
        self.__socket__.bind((self.__host__, self.__port__))
        self.__socket__.listen(SERVER_MAX_CONNECTIONS)
        self.__conection__, self.__address__ = self.__socket__.accept()
        
    
    def setMaxConnections(self, connections: int) -> None:
        self.__socket__.listen(connections)


