

import socket  # Importa la biblioteca socket para la comunicación de red
import cv2  # Importa la biblioteca OpenCV para el procesamiento de imágenes y videos
import numpy as np  # Importa la biblioteca NumPy para operaciones numéricas eficientes

SERVER_ADDRESS = "24.199.78.243"  # Dirección IP del servidor
SERVER_PORT = 9090  # Puerto del servidor

s = socket.socket()  # Crea un objeto socket para la comunicación
# Establece una conexión con el servidor
s.connect((SERVER_ADDRESS, SERVER_PORT))

# Imprime un mensaje de conexión exitosa
print("Conectado al servidor en " + str((SERVER_ADDRESS, SERVER_PORT)))

video_frames = []  # Lista para almacenar los frames de video recibidos

while True:  # Bucle infinito para recibir y mostrar los frames del video
    # Recibe los primeros 4 bytes que representan el tamaño del siguiente frame de video
    frame_size = s.recv(4)

    if not frame_size:  # Verifica si no se recibió ningún dato en frame_size
        print("Fin de la transmisión del video")
        break  # Rompe el bucle si no se recibieron más frames

    # Convierte los bytes a un entero (orden big-endian)
    frame_size = int.from_bytes(frame_size, byteorder='big')

    # Crea una cadena de bytes vacía para almacenar los bytes del frame de video
    frame_bytes = b""
    remaining_bytes = frame_size  # Almacena el número de bytes que quedan por recibir

    while remaining_bytes > 0:  # Bucle para recibir todos los bytes del frame de video
        # Recibe un fragmento de bytes del frame de video (tamaño máximo de 4096 bytes)
        chunk = s.recv(min(remaining_bytes, 4096))

        if not chunk:  # Verifica si no se recibió ningún dato en chunk
            print("Error al recibir los bytes del frame")
            break  # Rompe el bucle si no se recibieron más bytes del frame

        frame_bytes += chunk  # Concatena los bytes recibidos al conjunto de bytes del frame
        # Resta la longitud del fragmento recibido a los bytes restantes por recibir
        remaining_bytes -= len(chunk)

    # Convierte los bytes del frame en un array NumPy de tipo uint8
    frame_array = np.frombuffer(frame_bytes, dtype=np.uint8)
    # Decodifica el array de bytes en una imagen OpenCV en color
    frame = cv2.imdecode(frame_array, cv2.IMREAD_COLOR)
    # Muestra la imagen del frame en una ventana llamada "Video del servidor"
    cv2.imshow("Video del servidor", frame)
    video_frames.append(frame)  # Agrega el frame a la lista de frames de video

    # Espera durante 1 ms y verifica si la tecla 'q' ha sido presionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # Rompe el bucle si se presionó la tecla 'q'

cv2.destroyAllWindows()  # Cierra todas las ventanas abiertas por OpenCV
s.close()  # Cierra la conexión del socket
