import sys
import csv
import serial
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
x=0
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):    
        self.setWindowTitle('Ingreso al sistema DABM')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        label_username = QLabel('Usuario:')
        layout.addWidget(label_username)

        self.edit_username = QLineEdit()
        layout.addWidget(self.edit_username)

        label_password = QLabel('Contraseña:')
        layout.addWidget(label_password)

        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.edit_password)

        btn_load_file = QPushButton("Cargar archivo")
        btn_load_file.clicked.connect(self.load_file)
        layout.addWidget(btn_load_file)

        btn_ingresar = QPushButton("Ingresar")
        btn_ingresar.clicked.connect(self.auth)
        layout.addWidget(btn_ingresar)

        self.setLayout(layout)

    def load_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Cargar archivo", "", "CSV files (*.csv)")
        if file_path:
            self.user_data = self.read_csv(file_path)

    def read_csv(self, file_path):
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            user_data = []
            for row in reader:
                user_data.append((row[0], row[1]))
            return user_data

    def auth(self):
        username = self.edit_username.text()
        password = self.edit_password.text()
        


        if self.validate_credentials(username, password):
            print('Acceso concedido')
            x=("Acceso concedido")
        else:
            print('Acceso denegado')
            x=("Acceso denegado")


    def validate_credentials(self, username, password):
        for user_tuple in self.user_data:
            if user_tuple[0] == username and user_tuple[1] == password:
                return True
        

            
    



        return False
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())

if x=="Acceso concedido":
    arduino = serial.Serial('COM4', 9600)
    V_min = 0
    V_max = 730
    brillo_min = input("Ingrese el valor minimo que desea en un rango de 0-254")
    brillo_max = input("Ingrese el valor minimo que desea en un rango de-255")
    brillo_min=int(brillo_min)
    brillo_max=int(brillo_max)
    while True:
         #Lectura del valor del sensor para la comunicación serial
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
