import cv2
import socket
import pickle
import struct

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 9998

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print('Esperando conexión del cliente...')

# Aceptar la conexión del cliente
client_socket, address = server_socket.accept()
print('Cliente conectado:', address)

# Abrir el video
video = cv2.VideoCapture('/home/jhon/Downloads/mich.mp4')

# Obtener el tamaño del video (ancho x alto)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Enviar el tamaño del video al cliente
size = struct.pack('!ii', width, height)
client_socket.sendall(size)

while video.isOpened():
    # Leer el siguiente cuadro de video
    ret, frame = video.read()

    if ret:
        # Codificar el cuadro en formato de bytes
        data = pickle.dumps(frame)

        # Obtener la longitud de los datos codificados
        size = struct.pack('!i', len(data))

        # Enviar la longitud de los datos al cliente
        client_socket.sendall(size)

        # Enviar los datos al cliente
        client_socket.sendall(data)

    else:
        # Finalizar la transmisión del video
        break

# Cerrar la conexión con el cliente
client_socket.close()

# Cerrar el socket del servidor
server_socket.close()
