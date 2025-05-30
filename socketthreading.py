import socket
import threading
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('localhost',1111))
server_socket.listen(1)
print("Listening in port number : 1111")
conn,addr=server_socket.accept()
print(f"Connection request by {addr}")
def send():
    while True:
        msg=input("Server:")
        if msg=="quit":
            break
        conn.sendall(msg.encode())
def receive():
    while True :
        msg1=conn.recv(1024).decode()
        if not msg1:
            print("Connection Closed !!")
        print(f"Server :{msg1}")

threading.Thread(target=send).start()
threading.Thread(target=receive).start()
