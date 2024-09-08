from simple_screen import locate, DIMENSIONS, Input
from app.modelos import Ticket, DAO_Productos

class Vista_Nombre_Fruteria:
    def __init__(self, texto, y = 0):
        self.texto = texto
        self.y = y
    def paint(self):
        x = (DIMENSIONS.w - len(self.texto)) // 2
        locate(x, self.y,self.texto)
        

class Vista_Productos:
    def __init__(self, lista_productos,x, y):
        self.lista_productos = lista_productos
        self.x = x
        self.y = y

    def paint(self):

        separador = ("*" * 62)
        encuadrado = (DIMENSIONS.w - len(separador)) // 2

        
        locate(encuadrado, self.y, ("*" * 62))
        locate(encuadrado, self.y + 1, "| ID    ")
        locate(encuadrado + 5, self.y + 1, "| NOMBRE PRODUCTO ")
        locate(encuadrado + 23, self.y + 1, "| PRECIO UNIDAD ")
        locate(encuadrado + 39, self.y + 1, "| CANTIDAD")
        locate(encuadrado + 49, self.y + 1, " | SUBTOTAL |")   
        locate(encuadrado, self.y + 2, ("*" * 62))              

        for index, producto, in enumerate(self.lista_productos):
            locate(encuadrado, self.y + 3 + index, f"| {producto["id"]:2} | {producto["nombre"]:15} |{producto["precio_unitario"]:14} | {producto["cantidad"]:8} |{round(producto["subtotal"], 2):9} |")
        locate(encuadrado, self.y + 13, ("*" * 62))

        total = sum(producto["subtotal"] for producto in self.lista_productos)
        locate(encuadrado + 44, self.y + 14, f"TOTAL |  {total:.2f} €  |")


class Vista_Input:

    def __init__(self, texto, x, y):
        self.texto = texto
        self.y = y
        self.x = x
        
    def paint(self):
        locate(self.x, self.y, self.texto)
        return Input()
    
class Input_cantidad(Vista_Input):
    def paint(self):
        while True:
            cantidad_introducida = super().paint()

            try:
                cantidad = int(cantidad_introducida)
                if cantidad <= 0:
                    locate(self.x, self.y + 1, f"La cantidad debe ser un numero entero mayor que 0")
                else: 
                    return cantidad
            except ValueError:
                locate(self.x, self.y+1, f"Introduzca un numero entero válido")

class Input_id(Vista_Input):
    def paint(self):
        while True:
            id_introducida = super().paint()
            
            
            try:
                id = int(id_introducida)
                if id < 0 or id > 10:
                    locate(self.x,self.y+1, f"Introduzca un ID válido (0 para salir)")
                else:
                    return id
            except ValueError:
                locate(self.x, self.y+1, f"Introduzca un numero entero válido")

