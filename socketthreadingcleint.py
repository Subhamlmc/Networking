import socket
import threading
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('localhost',1111))
def send():
    while True:
        msg=input("Client:")
        if msg=="quit":
            break
        client_socket.sendall(msg.encode())
        
def receive():
    while True :
        msg1=client_socket.recv(1024).decode()
        if not msg1:
            print("Connection Closed !!")
        
        print(f"Server :{msg1}")

threading.Thread(target=send).start()
threading.Thread(target=receive).start()
