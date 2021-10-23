import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting
s.connect(("localhost", 14200))
print("Connected...\n")
 
s.send('client'.encode())
server_name = s.recv(1024).decode()
print(f"connected to : {server_name} ")
 
while True:
    message = s.recv(1024)
    message = message.decode()
    print(server_name, ":", message)
    message = input(str("client : "))
    s.send(message.encode())
    