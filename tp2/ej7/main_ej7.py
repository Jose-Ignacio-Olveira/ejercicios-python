from clase_persona import Persona
from datetime import date

fecha1 = date(1994,5,20)
persona1=Persona("Miguel","Rodriguez",fecha1)
fecha2= date(1998,2,14)
persona2=Persona("Fabiana","Cantilo", fecha2)
fecha3= date(1980,4,21)
persona3=Persona("Carlos", "García", fecha3)

persona1.toString()
print(f'{"EDAD: "}{persona1.edad()}')
persona2.toString()
print(f'{"EDAD: "}{persona2.edad()}')
persona3.toString()
print(f'{"EDAD: "}{persona3.edad()}')
