import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005

# Buat socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Ketik pesan ke server (ketik 'exit' untuk keluar)\n")

while True:
    message = input("Pesan: ")

    if message.lower() == "exit":
        print("Keluar dari client...")
        break

    # Kirim pesan ke server
    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

    # Terima balasan dari server
    data, _ = client_socket.recvfrom(1024)
    print("Server:", data.decode())

# Tutup socket client
client_socket.close()
