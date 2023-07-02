import re
import socket

SERVER_ADDRESS = '192.168.1.3'
SERVER_PORT = 9090

s = socket.socket()
s.connect((SERVER_ADDRESS, SERVER_PORT))
print('Servidor levantado:' + str((SERVER_ADDRESS, SERVER_PORT)))

while True:
  try:
    valor1 = input("[CLIENTE]: Ingrese un primer valor numerico:")
    valor2 = input("[CLIENTE]: Ingrese un segundo valor numerico:")
  except EOFError:
      print("Error: inconveniente en la captura de valores")
  
  digitos = [valor1, valor2]

  # Validaciones
  if any(not re.match(r'^\d+(\.\d+)?$' or not valor , valor) for valor in digitos):
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
