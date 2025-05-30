import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('localhost',1234))
digit=input("Enter the number you want table of : ")
client_socket.sendall(digit.encode())
while True:
    message = client_socket.recv(1024)
    if not message:
        break
    print(message.decode())

client_socket.close()