from app.modelos import Producto, DAO_Productos, Ticket
from simple_screen import DIMENSIONS, locate, Input, cls, Screen_manager
from app.vistas import Vista_Input, Vista_Nombre_Fruteria, Vista_Productos, Input_cantidad, Input_id

class Fruteria_Fruta:
    def __init__(self):
        self.titulo = Vista_Nombre_Fruteria("FRUTERIA FRUTA")
        self.dao_producto = DAO_Productos("data\\productos_fruteria.sqlite")
        self.lista_productos = self.dao_producto.todos()
        self.compra = Ticket(self.lista_productos)
        self.vista_productos = Vista_Productos(self.lista_productos, 0, 2)
        self.producto_cliente = Input_id("Introduzca el código de producto que desea, o 0 para terminar: ", 70, 16)
        self.cantidad_cliente = Input_cantidad("Introduzca la cantidad deseada:                                ", 70, 17)
        self.continuar = Vista_Input("Desea continuar? s/n ", 70, 18)


    def run(self):
        with Screen_manager:
            while True:
                cls()
                self.titulo.paint()
                self.vista_productos.paint()
                producto = self.producto_cliente.paint()
                
                if producto == 0:
                    continuar = self.continuar.paint()
                    if continuar.lower() == "s":
                        self.compra = Ticket(self.lista_productos)
                        self.compra.lista_productos_cantidades = self.lista_productos
                        continue
                    else:
                        break
                cantidad = self.cantidad_cliente.paint()
                    
                
                    
                producto = int(producto)
                cantidad = int(cantidad)
                self.compra.añadir_producto(producto, cantidad)
            
        