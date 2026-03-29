import socket
import ssl
import json
import os
import threading
from collections import defaultdict

HOST = '0.0.0.0'
PORT = 9999

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("🔐 Secure Multi-Client Server Started...\n")

device_temps = defaultdict(list)
lock = threading.Lock()

def handle_client(client_socket, addr):
    try:
        secure_socket = context.wrap_socket(client_socket, server_side=True)
        print(f"✅ Client connected: {addr}")

        while True:
            data = secure_socket.recv(1024)

            if not data:
                break

            packet = json.loads(data.decode())
            device = packet["device_id"]
            temp = packet["temperature"]

            with lock:
                device_temps[device].append(temp)

                os.system("cls")
                print("🔐 SECURE TELEMETRY DASHBOARD\n")
                print("Device\tLatest\tMin\tMax\tAvg\tCount")
                print("-------------------------------------------")

                for d, temps in device_temps.items():
                    latest = temps[-1]
                    minimum = min(temps)
                    maximum = max(temps)
                    avg = round(sum(temps)/len(temps), 2)

                    print(f"{d}\t{latest}°C\t{minimum}°C\t{maximum}°C\t{avg}°C\t{len(temps)}")

    except Exception as e:
        print(f"⚠️ Error with {addr}: {e}")

    finally:
        client_socket.close()
        print(f"❌ Client disconnected: {addr}")


while True:
    client_socket, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    thread.start()