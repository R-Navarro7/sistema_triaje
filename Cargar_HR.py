import subprocess

# Ruta al archivo .ino
ino_file_path = r'HR_arduino/HR_arduino.ino'

# Puerto del Arduino
arduino_port = 'COM6'  # Reemplaza 'COMX' con el puerto correspondiente a tu Arduino

# Comando para compilar y cargar el archivo .ino
command = f'arduino-cli compile --upload --port {arduino_port} {ino_file_path}'

# Ejecutar el comando
subprocess.call(command, shell=True)
