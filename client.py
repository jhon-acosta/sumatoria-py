import re
import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 9090

s = socket.socket()
s.connect((SERVER_ADDRESS, SERVER_PORT))
print('Servidor levantado:' + str((SERVER_ADDRESS, SERVER_PORT)))

while True:
  try:
    data = input("[CLIENTE]: Ingrese un valor numerico:")
  except EOFError:
      print("Error: inconveniente en la captura de valores")
  
  digitos = data.split(',')

  # Validaciones
  if not data:
      print("[CLIENTE]: No puedo enviar datos vacios")
      continue
  elif len(digitos) != 2:
      print("Ingrese dos valores númericos separados por una (,). Ej: 1,5.2")
      continue
  elif any(not re.match(r'^\d+(\.\d+)?$'  , valor) for valor in digitos):
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
