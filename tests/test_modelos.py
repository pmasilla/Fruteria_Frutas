from app.modelos import Producto, DAO_Productos, Ticket

def test_identificar_producto():
    #Compruebo que puedo comparar la id, el nombre y el precio unidad
    producto = Producto(5, "Lechuga", 0.9)

    assert producto.id == 5
    assert producto.nombre == "Lechuga"
    assert producto.precio_unitario == 0.9

def test_DAO_todos():
    #Creo un test para comprobar el funcionamiento de mostrar todos los productos
    #Creo una variable dando el path de la base de datos
    dao = DAO_Productos("data/productos_fruteria.sqlite")
    lista_productos = dao.todos()
    #Compruebo la longitud de la lista
    assert len(lista_productos) == 10
    #Compruebo que los valores son iguales a los que pido
    assert lista_productos[5]["id"] == 6
    assert lista_productos[5]["nombre"] == "Zanahoria"
    assert lista_productos[5]["precio_unitario"] == 0.4
    assert lista_productos[9]["id"] == 10
    assert lista_productos[9]["nombre"] == "Pimiento"
    assert lista_productos[9]["precio_unitario"] == 1
    assert lista_productos[9]["cantidad"] == 0

def test_añadir_producto_y_total():
    #Creo la lista de productos para el test
    lista_productos = [{"id": 1, "nombre": "Manzana", "precio_unitario": 0.5, "cantidad": 0, "subtotal": 0},
                    {"id": 2, "nombre": "Plátano", "precio_unitario": 0.3, "cantidad": 0, "subtotal": 0},
                    {"id": 3, "nombre": "Naranja", "precio_unitario": 0.7, "cantidad": 0, "subtotal": 0},
                    {"id": 4, "nombre": "Uvas", "precio_unitario": 1.2, "cantidad": 0, "subtotal": 0},
                    {"id": 5, "nombre": "Lechuga", "precio_unitario": 0.9, "cantidad": 0, "subtotal": 0}]
    #Añado la primera compra y compruebo la cantidad y el subtotal en el diccionario
    compra = Ticket(lista_productos)
    compra1 = compra.añadir_producto(5, 2)
    assert compra1[4]["cantidad"] == 2
    assert compra1[4]["subtotal"] == 1.8
    #Añado la segunda compra y compruebo todos los valores de las claves (solo por asegurar)
    compra2 = compra.añadir_producto(3, 5)
    assert compra2[2]["id"] == 3
    assert compra2[2]["nombre"] == "Naranja"
    assert compra2[2]["precio_unitario"] == 0.7
    assert compra2[2]["cantidad"] == 5
    assert compra2[2]["subtotal"] == 3.5
    #Compruebo que el total del ticket es la suma de los subtotales, (1.8 + 3.5 = 5.3)
    assert compra.total() == 5.3
    