import random
from Docente import Docente
from Nodocente import Nodocente 

personal = []
categorias = ["simple","semi exclusiva","exclusiva"]
jornadas = ["completa","Reducida"]

for i in range(10):
    opcion = random.randint(0,1)
    if opcion == 0:
        personal.append(Docente("nombre", random.randint(1,10), "sector", categorias[random.randint(0,2)])) 
    else:
        personal.append(Docente("nombre", random.randint(1,10), "sector", categorias[random.randint(0,2)])) 
        
    