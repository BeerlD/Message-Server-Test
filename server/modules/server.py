import socket
from threading import Thread

class Server:
    def __init__(self) -> None:
        self.__thread__ = Thread(target=self.__packetProcessor__)
    

    def init(self) -> None:
        self.__thread__.start()


    def __packetProcessor__(self):
        self.__host__ = socket.gethostname()
        self.__port__ = 5001
        self.__socket__ = socket.socket()
        self.__socket__.bind((self.__host__, self.__port__))
        self.__socket__.listen(100)
        self.__conection__, self.__address__ = self.__socket__.accept()
        
    
    def setMaxConnections(self, connections: int) -> None:
        self.__socket__.listen(connections)


