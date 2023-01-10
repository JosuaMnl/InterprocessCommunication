# Josua Manalu 2024240117
import socket
import json

IP = "127.0.0.5"

PORT = 5005

BUFFER_SIZE = 5005

# Data barang
dataBarang = [
    {
    "nama" : "Beras",
    "stock": 5
    },
    {"nama":"Cabai",
    "stock":2}
]

# Ubah data barang menjadi json
dataJson = json.dumps(dataBarang)

print(f"Target IP \t\t: {IP}")
print(f"Target Port \t\t: {PORT}")
print(f"Pesan \t\t\t: {dataJson.encode()}")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

sock.sendto(dataJson.encode(), (IP, PORT))