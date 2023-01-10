# Josua Manalu 2024240117
import socket
import json
import os, re, threading

TCP_IP = "127.0.0.1"
PORT = 5005
BUFFER_SIZE = 1024


class jumlahStock(threading.Thread):
    def __init__(self, IP, gudang):
        threading.Thread.__init__(self)
        self.IP = IP
        self.gudang = gudang
    def run(self):
        self.hasil = 0
        sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

        # Melakukan Binding Socket
        sock.bind((self.IP, PORT))
        print(f"Menunggu Kiriman Pesan {self.gudang}")
        data, addr = sock.recvfrom(1024)
        # Load data json dari gudang
        y = json.loads(data)
        # Memanggil stock data barang, pada kasus ini data beras
        stockBeras = y[0]["stock"]
        self.hasil = stockBeras
        # print(stockBeras)

    def hasilHitung(self):
        return self.hasil

gudang1 = jumlahStock("127.0.0.3", "Gudang 1")
gudang2 = jumlahStock("127.0.0.4", "Gudang 2")
gudang3 = jumlahStock("127.0.0.5", "Gudang 3")

gudang1.start()
gudang2.start()
gudang3.start()

gudang1.join()
gudang2.join()
gudang3.join()

totalStock = gudang1.hasilHitung() + gudang2.hasilHitung() + gudang3.hasilHitung()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, PORT))
s.listen(1)

print(f"Socket mendengar di alamat {TCP_IP} : {PORT}")

while True:
    conn, addr = s.accept()
    print(f"Mendengar koneksi dari {addr}")
    data = conn.recv(BUFFER_SIZE)

    informasiProduksi = f"Informasi jumlah stock untuk barang beras sebanyak {totalStock} KG."
    conn.send(informasiProduksi.encode())
    conn.close()