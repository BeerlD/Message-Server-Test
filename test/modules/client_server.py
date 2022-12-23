import socket

class Client:
    def __init__(self, port: int = 5001) -> None:
        self.__host = socket.gethostname()
        self.__port = port
        self.__socket = socket.socket()
        self.__socket.connect((self.__host, port))

    def sendMessage(self, message: str) -> int:
        self.__socket.send(message.encode())
        result = self.__socket.recv(1024).decode()
        return int(result)

    def close(self) -> None:
        self.__socket.send("exit".encode())
        self.__socket.close()
