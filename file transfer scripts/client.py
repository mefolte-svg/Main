
import socket

Host = socket.gethostname()
Ip = socket.gethostbyname(Host)
Port = 62222

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
    print(f"laczenie z {Ip} na porcie {Port}")
    s1.connect((Ip, Port))
    sciezka = input()
    koncowka = sciezka.split('.')[1]
    with open(sciezka, 'rb') as f1:
        smb = f1.read()
        liczba_kontrolna = len(smb)
    s1.sendall(liczba_kontrolna.to_bytes(1024, byteorder='big'))
    s1.sendall(smb)
    s1.sendall(koncowka.encode())
