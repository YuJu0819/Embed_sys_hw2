import socket
import json
import numpy as np
import matplotlib.pyplot as plt

HOST = '172.20.10.14'  # IP address
PORT = 4000  # Port to listen on (use ports > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Starting server at: ", (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print("Connected at", addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print("Received from socket server:", data)
            if (data.count('{') != 1):
                # Incomplete data are received.
                choose = 0
                buffer_data = data.split('}')
                while buffer_data[choose][0] != '{':
                    choose += 1
                data = buffer_data[choose] + '}'
            obj = json.loads(data)
            t = obj['s']
            plt.plot(t, obj['x'], 'bo-', linewidth=2, label='pGyroDataX')  # x, y, z, gx, gy, gz
            plt.plot(t, obj['y'], 'ro-', label='pGyroDataY')  # x, y, z, gx, gy, gz
            plt.plot(t, obj['z'], 'yo-', label='pGyroDataZ')  # x, y, z, gx, gy, gz
            plt.xlabel("sample num")
            plt.pause(0.0001)
