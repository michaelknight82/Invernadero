class Registro:
    def __init__(self, conexion, cursor):
        self.conexion = conexion
        self.cursor = cursor
        
    def agregar(self, fecha,ph,luz,humedad,co2,id_planta):
        insertar = ("INSERT INTO registro(fecha, ph, luz, humedad, co2, id_planta) VALUES(%s, %s, %s, %s, %s, %s)")
        self.cursor.execute(insertar,(fecha,ph,luz,humedad,co2, id_planta))
        self.conexion.commit()
        
    def buscar(self,id_planta):
        select = ("SELECT * FROM registro WHERE id_planta=%s")
        self.cursor.execute(select,(id_planta,))
        resultados = self.cursor.fetchall()
        return resultados