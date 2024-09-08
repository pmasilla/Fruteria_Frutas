from abc import ABC
import sqlite3


class Producto():
        
    def __init__(self, id, nombre, precio_unitario):
        self.id = id
        self.nombre = nombre
        self.precio_unitario = precio_unitario

    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.id == other.id and self.nombre == other.nombre and self.precio_unitario == other.precio_unitario
        return False
    def __hash__(self):
        return hash((self.id, self.nombre, self.precio_unitario))
    def __repr__(self):
        return f'Producto({self.id}, "{self.nombre}", {self.precio_unitario})'

class DAO(ABC):
    def todos(self):
        pass

class DAO_Productos(DAO):    
    def __init__(self, path):
        self.path = path

    #En la funcion todos he decidido añadir al diccionario que me va a devolver, las claves cantidad y subtotal, para ayudarme en la clase Ticket, no estoy del todo seguro si es buena práctica,
    #la única manera que se me ocurría de llevar un contador de cantidad y subtotal era añadiendola al diccionario con valor predeterminado 0, como vimos previamente en zoo, supongo que habrá otra manera, estoy abierto a correcciones.
    
    def todos(self):
        con = sqlite3.connect("data/productos_fruteria.sqlite")
        cur = con.cursor()
        cur.execute("select id, nombre, precio_unitario from Productos")
        lista_producto_cantidades = []
        for fila in cur.fetchall():
            lista_producto_cantidades.append({
                "id": fila[0],
                "nombre": fila[1],
                "precio_unitario": fila[2],
                "cantidad":0,
                "subtotal":0
                })
        con.close()
        return lista_producto_cantidades
    

class Ticket():
    def __init__(self, lista_productos_cantidades):
        self.lista_productos_cantidades = lista_productos_cantidades


    def añadir_producto(self, id: int, cantidad: int):
        #Itinero por la lista de productos, cuando la id coincide con alguna del diccionario, sumo la cantidad dada a la clave "cantidad"
        for producto in self.lista_productos_cantidades:
            if producto["id"] == id:
                producto["cantidad"] = producto["cantidad"] + cantidad
                producto["subtotal"] = producto["precio_unitario"] * producto["cantidad"]
            

        return self.lista_productos_cantidades
    
    def total(self):
        total = 0
        for producto in self.lista_productos_cantidades:
            total += producto["subtotal"]
        return total