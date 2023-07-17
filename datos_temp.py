import serial
import time
import statistics

class DatosTemp:
    def __init__(self,COM="COM9",FR=9600) -> None:
        self.datos = []
        self.serialArduino = serial.Serial(COM, FR)
        time.sleep(1)

    def get_data(self):
        while len(self.datos) < 10:  # Almacenar 20 mediciones
            cad = self.serialArduino.readline().decode('utf-8')
            valor = cad[:4]
            try:
                valor_float = float(valor)
                if 31 < valor_float < 45:  # Cumple con los criterios
                    self.datos.append(valor_float)
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
