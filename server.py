import socket
import threading

clients = []
document = ""

def handle_client(client_socket, addr):
    global document
    print(f"[NEW CONNECTION] {addr} connected.")
    client_socket.send(document.encode('utf-8'))  
    connected = True
    while connected:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if data:
                print(f"[{addr}] {data}")
                document += data  
                broadcast(data, client_socket, addr)  
        except Exception as e:
            print(f"[ERROR] An error occurred while handling client {addr}: {e}")
            break
    client_socket.close()
    clients.remove(client_socket)
    print(f"[DISCONNECTED] {addr} disconnected.")

def broadcast(message, sender_socket, sender_addr):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(f"[{sender_addr}] {message}".encode('utf-8'))
            except Exception as e:
                print(f"[ERROR] An error occurred while broadcasting message to client: {e}")
                client.close()
                clients.remove(client)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))  
server.listen()
print("[STARTING] Server is starting...")

while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
