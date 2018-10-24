import os
from usuario import Usuario
import getpass
class MenuUsu:
    def __init__(self,conexion,cursor):
        self.usuario = Usuario(conexion, cursor)
        
        while True:
            os.system('cls')
            print("1) Crear usuario")
            print("2) Login")
            print("0) Salir")
            op = input(":")
            
            if op == '1':
                self.capturar()
                os.system('cls')
            elif op == "2":
                os.system('cls')
                self.login()
                os.system('pause')
            elif op == '0':
                os.system('cls')
                break
            
    def capturar(self):
        usuario = input("Correo: ")
        contra = getpass.getpass("Contraseña: ")
        tipo = input("tipo: ")
        
        self.usuario.crear(usuario,contra,tipo)
        
    def login(self):
        usuario = input("Correo: ")
        contra = getpass.getpass("Contraseña: ")
        
        if self.usuario.login(usuario,contra):
            print("Bienvenido")
        else:
            print("Usuario/contraseña incorrectos")
        
    
        