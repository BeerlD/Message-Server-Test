import socket
from threading import Thread

class Server:
    def __init__(self, maxClients: int = 2) -> None:
        self.__thread = Thread(target=self.__packetProcessor, args=[maxClients])
    
    def init(self) -> None:
        self.__thread.start()

    def __packetProcessor(self, maxClients):
        self.__host = socket.gethostname()
        self.__port = 5001

        self.__socket = socket.socket()
        self.__socket.bind((self.__host, self.__port))
        self.__socket.listen(maxClients)
        self.__conection, self.__address = self.__socket.accept()

        while True:
            response = self.__conection.recv(1024).decode()
            if response:
                if response == "exit":
                    break

                print("Server received: " + response)
                self.__conection.send("200".encode())
        
        self.__conection.close()
    
