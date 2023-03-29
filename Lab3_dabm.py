import serial
import csv
import os

arduino = serial.Serial('COM4', 9600)
V_min = 0
V_max = 730


brillo_min = input("Ingrese el valor minimo que desea en un rango de 0-254")
brillo_max = input("Ingrese el valor minimo que desea en un rango de-255")
brillo_min=int(brillo_min)
brillo_max=int(brillo_max)
while True:
    # Lectura del valor del sensor para la comunicación serial
    V_sensor = int(arduino.readline().strip())
    
    # Mapeo
    brightness = int((V_sensor - V_min) / (V_max - V_min) * (brillo_max - brillo_min) + brillo_min)
    
    # Envio de  la orden 
    arduino.write(str(brightness).encode() + b'\n')
    data = [[brillo_min,brillo_max]]
    ruta_archivo = 'pruebas\Archivos'
    nombre_archivo = 'Valor maximo    Valor minimo .csv'
    ruta_completa = os.path.join(ruta_archivo, nombre_archivo)
    with open(ruta_completa, 'w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerows(data)