import socket
from datetime import datetime

# Konfigurasi server
SERVER_IP = "127.0.0.1"     # alamat lokal
SERVER_PORT = 5005          # port server
BUFFER_SIZE = 1024          # ukuran buffer pesan

# Buat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"Server UDP berjalan di {SERVER_IP}:{SERVER_PORT}")
print("Menunggu pesan dari client...\n")

# Server berjalan terus (tidak menutup koneksi)
while True:
    data, client_address = server_socket.recvfrom(BUFFER_SIZE)
    message = data.decode()
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Tampilkan di terminal
    print(f"[{waktu}] Pesan dari {client_address}: {message}")

    # Simpan log ke file
    with open("server_log.txt", "a") as log_file:
        log_file.write(f"[{waktu}] Dari {client_address}: {message}\n")

    # Kirim balasan ke client
    response = f"Pesan diterima pada {waktu}"
    server_socket.sendto(response.encode(), client_address)
