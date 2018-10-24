import os
from dueno import Dueno
class menuDueno:
    def __init__ (self,conexion,cursor):
        self.dueno = Dueno(conexion,cursor)
        while True:
            os.system('cls')
            print("\n1) Agregar dueño")
            print("2) Mostrar Dueños")
            print("0) Salir ")
            op = input(":")
            
            if op == "1":
                os.system('cls')
                self.agregar();
            elif op == "2":
                os.system('cls')
                self.mostar();
                os.system('pause')
            elif op == "0":
                os.system('cls')
                break;
                
    def agregar(self):
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        self.dueno.crear(nombre,apellidos)
    def mostar(self):
        resultados = self.dueno.recuperar()
        for r in resultados:
            print("{0:3} {1:10} {2:15}".format(r[0], r[1],r[2]))