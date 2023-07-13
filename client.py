import socket
import pickle
import struct
import cv2

# Configuración del servidor
HOST = '0.0.0.0'
PORT = 9999

# Crear un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Recibir el tamaño del video del servidor
size_data = client_socket.recv(8)
width, height = struct.unpack('!ii', size_data)

# Crear una ventana para mostrar el video
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Video', width, height)

while True:
    # Recibir la longitud de los datos del servidor
    size_data = client_socket.recv(4)
    size = struct.unpack('!i', size_data)[0]

    # Recibir los datos del servidor
    data = b''
    while len(data) < size:
        packet = client_socket.recv(size - len(data))
        if not packet:
            break
        data += packet

    # Si no se reciben datos, finalizar la recepción
    if not data:
        break

    # Deserializar los datos y convertirlos en un cuadro de imagen
    frame = pickle.loads(data)

    # Mostrar el cuadro de imagen en la ventana
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cerrar la ventana y la conexión con el servidor
cv2.destroyAllWindows()
client_socket.close()
