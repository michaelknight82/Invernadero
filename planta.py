class Planta:
    def __init__(self, conexion, cursor):
        self.conexion = conexion
        self.cursor = cursor
        
    def agregar(self, fecha,cultivo ,id_clasi, id_inv):
        insertar = ('INSERT INTO planta(fecha, cultivo, id_clasi,id_inv) VALUES(%s, %s, %s, %s)')
        self.cursor.execute(insertar,(fecha,cultivo, id_clasi,id_inv))
        self.conexion.commit()
        
    def buscar(self,id_inv):
        select = ("SELECT * FROM planta WHERE id_inv=%s")
        self.cursor.execute(select,(id_inv,))
        resultados = self.cursor.fetchall()
        return resultados