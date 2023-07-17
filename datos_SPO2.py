import serial
import time
import statistics

class DatosSPO2:
    def __init__(self, COM="COM6", FR=115200) -> None:
        self.datos = []
        self.serialArduino = serial.Serial(COM, FR)
        time.sleep(1)

    def get_data(self):
        print('Midiendo, por favor mantenga una presión constante en el sensor con el dedo índice.')
        while len(self.datos) < 30:  # Almacenar 500 datos
            cad = self.serialArduino.readline().decode('ascii').strip()
            try:
                x, y = map(int, cad.split())
                if y == 1 and 85 <= x < 100:  # Cumple con los criterios
                    self.datos.append(x)
            except ValueError:
                pass

            print(cad)

        self.serialArduino.close()

    def get_value(self):
        media = statistics.mean(self.datos)
        desviacion_estandar = statistics.stdev(self.datos)

        datos_filtrados = [dato for dato in self.datos if media - 2 * desviacion_estandar <= dato <= media + 2 * desviacion_estandar]

        promedio = statistics.mean(datos_filtrados)

        return promedio
