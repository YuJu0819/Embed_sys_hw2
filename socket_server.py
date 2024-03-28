import socket
import json
import numpy as np
import matplotlib.pyplot as plt

HOST = '172.20.10.14'  # IP address
PORT = 4000  # Port to listen on (use ports > 1023)

plt.ion()
legend_shown = False
dataX = []
dataY = []
dataZ = []
dataTime = []


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
            dataTime.append(obj['s'])
            dataX.append(obj['x'])
            dataY.append(obj['y'])
            dataZ.append(obj['z'])
            # obj['s']

            plt.plot(dataTime, dataX, 'b-', linewidth=0.5, label='pGyroDataX')  # x, y, z, gx, gy, gz
            plt.plot(dataTime, dataY, 'r-', linewidth=0.5, label='pGyroDataY')  # x, y, z, gx, gy, gz
            plt.plot(dataTime, dataZ, 'y-', linewidth=0.5, label='pGyroDataZ')  # x, y, z, gx, gy, gz
            plt.xlabel("sample num")
            plt.title("Gyro Data - sample num")
            plt.draw()
            if not legend_shown:
                plt.legend()
                legend_shown = True     
            plt.pause(0.0001)

