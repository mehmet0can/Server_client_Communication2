import sys
import socket
import subprocess
from datetime import datetime
from optparse import OptionParser

# HALF DUPLEX haberleşme sağlayan python kodu
# Bir önceki kodun değiştirilimş halidir

Parsers = OptionParser()
# Kullanıcıdan verilerini parametre olarak girebilmesini sağlamak için
# bir OptionParser oluşturdum.
Parsers.add_option("-i", dest="ip", help="IP address")
Parsers.add_option("-p", dest="port", help="Port number")

(user_input, argumets) = Parsers.parse_args()

ip_address = user_input.ip
port_nmbrs = int(user_input.port)

try:
    subprocess.call(["clear"])
    t = datetime.today()
    print(f"Connection OK\t\t{t.year}.{t.month}.{t.day}\t{t.hour}:{t.minute}")
    print("communication will be done in half duplex\n\n")
    while True:
        try:
            # Kullanıcının karşı taraf ile bağlantı açmasını ve veri iletmesini saglayan kısım. 
            client_socket = socket.socket()
            client_socket.connect((str(ip_address), port_nmbrs))

            data = client_socket.recv(1024)
            print(f"Server message  . . : \033[36m{data}\033[0m")
            client_socket.send(data)

            message = input("message enter . . . : ")
            client_socket.send(message.encode(encoding="UTF-8"))
            msgreceived = client_socket.recv(1024)

            if client_socket.close():
                print("connection closed")

        except ConnectionRefusedError:
            print(f"Connection Lost")
            sys.exit()

except KeyboardInterrupt:
    print("\npressed 'CTRL + C'")
    sys.exit()

except Exception as E:
    print(E)
    sys.exit()
