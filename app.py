import os
import mysql.connector
from dueno import Dueno
from menudueno import menuDueno
from menuinvernadero import MenuInvernadero
from menuUsuario import MenuUsu
from menuplanta import MenuPlanta
from menuregistro import MenuRegistro
conexion = mysql.connector.connect(user='jose',password='1234',database='invernadero')

cursor = conexion.cursor()

while True:
    os.system('cls')
    print("\n1) Menu Dueño")
    print("2) Menu Invernadero ")
    print("3) Menu Usuario ")
    print("4) Menu planta")
    print("5) Menu Registro")
    print("0) Salir");
    
    op = input(":")  
    if op == "1":
        os.system('cls')
        menuD= menuDueno(conexion,cursor)
    elif op == "2":
        os.system('cls')
        menuI = MenuInvernadero(conexion,cursor)
    elif op =="3":
        os.system('cls')
        menuU = MenuUsu(conexion,cursor)
    elif op =="4":
        os.system('cls')
        menuP =MenuPlanta(conexion,cursor)
    elif op =="5":
        os.system('cls')
        menuR =MenuRegistro(conexion,cursor)
    elif( op == "0"):
        os.system('cls')
        break;
    
    

#d = Dueno(conexion, cursor)
#d.crear('Jose','Valdez Gutierrez')
#print(d.recuperar())