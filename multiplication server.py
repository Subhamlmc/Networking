import socket
import time
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('localhost',1234))
server_socket.listen(5)
print(f"Listening in port number --1234--")
#accepting connection part
conn,addr=server_socket.accept()
print(f"\tConnection request accepted for {addr}")
data=conn.recv(1024).decode()
x=int(data)
i=int(1)
for i in range(1, 11):
    result = x * i
    msg = f"{x} * {i} = {result}"
    conn.sendall(msg.encode())
    time.sleep(1)
conn.close()