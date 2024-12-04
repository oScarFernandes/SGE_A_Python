from coche import Coche
from colibri import Colibri

# Crea 3 instancias de Coche
coche1 = Coche("Toyota", "Corolla", 2020, "Azul", 20000)
coche2 = Coche("Ford", "Focus", 2018, "Negro", 18000)
coche3 = Coche("Honda", "Civic", 2021, "Rojo", 22000)

# Crea 3 instancias de Colibri
colibri1 = Colibri("Colibri de Anna", "10 cm", "4 g", "Verde", "Bosques")
colibri2 = Colibri("Colibri de cola ancha", "11 cm", "4.5 g", "Azul", "Zonas montañosas")
colibri3 = Colibri("Colibri de garganta roja", "9 cm", "3.5 g", "Rojo", "Praderas")

# Muestra 3 getters de Coche
print("Marca:", coche1.get_marca())
print("Modelo:", coche1.get_modelo())
print("Color:", coche1.get_color())

# Muestra 4 getters de Colibri
print("Especie:", colibri1.get_especie())
print("Tamaño:", colibri1.get_tamaño())
print("Peso:", colibri1.get_peso())
print("Hábitat:", colibri1.get_habitat())

# Modifica 2 atributos de Coche
coche1.set_color("Blanco")
coche1.set_precio(21000)

# Muestra los 2 atributos modificados
print("Color modificado:", coche1.get_color())
print("Precio modificado:", coche1.get_precio())

# Modifica 2 atributos de Colibri
colibri1.set_color("Turquesa")
colibri1.set_peso("4.2 g")

# Muestra los 2 atributos modificados
print("Color modificado:", colibri1.get_color())
print("Peso modificado:", colibri1.get_peso())