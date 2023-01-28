import time

import serial

class PyArduinoEmisor:

    PUERTO = "COM3"
    BAUDIOS = 9600
    serialArduino = serial.Serial(PUERTO,BAUDIOS)
    time.sleep(1)
    # x = ""
    # cad = ""
    while True:
        cad = serialArduino.readline().decode("ascii")
        print(cad)
        # if cad != x:
        #     print("Cambio")
        # print(x)
        # x = cad
