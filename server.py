import socket

#konfigurasi server
HOST = '10.178.155.222'  #alamat IP di ini yang akan di hubungi oleh client
PORT = 8080            # port server kita 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  
    s.listen()
    print(f"Server mendengarkan di {HOST}:{PORT}")
    
    while True:
        
        conn, addr = s.accept()
        
        with conn:
            print(f"Terhubung dengan client dari alamat: {addr}")
            
            while True:
                data = conn.recv(1024)  
                if not data:
                    break  
                
                pesan_diterima = data.decode('utf-8')
                print(f"Pesan dari client: {pesan_diterima}")
                
                pesan_balasan = "Konfirmasi: Pesan Anda sudah diterima oleh server."
                conn.sendall(pesan_balasan.encode('utf-8'))
            
            print("Koneksi dengan client ditutup.")
            print("Menunggu koneksi client berikutnya...\n")