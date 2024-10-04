from clase_persona import Persona
from clase_familia import Familia
from clase_censo import Censo

persona1 = Persona(23, "Femenino", True, False)
persona2 = Persona(30, "Masculino", False, True)
persona3 = Persona(25, "Femenino", True, True)
familia1= Familia("Martinez")
familia1.agregar_integrante(persona1)
familia1.agregar_integrante(persona2)
familia1.agregar_integrante(persona3)

persona4 = Persona(28, "Masculino", False, False)
persona5 = Persona(12, "Femenino", True, False)
persona6 = Persona(35, "Masculino", True, True)
persona7 = Persona(27, "Femenino", False, True)
familia2= Familia("Olveira")
familia2.agregar_integrante(persona4)
familia2.agregar_integrante(persona5)
familia2.agregar_integrante(persona6)
familia2.agregar_integrante(persona7)

persona8 = Persona(32, "Masculino", True, False)
persona9 = Persona(26, "Femenino", True, True)
familia3= Familia("Garabaldi")
familia3.agregar_integrante(persona8)
familia3.agregar_integrante(persona9)

censo1 = Censo("Comodoro Rivadavia")
censo1.agregar_familia(familia1)
censo1.agregar_familia(familia2)
censo1.agregar_familia(familia3)

print(f'{"La cantidad de familias es de: "}{censo1.cantidad_familias()}')
print(f'{"La cantidad de personas es de :"}{censo1.cantidad_personas_censo()}')
print(f'{"El promedio de edad es de: "}{censo1.promedio_edad()}')
print(f'{"La cantidad de personas que trabajan es de: "}{censo1.cantidad_trabajadores()}')

persona4.permiso_conducir()
persona5.permiso_conducir()
persona6.permiso_trabajo()
persona5.permiso_trabajo()
