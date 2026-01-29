import socket

#socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 9999

#bind
server_socket.bind((host,port))
#listen
server_socket.listen(1)


#accept
client_socket, addr = server_socket.accept() 
print("Connection from: " + str(addr)+ " has been established.")

print("Connected to server. Type 'stop' to end.")
while True:
    # receive data from client
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print(f"Client: {data}")

    # check for stop command
    if data.strip().lower() == "stop":
        print("Stop command received. Closing connection.")
        break
    #send
    server_data = input("Server: ")
    client_socket.sendall(server_data.encode())

    #check for stop command
    if server_data.strip().lower() == "stop":
        print("Stop command sent. Closing connection.")
        break

#close
client_socket.close()
server_socket.close()
print("Server closed.")