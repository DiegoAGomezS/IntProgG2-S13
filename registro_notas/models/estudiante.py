class Estudiante:
    def __init__(self, cif, nombres, apellidos, asignatura, nota1, nota2, nota3):
        self.cif = cif
        self.nombres = nombres
        self.apellidos = apellidos
        self.asignatura = asignatura
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)
        self.nota3 = float(nota3)
        self.nota_final = self.calcular_promedio()
        self.estado = self.determinar_estado()
    
    def calcular_promedio(self):
        """Calcula el promedio de las 3 notas"""
        return round((self.nota1 + self.nota2 + self.nota3) / 3, 2)
    
    def determinar_estado(self):
        """Determina si el estudiante aprobó o desaprobó (mínimo 70 puntos)"""
        return "APROBADO" if self.nota_final >= 70 else "DESAPROBADO"
    
    def __str__(self):
        return f"CIF: {self.cif}, {self.nombres} {self.apellidos}, {self.asignatura}, Promedio: {self.nota_final}, Estado: {self.estado}"
    
    def to_file_format(self):
        """Formato para guardar en archivo de texto"""
        return f"{self.cif}|{self.nombres}|{self.apellidos}|{self.asignatura}|{self.nota1}|{self.nota2}|{self.nota3}|{self.nota_final}|{self.estado}\n"

