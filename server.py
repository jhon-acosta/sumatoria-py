import socket
from functools import reduce

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 9090

s = socket.socket()
s.bind((SERVER_ADDRESS, SERVER_PORT))
s.listen()

print("Escuchando en el servidor: " + str((SERVER_ADDRESS, SERVER_PORT)))

while True:
  c, addr = s.accept()
  while True:
    data = c.recv(2048)

    if not data:
      print("[SERVIDOR]: Fin de transmisión desde el cliente")
      break

    data = data.decode()
    data = [format(float(num), '.2f') for num in data.split(',')]
    data = list(map(float, data))
    data = reduce(lambda acc, val: acc + val, data, 0)

    print(f'[SERVIDOR]: Sumatoria {data}')

    c.send(f'[SERVIDOR]: La sumatoria es: {data} //'.encode())

  c.close() 