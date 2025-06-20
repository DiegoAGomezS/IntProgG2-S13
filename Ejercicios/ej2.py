from ej1 import RegTrabajador

class TrabajadoresDao:
    def __init__(self):
        self.trabajadores = []
    
    def crear_trabajadores(self, nombres, apellidos, cargo, salario_base):
        trabajador = RegTrabajador(nombres, apellidos, cargo, salario_base)
        self.trabajadores.append(trabajador)
        return f"Se ha registrado correctamente la información"
    
    def listar_trabajadores(self):
        if not self.trabajadores:
            return f"No hay trabajadores registrados"
        else:
            for i, trabajador in enumerate(self.trabajadores):
                return f"{i+1}. {trabajador}"
    
    def actualizar_trabajador(self, indice, nombres=None, apellidos=None, cargo=None, salario_base=None):
        if 0 <= indice < len(self.trabajadores):
            trabajador = self.trabajadores[indice]
            if nombres:
                trabajador.nombres = nombres
            if apellidos:
                trabajador.apellidos = apellidos
            if cargo:
                trabajador.cargo = cargo
            if salario_base:
                trabajador.salario_base = salario_base
            return f"Información actualizada correctamente"
        else:
            return f"Índice de trabajador no válido"
    
    def eliminar_trabajador(self, indice):
        if 0 <= indice < len(self.trabajadores):
            eliminado = self.trabajadores[indice]
            return f"Información eliminada correctamente"
        else:
            return f"Trabajador no encontrado"