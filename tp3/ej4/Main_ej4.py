from Personaje import Personaje
from Tanque import Tanque
from Asesino import Asesino

tank = Tanque("Sion")
assassin = Asesino("Nocturne")

def pelea(atacante,defensor):
    print(f'{atacante.get_nombre()}{" ataca a: "}{defensor.get_nombre()}')
    daño = atacante.atacar() - defensor.defender()
    defensor.set_vida(defensor.get_vida() - daño)
    print(f'{defensor.get_nombre()}{" recibe "}{daño}{" de daño, y queda en "}{defensor.get_vida()}{" puntos de vida!"}')

pelea(assassin,tank)
pelea(tank,assassin)
pelea(assassin,tank)
pelea(tank,assassin)
pelea(assassin,tank)
pelea(tank,assassin)
pelea(assassin,tank)
pelea(tank,assassin)
pelea(assassin,tank)
pelea(tank,assassin)
pelea(assassin,tank)
pelea(tank,assassin)