# Josua Manalu 2024240117
import socket

BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, \
    socket.SOCK_STREAM)

pilih = input("Pilih Mesin (1/2) : ")

if pilih == "1":
    PORT = 5005
    IP = "127.0.0.1"
    mesin = "Mesin 1"
    s.connect((IP, PORT))
    s.send(pilih.encode())
    data = s.recv(BUFFER_SIZE)
    s.close()

elif pilih == "2":
    PORT = 5004
    IP = "127.0.0.2"
    mesin = "Mesin 2"
    s.connect((IP, PORT))
    s.send(pilih.encode())
    data = s.recv(BUFFER_SIZE)
    s.close()
else:
    print("Pilihan yang anda masukkan tidak tersedia!")


print(f"Pesan didapatkan dari {mesin} : {data.decode()}")