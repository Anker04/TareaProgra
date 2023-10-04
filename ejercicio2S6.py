class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def describir_rol(self):
        return f"Soy un empleado de la empresa."

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    def describir_rol(self):
        return f"Soy un gerente del departamento {self.departamento}. Gestiono y superviso el trabajo de otros empleados."

class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, especialidad):
        super().__init__(nombre, edad, salario)
        self.especialidad = especialidad

    def describir_rol(self):
        return f"Soy un ingeniero especializado en {self.especialidad}. Trabajo en el desarrollo y mantenimiento de proyectos técnicos."

class Asistente(Empleado):
    def __init__(self, nombre, edad, salario, supervisor):
        super().__init__(nombre, edad, salario)
        self.supervisor = supervisor

    def describir_rol(self):
        return f"Soy un asistente de {self.supervisor}. Ayudo en tareas administrativas y de organización."

# Ejemplo de uso:
gerente1 = Gerente("Ana", 40, 60000, "Ventas")
ingeniero1 = Ingeniero("Carlos", 28, 75000, "Inteligencia Artificial")
asistente1 = Asistente("Laura", 22, 30000, "Gerente de Proyectos")

print("Descripción del Gerente:")
print(gerente1.describir_rol())
print("\nDescripción del Ingeniero:")
print(ingeniero1.describir_rol())
print("\nDescripción del Asistente:")
print(asistente1.describir_rol())
