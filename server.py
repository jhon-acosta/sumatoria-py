import socket
from functools import reduce

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 9090

s = socket.socket()
s.bind((SERVER_ADDRESS, SERVER_PORT))
s.listen()

print("Escuchando en el servidor: " + str((SERVER_ADDRESS, SERVER_PORT)))


def onVeces(number):
    array = []
    for i in range(1, round(number) + 1):
        array.append(i)
    return array


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
        print(f'[SERVIDOR]: Sumatoria de ambos números es {data}')

        nArr = onVeces(data)
        print(f'[SERVIDOR]: Array de n veces de sumatoria es', nArr)

        nArrTotal = reduce(lambda acc, val: acc + val, nArr, 0)
        response = '[SERVIDOR]: Sumatoria mas n veces es: ' + \
            str(data + nArrTotal)
        print(response)

        c.send(response.encode())

    c.close()
