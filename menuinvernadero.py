import os
from invernadero import Invernadero

class MenuInvernadero:
    def __init__ (self,conexion,cursor):
        self.inv = Invernadero(conexion,cursor)
        while True:
            os.system('cls')
            print("1) Agregar invernadero")
            print("2) Mostrar inveraderos")
            print("0) Salir ")
            op = input(":")
            
            if op == "1":
                os.system('cls')
                self.agregar()
            elif op == "2":
                os.system('cls')
                self.mostrar()
                os.system('pause')
            elif op == "0":
                os.system('cls')
                break;
                
    def agregar(self):
        nombre = input("Nombre invernadero: ")
        ubicacion = input("Ubicacion Invernadero ")
        id_dueno = input("id_dueno: ")
        self.inv.crear(nombre,ubicacion,id_dueno)
            
    def mostrar(self):
        resultados = self.inv.recuperar()
        for r in resultados:
            print ("{0:3} {1:10} {2:10} {3:3}".format(r[0], r[1], r[2], r[3]))