import serial
import time
import statistics

class DatosHR:
    def __init__(self, COM="COM6", FR=115200) -> None:
        self.datos = []
        self.serialArduino = serial.Serial(COM, FR)
        time.sleep(1)

    def get_data(self):
        t0= time.time()
        while len(self.datos) < 750:  # Almacenar 200 datos
            tf = time.time()
            if tf-t0 > 10:
                cad = self.serialArduino.readline().decode('utf-8').strip()
                try:
                    valor = float(cad)
                    if 25 < valor < 135:  # Cumple con los criterios
                        self.datos.append(valor)
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
