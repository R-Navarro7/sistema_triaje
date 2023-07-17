import subprocess
import datos_temp
import datos_SPO2
import datos_HR
import sbc

# Comando para compilar y cargar el archivo .ino
command = f'python cargar_temp.py'
# Ejecutar el comando
subprocess.call(command, shell=True)


arduino_temp = datos_temp.DatosTemp(COM='COM4')

data_temp = arduino_temp.get_data()
print('Finished getting data.')
val_temp = arduino_temp.get_value()

print('Promedio: ', val_temp)

# Comando para compilar y cargar el archivo .ino
command = f'python Cargar_SPO2.py'
# Ejecutar el comando
subprocess.call(command, shell=True)

arduino_SPO2 = datos_SPO2.DatosSPO2()
data_SPO2 = arduino_SPO2.get_data()
val_SPO2 = arduino_SPO2.get_value()
print('Promedio: ', val_SPO2)

# Comando para compilar y cargar el archivo .ino
command = f'python Cargar_HR.py'
# Ejecutar el comando
subprocess.call(command, shell=True)

arduino_HR = datos_HR.DatosHR()
data_HR = arduino_HR.get_data()
val_HR = arduino_HR.get_value()
print('Promedio: ', val_HR)

val_temp_norm = (val_temp - 37)/(44-37)
val_SPO2_norm = (val_SPO2 - 100)/(100 - 85)
val_HR_norm = (val_HR - 80)/(135-80)

SBC = sbc.SistemaExperto()
result = SBC.inference_machine(val_temp_norm, val_SPO2_norm, val_HR_norm)


print('Promedios: ', val_temp, val_SPO2, val_HR)
print('Promedios Normalizados: ', val_temp_norm, val_SPO2_norm, val_HR_norm)
print(f'Categoría de triaje: {result[0]}\nGrado de certeza: {result[1]*100}%')


