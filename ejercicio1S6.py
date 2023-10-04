class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_detalle(self):
        return f"Nombre: {self.nombre}\nPrecio: ${self.precio}\nCategoría: {self.categoria}"

class Electronico(Producto):
    def __init__(self, nombre, precio, categoria, marca, modelo):
        super().__init__(nombre, precio, categoria)
        self.marca = marca
        self.modelo = modelo


    def mostrar_detalle(self):
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre}\nMarca: {self.marca}\nModelo: {self.modelo}"


class Alimenticio(Producto):
    def __init__(self, nombre, precio, categoria, fecha_vencimiento):
        super().__init__(nombre, precio, categoria)
        self.fecha_vencimiento = fecha_vencimiento

    def mostrar_detalle(self):
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre}\nFecha de Vencimiento: {self.fecha_vencimiento}"


class Vestimenta(Producto):
    def __init__(self, nombre, precio, categoria, talla, color):
        super().__init__(nombre, precio, categoria)
        self.talla = talla
        self.color = color

    def mostrar_detalle(self):
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre}\nTalla: {self.talla}\nColor: {self.color}"

# Ejemplo de uso:
producto_electronico = Electronico("Smartphone", 599.99, "Electrónico", "Samsung", "Galaxy S22")
producto_alimenticio = Alimenticio("Leche", 2.99, "Alimenticio", "2023-10-20")
producto_vestimenta = Vestimenta("Camiseta", 19.99, "Vestimenta", "M", "Azul")

print("Detalles del Producto Electrónico:")
print(producto_electronico.mostrar_detalle())
print("\nDetalles del Producto Alimenticio:")
print(producto_alimenticio.mostrar_detalle())
print("\nDetalles del Producto de Vestimenta:")
print(producto_vestimenta.mostrar_detalle())
