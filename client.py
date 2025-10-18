import socket

# Konfigurasi Client
HOST = '10.178.155.222'  # Alamat IP server yang akan dihubungi
PORT = 8080            # Port server (harus sama dengan port di server.py)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    print(f"Mencoba terhubung ke server {HOST}:{PORT}...")
    s.connect((HOST, PORT))
    print("Berhasil terhubung ke server!\n")
    
    while True:
        pesan = input("Ketik pesan (atau 'exit' untuk keluar): ")
        
        if pesan.lower() == 'exit':
            print("Menutup koneksi...")
            break
        
        s.sendall(pesan.encode('utf-8'))
        
        data = s.recv(1024)
        
        balasan = data.decode('utf-8')
        print(f"Balasan dari server: {balasan}\n")
    
    print(" Koneksi ditutup.")