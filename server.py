import sys
import socket
import subprocess
from datetime import datetime
from optparse import OptionParser

# HALF DUPLEX haberleşme sağlayan python kodu
# bir önceki kodun değiştirilmiş ve güncellenmiş haildir.

Parsers = OptionParser()
# Kullanıcıdan verilerini parametre olarak girebilmesini sağlamak için
# bir OptionParser oluşturdum.
Parsers.add_option("-i", dest="ip", help="IP address")
Parsers.add_option("-p", dest="port", help="Port number")

(user_input, arguments) = Parsers.parse_args()

ip_address = user_input.ip
port_nmbrs = int(user_input.port)

try:
    # kodun bu kısmında bir baglantı açıyor.
    server_connect = socket.socket()
    server_connect.bind((str(ip_address), port_nmbrs))
    server_connect.listen()

except KeyboardInterrupt:
    print("pressed 'CTRL + C'")
    sys.exit()

except Exception as E:
    print(E)
    sys.exit()

try:
    subprocess.call(["clear"])
    t = datetime.today()
    print(f"Connection OK\t\t{t.year}.{t.month}.{t.day}\t{t.hour}:{t.minute}")
    print("communication will be done in half duplex\n\n")
    while True:
        (server_sock, server_addr) = server_connect.accept()
        while True:
            try:
                # Kullanıcının karşı tarafa veri iletmesini saglayan kısım.
                message = input("message enter . . . : ")
                server_sock.send(message.encode(encoding="UTF-8"))
                msgreceived = server_sock.recv(1024)

                data = server_sock.recv(1024)
                print(f"Client message  . . : \033[36m{data}\033[0m")
                server_sock.send(data)
                break

            except ConnectionRefusedError:
                server_sock.close()
                print(f"Connection Lost")
                sys.exit()

except KeyboardInterrupt:
    print("\npressed 'CTRL + C'")
    sys.exit()

except Exception as E:
    print(E)
    sys.exit()
