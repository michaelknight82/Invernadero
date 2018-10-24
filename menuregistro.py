import os
from registro import Registro
from datetime import datetime,date
class MenuRegistro:
    def __init__(self, conexion, cursor,):
        self.registro = Registro(conexion, cursor)
        
        while True:
            os.system('cls')
            print("1) Agregar registro")
            print("2) Buscar registro")
            print("0) Salir")
            op = input(":")
            
            if op == "1":
                os.system('cls')
                self.agregar()
            elif op == "2":
                os.system('cls')
                self.buscar()
                print('       Registro guardado con exito')
                os.system('pause')
            elif op == "0":
                os.system('cls')
                break
            
    def agregar(self):
        #fecha = datetime.now().date();
        dia = input("Dia: ")
        mes = input("Mes: ")
        year = input("Año: ")
        fecha = date(int(year),int(mes),int(dia))
        ph = input("Ph: ")
        luz = input("Luz: ")
        humedad = input("Humedad: ")
        co2 = input("CO2: ")
        id_planta = input("Id Planta: ")
        self.registro.agregar(fecha,ph,luz,humedad,co2,id_planta)
        
        
    def buscar(self):
        id_planta = input("Id Planta: ")
        resultados = self.registro.buscar(id_planta)
        
        for p in resultados:
            #print(p)
            print("{0:2} {1:10} {2:10} {3:10} {4:10} {5:10}".format(p[0], str(p[1]),p[2],p[3],p[4],p[5]))