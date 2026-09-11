
import socket

Host = socket.gethostname()
Ip = socket.gethostbyname(Host)
Port = 62222

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
    s1.bind((Ip,Port))
    s1.listen()
    while True:
        client_socket, Ip_client = s1.accept()
        print(f'polaczenie z {Ip_client}' )
        nr_kontrolny_bajty = client_socket.recv(1024)
        nr_kontrolny_int = int.from_bytes(nr_kontrolny_bajty, byteorder='big')
        plik_bajty = client_socket.recv(nr_kontrolny_int)
        koncowka_bajty = client_socket.recv(1024)
        koncowka_str = koncowka_bajty.decode()
        print(plik_bajty)
        nazwa_pliku = f'{id({})}.bin'
        sciezka = r"C:\Users\opyrc\Desktop\test" + f"\{nazwa_pliku}.{koncowka_str}"
        
        with open(sciezka, "wb") as plik:
            plik.write(plik_bajty)
        print("plik zapisany")


