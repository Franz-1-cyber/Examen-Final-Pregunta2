from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def obtener_info(self):
        pass


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def obtener_info(self):
        return f"Estudiante: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}"


class Administrativo(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto = puesto

    def obtener_info(self):
        return f"Administrativo: {self.nombre}, Edad: {self.edad}, Puesto: {self.puesto}"


class Docente(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def obtener_info(self):
        return f"Docente: {self.nombre}, Edad: {self.edad}, Materia: {self.materia}"


def guardar_datos(personas):
    with open('personas.txt', 'w') as file:
        for persona in personas:
            file.write(persona.obtener_info() + '\n')


def mostrar_datos():
    try:
        with open('personas.txt', 'r') as file:
            print("\nLista de Personas:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No hay datos guardados.")


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


if __name__ == "__main__":
    main()

