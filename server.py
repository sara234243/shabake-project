import time, socket, sys
 
print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 14200))
s.listen(1)
name = '[server]'
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")
 
s_name = conn.recv(4096)
s_name = s_name.decode()
print(s_name, "connected ")
conn.send(name.encode())
 
while True:
    conn.send('send me path'.encode())
    message = conn.recv(4096)
    message = message.decode()
    try:
        file=open(f'{message}','r')
        message=file.read()
        conn.send(message.encode())
        message = conn.recv(4096)
        message = message.decode()
        print(s_name, ":", message)
    except:
        conn.send('“404 Not Found'.encode())
        message = conn.recv(4096)
        message = message.decode()
        print(s_name, ":", message)