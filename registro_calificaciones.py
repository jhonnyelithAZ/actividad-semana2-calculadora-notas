def sistema_registro_calificaciones():
    print("=== SISTEMA DE REGISTRO DE CALIFICACIONES ===")
    
    # Validación de entrada para cantidad de aprendices
    while True:
        try:
            num_aprendices = int(input("Ingrese la cantidad de aprendices a evaluar: "))
            if num_aprendices > 0:
                break
            print("Error: La cantidad de aprendices debe ser mayor a 0.")
        except ValueError:
            print("Error: Por favor ingrese un número entero válido.")

    # Arreglos paralelos (Listas en Python)
    nombres = []
    promedios = []
    estados = []
    
    suma_promedios_grupo = 0.0

    # Ciclo para captura y procesamiento (Punto 5)
    for i in range(num_aprendices):
        print("\n---------------------------------------------")
        print(f"Datos del aprendiz #{i + 1}")
        nombre = input("Nombre completo: ").strip()
        nombres.append(nombre)

        # Captura de las 3 notas con validación de rango (0 a 100)
        notas_aprendiz = []
        for j in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Ingrese calificación {j} (0 - 100): "))
                    if 0 <= nota <= 100:
                        notas_aprendiz.append(nota)
                        break
                    print("Error: La nota debe estar entre 0 y 100.")
                except ValueError:
                    print("Error: Ingrese un valor numérico válido.")

        # Cálculo de promedio individual
        promedio_individual = sum(notas_aprendiz) / len(notas_aprendiz)
        promedios.append(promedio_individual)

        # Estructura de decisión para estado (Punto 6)
        if promedio_individual >= 70:
            estados.append("Aprobado")
        else:
            estados.append("Reprobado")

        # Acumular para el promedio del grupo
        suma_promedios_grupo += promedio_individual

    # Cálculo del promedio general (Punto 7)
    promedio_general = suma_promedios_grupo / num_aprendices

    # Presentación de resultados finales
    print("\n=============================================")
    print("          REPORTE FINAL DE RESULTADOS        ")
    print("=============================================")
    
    for i in range(num_aprendices):
        print(f"Aprendiz: {nombres[i]:<20} | Promedio: {promedios[i]:6.2f} | Estado: {estados[i]}")
        
    print("---------------------------------------------")
    print(f"PROMEDIO GENERAL DEL GRUPO: {promedio_general:.2f}")
    print("=============================================")

if __name__ == "__main__":
    sistema_registro_calificaciones()