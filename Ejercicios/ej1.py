class RegTrabajador:
    def __init__(self, nombres, apellidos, cargo, salario_base):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cargo = cargo
        self.salario_base = salario_base
        
        def __str__(self):
            return f"Nombres: {self.nombres} | Apellido: {self.apellidos} | Cargo: {self.cargo} | Salario: {self.salario_base}"