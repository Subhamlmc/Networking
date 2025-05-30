import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is listening on port 12345...")
conn, addr = server_socket.accept()
print(f"Connection established with {addr}")

while True:
    message = conn.recv(1024).decode()
    if message.lower() == 'exit':
        print("Client disconnected.")
        break
    print(f"Client: {message}")
    reply = input("You: ")
    conn.sendall(reply.encode())

conn.close()
