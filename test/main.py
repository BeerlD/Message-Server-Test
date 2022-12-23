import modules

server = modules.Server()
server.init()

client = modules.Client()

while True:
    message = input("Message (exit): ")
    if message.lower() == "exit":
        client.close()
        break
    print(f"Response: {client.sendMessage(message)}")
