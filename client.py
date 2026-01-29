import socket

#socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 9999

#credentials for connection
cred = {
    "username" : "user123",
    "pass" : "pass123"
}

#verification
print("Enter credentials to connect to the server: \n")
username = input("username: ")
password = input("password: ")

if(username == cred["username"] and password == cred["pass"]):

    #connect
    client_socket.connect((host,port))

    print("Connected to server. Type 'stop' to end.")

    while True:
        #send data to server
        client_data = input("Client: ")
        client_socket.sendall(client_data.encode())

        #check for stop command
        if client_data.strip().lower() == "stop":   
            print("Stop command sent. Closing connection.")
            break
        # receive data from server
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Server: {data}")
        # check for stop command
        if data.strip().lower() == "stop":
            print("Stop command received. Closing connection.")
            break

    client_socket.close()
    print("Client closed.")

else:
    client_socket.close()
    print("invalid credentials, server connection failed! ")
    print("Client closed.")

