# Sistema de Registro y Procesamiento de Calificaciones

Solución algorítmica e implementación en Python para gestionar el registro de notas académicas de un grupo de aprendices, calcular sus promedios individuales, determinar su estado de aprobación y obtener el promedio general del grupo.

## Autor
* **Jhonatan Elith Ayala Sánchez** - [@jhonnyelithAZ](https://github.com/jhonnyelithAZ)


---

## 1. Comprensión del Problema
Una institución educativa requiere automatizar el cálculo de calificaciones de sus aprendices. El sistema debe permitir el ingreso de $N$ aprendices, capturar 3 calificaciones por cada uno (en escala de 0 a 100), calcular su nota definitiva, evaluar si cumple con el criterio de aprobación ($\ge 70$) y generar al final un reporte consolidado con el promedio general de todo el grupo.

---

## 2. Descomposición del Problema (E - P - S)

| Fase | Descripción de Elementos |
| :--- | :--- |
| **Entradas** | • `num_aprendices`: Cantidad total de aprendices a registrar.<br>• `nombre`: Nombre completo de cada aprendiz.<br>• `nota1`, `nota2`, `nota3`: Calificaciones parciales (rango 0 - 100). |
| **Procesos** | • Iterar $N$ veces mediante un ciclo controlado.<br>• Calcular el promedio individual: `(nota1 + nota2 + nota3) / 3`.<br>• Evaluar condición de aprobación (`promedio >= 70`) para asignar estado.<br>• Acumular los promedios individuales en `suma_promedios_grupo`.<br>• Calcular el promedio del grupo: `suma_promedios_grupo / num_aprendices`. |
| **Salidas** | • Listado final con Nombre, Promedio definitivo y Estado (`Aprobado` / `Reprobado`) de cada aprendiz.<br>• Promedio general del grupo. |

---

## 3. Variables y Arreglos Utilizados

### Variables Escalares
* `num_aprendices` *(Entero)*: Límite de iteraciones del ciclo principal.
* `suma_promedios_grupo` *(Real)*: Acumulador para la sumatoria de notas definitivas del salón.
* `promedio_general` *(Real)*: Resultado final de rendimiento del grupo.

### Arreglos Paralelos (Listas en Python)
Se utilizan tres arreglos indexados de forma paralela para conservar la integridad de los datos de cada aprendiz hasta la impresión del reporte:
* `nombres[]` *(Cadena)*: Almacena los nombres de los aprendices.
* `promedios[]` *(Real)*: Almacena el promedio calculado de cada aprendiz.
* `estados[]` *(Cadena)*: Almacena la etiqueta `"Aprobado"` o `"Reprobado"`.

---

## 4. Diseño en Pseudocódigo

```text
Algoritmo SistemaRegistroCalificaciones
    Definir num_aprendices, i Como Entero
    Definir nota1, nota2, nota3, suma_notas, suma_promedios_grupo, promedio_general Como Real
    
    suma_promedios_grupo <- 0
    Escribir "Ingrese la cantidad de aprendices a evaluar:"
    Leer num_aprendices
    
    Si num_aprendices <= 0 Entonces
        Escribir "Error: La cantidad debe ser mayor a 0."
    Sino
        Dimension nombres[num_aprendices], promedios[num_aprendices], estados[num_aprendices]
        
        Para i <- 0 Hasta num_aprendices - 1 Con Paso 1 Hacer
            Escribir "Nombre completo:"
            Leer nombres[i]
            Leer nota1, nota2, nota3
            
            suma_notas <- nota1 + nota2 + nota3
            promedios[i] <- suma_notas / 3
            
            Si promedios[i] >= 70 Entonces
                estados[i] <- "Aprobado"
            Sino
                estados[i] <- "Reprobado"
            FinSi
            
            suma_promedios_grupo <- suma_promedios_grupo + promedios[i]
        FinPara
        
        promedio_general <- suma_promedios_grupo / num_aprendices
        
        Para i <- 0 Hasta num_aprendices - 1 Con Paso 1 Hacer
            Escribir nombres[i], " | Promedio: ", promedios[i], " | Estado: ", estados[i]
        FinPara
        
        Escribir "PROMEDIO GENERAL DEL GRUPO: ", promedio_general
    FinSi
FinAlgoritmo
```

---

## 5. Prueba de Escritorio

Se realizaron pruebas con **3 aprendices** evaluando un caso aprobatorio, uno reprobatorio y un caso límite exacto en `70.0`:

| Iteración (`i`) | `nombres[i]` | Notas Ingresadas | `promedios[i]` | Condición (`>= 70`) | `estados[i]` | `suma_promedios_grupo` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | Carlos | `80, 90, 85` | `85.00` | Verdadero | Aprobado | `85.00` |
| **1** | Sofía | `50, 60, 55` | `55.00` | Falso | Reprobado | `140.00` |
| **2** | Andrés | `70, 70, 70` | `70.00` | Verdadero | Aprobado | `210.00` |

* **Cálculo final:** `210.00 / 3 = 70.00`
* **Correcciones aplicadas tras pruebas:** Se añadieron bloques `try-except` y bucles `while` en Python para evitar caídas por ingreso de texto en campos numéricos, notas fuera del rango `0-100` o división por cero si se ingresan `0` aprendices.

---

## 6. Ejecución del Proyecto

### Requisitos
* Python 3.8 o superior.

### Pasos para ejecutar
1. Clonar el repositorio o descargar los archivos en una carpeta local.
2. Abrir una terminal en la raíz del proyecto y ejecutar:
   ```bash
   python3 registro_calificaciones.py
   ```