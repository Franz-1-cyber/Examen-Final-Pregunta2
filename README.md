# Examen-Final-Pregunta2

# Examen Final Pregunta 2

Este repositorio contiene una implementación en Python de una clase abstracta `Persona` y sus subclases `Estudiante`, `Administrativo` y `Docente`. El programa permite al usuario agregar datos para crear instancias de estas clases, guardar la información en un archivo y mostrar la lista de personas ingresadas.

## Estructura del Código

- **Clase Abstracta `Persona`**:
  - Atributos:
    - `nombre`: Nombre de la persona.
    - `edad`: Edad de la persona.
  - Método abstracto:
    - `obtener_info()`: Método que debe ser implementado en las subclases.

- **Clase `Estudiante`**:
  - Atributos:
    - `carrera`: Carrera que estudia el estudiante.
  - Implementa `obtener_info()`.

- **Clase `Administrativo`**:
  - Atributos:
    - `puesto`: Puesto que ocupa el administrativo.
  - Implementa `obtener_info()`.

- **Clase `Docente`**:
  - Atributos:
    - `materia`: Materia que enseña el docente.
  - Implementa `obtener_info()`.

## Ejemplo de Uso

El siguiente código permite al usuario ingresar datos para crear instancias de cada tipo de persona, guardar los datos en un archivo y mostrar la lista de personas ingresadas:

```python
def main():
    personas = []

    while True:
        print("\nOpciones:")
        print("1. Agregar persona")
        print("2. Mostrar lista de personas")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            tipo = input("Ingrese el tipo de persona (Estudiante, Administrativo, Docente): ").strip().lower()

            nombre = input("Ingrese el nombre: ")
            edad = int(input("Ingrese la edad: "))

            if tipo == 'estudiante':
                carrera = input("Ingrese la carrera: ")
                persona = Estudiante(nombre, edad, carrera)
            elif tipo == 'administrativo':
                puesto = input("Ingrese el puesto: ")
                persona = Administrativo(nombre, edad, puesto)
            elif tipo == 'docente':
                materia = input("Ingrese la materia: ")
                persona = Docente(nombre, edad, materia)
            else:
                print("Tipo de persona no reconocido. Intente de nuevo.")
                continue

            personas.append(persona)
            guardar_datos(personas)
            print("Persona añadida y guardada exitosamente.")

        elif opcion == '2':
            mostrar_datos()

        elif opcion == '3':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
Requisitos
Python 3.x
Módulo abc (incluido en las instalaciones estándar de Python)
