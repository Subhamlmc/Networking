import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

print("Connected to server. Type 'exit' to disconnect.")

while True:
    message = input("You: ")
    client_socket.sendall(message.encode())
    if message.lower() == 'exit':
        break
    reply = client_socket.recv(1024).decode()
    print(f"Server: {reply}")

client_socket.close()
