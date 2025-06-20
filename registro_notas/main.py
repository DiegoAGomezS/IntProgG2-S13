from models.estudiante import Estudiante
from dao.estudiante_dao import EstudianteDAO

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 50)
    print("   SISTEMA DE REGISTRO DE NOTAS DE ESTUDIANTES")
    print("=" * 50)
    print("1. Registrar nuevo estudiante")
    print("2. Ver todos los estudiantes")
    print("3. Ver estudiantes aprobados")
    print("4. Ver estudiantes desaprobados")
    print("5. Generar reporte completo")
    print("6. Salir")
    print("=" * 50)

def validar_nota(nota_str, nombre_nota):
    """Valida que la nota sea un número entre 0 y 100"""
    try:
        nota = float(nota_str)
        if 0 <= nota <= 100:
            return nota
        else:
            print(f"Error: {nombre_nota} debe estar entre 0 y 100")
            return None
    except ValueError:
        print(f"Error: {nombre_nota} debe ser un número válido")
        return None

def registrar_estudiante(dao):
    """Registra un nuevo estudiante"""
    print("\n--- REGISTRAR NUEVO ESTUDIANTE ---")
    
    # Solicitar datos del estudiante
    cif = input("Ingrese el CIF del estudiante: ").strip()
    if not cif:
        print("Error: El CIF no puede estar vacío")
        return
    
    # Verificar si el estudiante ya existe
    if dao.existe_estudiante(cif):
        print(f"Error: Ya existe un estudiante con CIF {cif}")
        return
    
    nombres = input("Ingrese los nombres: ").strip()
    if not nombres:
        print("Error: Los nombres no pueden estar vacíos")
        return
    
    apellidos = input("Ingrese los apellidos: ").strip()
    if not apellidos:
        print("Error: Los apellidos no pueden estar vacíos")
        return
    
    asignatura = input("Ingrese la asignatura: ").strip()
    if not asignatura:
        print("Error: La asignatura no puede estar vacía")
        return
    
    # Solicitar y validar las 3 notas
    nota1 = None
    while nota1 is None:
        nota1_str = input("Ingrese la primera nota (0-100): ")
        nota1 = validar_nota(nota1_str, "La primera nota")
    
    nota2 = None
    while nota2 is None:
        nota2_str = input("Ingrese la segunda nota (0-100): ")
        nota2 = validar_nota(nota2_str, "La segunda nota")
    
    nota3 = None
    while nota3 is None:
        nota3_str = input("Ingrese la tercera nota (0-100): ")
        nota3 = validar_nota(nota3_str, "La tercera nota")
    
    # Crear y guardar el estudiante
    try:
        estudiante = Estudiante(cif, nombres, apellidos, asignatura, nota1, nota2, nota3)
        if dao.guardar_estudiante(estudiante):
            print(f"\n¡Estudiante registrado exitosamente!")
            print(f"Promedio calculado: {estudiante.nota_final}")
            print(f"Estado: {estudiante.estado}")
        else:
            print("Error al guardar el estudiante")
    except Exception as e:
        print(f"Error al crear el estudiante: {e}")

def mostrar_estudiantes(estudiantes, titulo):
    """Muestra una lista de estudiantes"""
    print(f"\n--- {titulo} ---")
    if not estudiantes:
        print("No hay estudiantes para mostrar.")
        return
    
    print(f"Total: {len(estudiantes)} estudiantes")
    print("-" * 80)
    for i, est in enumerate(estudiantes, 1):
        print(f"{i}. {est}")
    print("-" * 80)

def main():
    """Función principal"""
    dao = EstudianteDAO()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            registrar_estudiante(dao)
        
        elif opcion == "2":
            estudiantes = dao.cargar_estudiantes()
            mostrar_estudiantes(estudiantes, "TODOS LOS ESTUDIANTES")
        
        elif opcion == "3":
            aprobados = dao.obtener_estudiantes_por_estado("APROBADO")
            mostrar_estudiantes(aprobados, "ESTUDIANTES APROBADOS")
        
        elif opcion == "4":
            desaprobados = dao.obtener_estudiantes_por_estado("DESAPROBADO")
            mostrar_estudiantes(desaprobados, "ESTUDIANTES DESAPROBADOS")
        
        elif opcion == "5":
            print("\n--- GENERANDO REPORTE ---")
            if dao.generar_reporte():
                print("¡Reporte generado exitosamente!")
            else:
                print("Error al generar el reporte")
        
        elif opcion == "6":
            print("\n¡Gracias por usar el sistema!")
            break
        
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 6.")
        
        # Pausa para que el usuario pueda leer la información
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()

