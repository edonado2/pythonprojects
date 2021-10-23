

class main:
    def __init__(self):
        self.personas = []
        self.estudiantes = []
        self.profesores = []
        self.cursos = []

        self.personas.append(estudiante('Juan', 20, 'Ingenieria'))
        self.personas.append(estudiante('Pedro', 21, 'Medicina'))
        self.personas.append(estudiante('Maria', 22, 'Derecho'))
        self.personas.append(estudiante('Ana', 23, 'Economia'))
        self.personas.append(estudiante('Juan', 20, 'Ingenieria'))

        self.estudiantes.append(estudiante('Juan', 20, 'Ingenieria'))
        self.estudiantes.append(estudiante('Pedro', 21, 'Medicina'))
        self.estudiantes.append(estudiante('Maria', 22, 'Derecho'))
        self.estudiantes.append(estudiante('Ana', 23, 'Economia'))
        self.estudiantes.append(estudiante('Juan', 20, 'Ingenieria'))

        self.profesores.append(profesor('Juan', 20, 'Ingenieria'))
        self.profesores.append(profesor('Pedro', 21, 'Medicina'))
        self.profesores.append(profesor('Maria', 22, 'Derecho'))
        self.profesores.append(profesor('Ana', 23, 'Economia'))
        self.profesores.append(profesor('Juan', 20, 'Ingenieria'))

        self.cursos.append(curso('Ingenieria', 'Juan'))
        self.cursos.append(curso('Medicina', 'Pedro'))
        self.cursos.append(curso('Derecho', 'Maria'))
        self.cursos.append(curso('Economia', 'Ana'))
        self.cursos.append(curso('Ingenieria', 'Juan'))

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return '{} ({})'.format(self.nombre, self.edad)

class estudiante(persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    def __str__(self):
        return super().__str__() + ' ' + self.carrera

class profesor(persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia
    def __str__(self):

        return super().__str__() + ' ' + self.materia

class empleado(persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario
    def __str__(self):
        return super().__str__() + ' ' + self.salario
class curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
    def __str__(self):
        return self.nombre + ' ' + self.profesor        

     

empleado1 = empleado('Juan', 20, '$1000')
empleado2 = empleado('Pedro', 21, '$2000')
empleado3 = empleado('Maria', 22, '$3000')
empleado4 = empleado('Ana', 23, '$4000')
empleado5 = empleado('Juan', 20, '$5000')
empleado6 = empleado('Pedro', 21, '$6000')


estudiante1 = estudiante('Juan', 20, 'Ingenieria')
estudiante2 = estudiante('Pedro', 21, 'Medicina')
estudiante3 = estudiante('Maria', 22, 'Derecho')
estudiante4 = estudiante('Ana', 23, 'Economia')
estudiante5 = estudiante('Juan', 20, 'Ingenieria')
estudiante6 = estudiante('Pedro', 21, 'Medicina')
estudiante7 = estudiante('Maria', 22, 'Derecho')

profesor1 = profesor('Juan', 20, 'Ingenieria')
profesor2 = profesor('Pedro', 21, 'Medicina')
profesor3 = profesor('Maria', 22, 'Derecho')
profesor4 = profesor('Ana', 23, 'Economia')
profesor5 = profesor('Juan', 20, 'Ingenieria')  
profesor6 = profesor('Pedro', 21, 'Medicina')
profesor7 = profesor('Maria', 22, 'Derecho')

if __name__ == '__main__':
    main()
    print("")
    print("Los empleados con su salarios: ")   
    print("")
    print(empleado1)
    print(empleado2)
    print(empleado3)
    print(empleado4)
    print(empleado5)
    print(empleado6)

if __name__ == '__main__':
    main()
    print("")
    print("El nombre de los estudiantes del curso es:")
    print("")
    print(estudiante1)
    print(estudiante2)
    print(estudiante3)
    print(estudiante4)
    print(estudiante5)
    print(estudiante6)
    print(estudiante7)

if __name__ == '__main__':
    main()
    print("")
    print("El nombre de los profesores del curso es:")
    print("")
    print(profesor1)
    print(profesor2)
    print(profesor3)
    print(profesor4)
    print(profesor5)
    print(profesor6)
    print(profesor7)

if __name__ == '__main__':
    main()
    print("")
    print("Los cursos que tiene cada profesor:")
    print("")
    print(curso('Ingenieria', 'Juan'))
    print(curso('Medicina', 'Pedro'))
    print(curso('Derecho', 'Maria'))
    print(curso('Economia', 'Ana'))
    print(curso('Ingenieria', 'Juan'))


    
