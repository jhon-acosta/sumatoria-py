import re
import socket

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 9090

s = socket.socket()
s.connect((SERVER_ADDRESS, SERVER_PORT))
print('Servidor levantado:' + str((SERVER_ADDRESS, SERVER_PORT)))

while True:
    try:
        num1 = input("[CLIENTE]: Ingrese un primer valor numerico:")
        num2 = input("[CLIENTE]: Ingrese un segundo valor numerico:")
    except EOFError:
        print("Error: inconveniente en la captura de valores")

    digitos = [num1, num2]

    # Validaciones
    if any(not re.match(r'^\d+(\.\d+)?$' or not valor, valor) for valor in digitos):
        print("[CLIENTE]: Algun valor ingresado no es numerico")
        continue

    data = ','.join(digitos)
    s.send(data.encode())

    data = s.recv(2048)
    if not data:
        print("[CLIENTE]: Servidor habilitado")
        break
    else:
        print(data)

s.close()
