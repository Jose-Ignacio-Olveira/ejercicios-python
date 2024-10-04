from clase_persona import Persona
from clase_empresa import Empresa

persona1 = Persona("Mauricio","Moldavski",43,"Masculino",True,False)
persona2 = Persona("Alan","Parson",23,"Masculino",True,False)
persona3 = Persona("Isabel","Laporte",50,"Femenino",True,False)
persona4 = Persona("Javier","Campari",31,"Masculino",True,False)
persona5 = Persona("Elisa","Damasco",43,"Femenino",True,False)
empresa1 = Empresa("NINTENDO","Chacabuco 570")
empresa1.agregar_empleado(persona1)
empresa1.agregar_empleado(persona2)
empresa1.agregar_empleado(persona3)
empresa1.agregar_empleado(persona4)
empresa1.agregar_empleado(persona5)

print(f'{"La empresa "}{empresa1.get_nombre()}{ " posee: "}{empresa1.cantidad_empleados()}{" empleados."}')
print("--------------------------------------")
empresa1.datos_empleados()
