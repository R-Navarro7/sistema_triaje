import serial
import time

archivo = open('D:\\Taller_Proyectos\\datos_HR.txt','w')
serialArduino = serial.Serial("COM3",115200)
time.sleep(1)

while True:
    cad = serialArduino.readline().decode('ascii')
    print(cad)

    archivo.write(cad)
