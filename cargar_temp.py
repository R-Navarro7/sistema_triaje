import subprocess

# Ruta al archivo .ino
ino_file_path = r'temperatura_arduino/temperatura_arduino.ino'

# Puerto del Arduino
arduino_port = 'COM9'  # Reemplaza 'COMX' con el puerto correspondiente a tu Arduino

# FQBN del Arduino
arduino_fqbn = 'arduino:avr:uno'  # Reemplaza con el FQBN específico de tu Arduino

# Comando para compilar y cargar el archivo .ino
command = f'arduino-cli compile --upload --port {arduino_port} -b {arduino_fqbn} {ino_file_path}'

# Ejecutar el comando
subprocess.call(command, shell=True)
