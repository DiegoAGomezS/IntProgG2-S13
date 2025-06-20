import os
from models.estudiante import Estudiante

class EstudianteDAO:
    def __init__(self, archivo_path="data/estudiantes.txt"):
        self.archivo_path = archivo_path
        self.asegurar_directorio()
    
    def asegurar_directorio(self):
        """Asegura que el directorio data existe"""
        directorio = os.path.dirname(self.archivo_path)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)
    
    def guardar_estudiante(self, estudiante):
        """Guarda un estudiante en el archivo de texto"""
        try:
            with open(self.archivo_path, 'a', encoding='utf-8') as archivo:
                archivo.write(estudiante.to_file_format())
            return True
        except Exception as e:
            print(f"Error al guardar estudiante: {e}")
            return False
    
    def cargar_estudiantes(self):
        """Carga todos los estudiantes desde el archivo"""
        estudiantes = []
        try:
            if os.path.exists(self.archivo_path):
                with open(self.archivo_path, 'r', encoding='utf-8') as archivo:
                    for linea in archivo:
                        linea = linea.strip()
                        if linea:
                            datos = linea.split('|')
                            if len(datos) >= 9:
                                estudiante = Estudiante(
                                    datos[0], datos[1], datos[2], datos[3],
                                    float(datos[4]), float(datos[5]), float(datos[6])
                                )
                                estudiantes.append(estudiante)
        except Exception as e:
            print(f"Error al cargar estudiantes: {e}")
        return estudiantes
    
    def obtener_estudiantes_por_estado(self, estado):
        """Obtiene estudiantes filtrados por estado (APROBADO/DESAPROBADO)"""
        todos_estudiantes = self.cargar_estudiantes()
        return [est for est in todos_estudiantes if est.estado == estado]
    
    def existe_estudiante(self, cif):
        """Verifica si un estudiante ya existe por CIF"""
        estudiantes = self.cargar_estudiantes()
        return any(est.cif == cif for est in estudiantes)
    
    def generar_reporte(self):
        """Genera un reporte completo en archivo de texto"""
        estudiantes = self.cargar_estudiantes()
        aprobados = [est for est in estudiantes if est.estado == "APROBADO"]
        desaprobados = [est for est in estudiantes if est.estado == "DESAPROBADO"]
        
        reporte_path = "data/reporte_estudiantes.txt"
        try:
            with open(reporte_path, 'w', encoding='utf-8') as archivo:
                archivo.write("=" * 60 + "\n")
                archivo.write("           REPORTE DE ESTUDIANTES\n")
                archivo.write("=" * 60 + "\n\n")
                
                archivo.write(f"Total de estudiantes: {len(estudiantes)}\n")
                archivo.write(f"Estudiantes aprobados: {len(aprobados)}\n")
                archivo.write(f"Estudiantes desaprobados: {len(desaprobados)}\n\n")
                
                archivo.write("ESTUDIANTES APROBADOS:\n")
                archivo.write("-" * 40 + "\n")
                for est in aprobados:
                    archivo.write(f"{est}\n")
                
                archivo.write("\nESTUDIANTES DESAPROBADOS:\n")
                archivo.write("-" * 40 + "\n")
                for est in desaprobados:
                    archivo.write(f"{est}\n")
            
            print(f"Reporte generado en: {reporte_path}")
            return True
        except Exception as e:
            print(f"Error al generar reporte: {e}")
            return False

