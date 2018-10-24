import os
from planta import Planta
from datetime import datetime,date
class MenuPlanta:
    def __init__(self, conexion, cursor,):
        self.planta = Planta(conexion, cursor)
        
        while True:
            os.system('cls')
            print("1) Agregar planta")
            print("2) Buscar planta")
            print("0) Salir")
            op = input(":")
            
            if op == "1":
                os.system('cls')
                self.agregar()
            elif op == "2":
                os.system('cls')
                self.buscar()
                os.system('pause')
            elif op == "0":
                os.system('cls')
                break
            
    def agregar(self):
        #fecha = datetime.now().date();
        dia = input("Dia: ")
        mes = input("Mes:")
        year = input("Año: ")
        fecha = date(int(year),int(mes),int(dia))
        cultivo = input("Cultivo: ")
        id_clasi = input("Id clasificacion: ")
        id_inv = input("Id invernadero: ")
        self.planta.agregar(fecha,cultivo,id_clasi,id_inv)
        
    def buscar(self):
        id_inv = input("Id invernadero: ")
        resultados = self.planta.buscar(id_inv)
        
        for p in resultados:
            #print(p)
            print("{0:2} {1:10} {2:10}".format(p[0], str(p[1]),p[2]))