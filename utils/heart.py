import socket
import time

def beat_heart(server_socket, heartbeat, verbose):
    conn, addr = server_socket.accept()
    if verbose : print(f"Connected by {addr}")
    
    data = conn.recv(1024).decode()
    if data.startswith("heartbeat"):
        client_heartbeat = int(data.split()[1])
        heartbeat = client_heartbeat + 1
        if verbose : print(f"Heartbeat {client_heartbeat} received, sending heartbeat number {heartbeat}...")
        response = f"heartbeat {heartbeat}"
        conn.sendall(response.encode())
        return conn, heartbeat

def connect_heart(server_ip, client_heartbeat, verbose):
    try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((server_ip, 5551))
                message = f"heartbeat {client_heartbeat}"
                client_socket.sendall(message.encode())
                if verbose : print(f"Sent heartbeat {client_heartbeat}")
                
                response = client_socket.recv(1024).decode()
                if response.startswith("heartbeat"):
                    server_heartbeat = int(response.split()[1])
                    if verbose : print(f"Heartbeat {server_heartbeat} received")
                    client_heartbeat = server_heartbeat + 1
                return client_heartbeat
               
                
                
    except socket.error as e:
        print(f"Couldn't connect to server {server_ip}:5551. Error: {e}. Retrying...")
        time.sleep(5)