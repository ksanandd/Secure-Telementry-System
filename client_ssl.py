import socket
import ssl
import json

SERVER_IP = "localhost"
PORT = 9999

context = ssl._create_unverified_context()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure_client = context.wrap_socket(client, server_hostname=SERVER_IP)

secure_client.connect((SERVER_IP, PORT))

print("✅ Connected securely!")

device_id = input("Enter Device ID: ")

while True:
    try:
        temp = float(input("Enter temperature: "))

        packet = {
            "device_id": device_id,
            "temperature": temp
        }

        secure_client.send(json.dumps(packet).encode())

        print("✅ Sent securely!\n")

    except Exception as e:
        print("Error:", e)
        break

secure_client.close()