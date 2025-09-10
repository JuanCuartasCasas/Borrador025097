#Autor:Juan Diego Cuartas Casas
#Motivo:Realización tarea 1

class Perro:
    def __init__(self,raza,color):#--init__/    metodo inicial que va a corre una instancia futura cuando llame una clase perro
        Perro.raza = raza
        Perro.color = color
   

class Gato:
    def __init__(self,raza,color):
        Gato.raza = raza
        Gato.color = color


print("Bienvenido a la veterinaria")
clperro = input("Que raza de perro tienes?: ")
clcolor = input("De que color es tu perro?: ")
clgato = input("Que raza de gato tienes?: ")
clcolor2 = input("De que color es tu gato?: ")

perro1 = Perro(clperro,clcolor) #perro1,referencia a la clase perro,instancia,por lo tanto se crea un objeto
gato1 = Gato(clgato,clcolor2)

print(f"Tu perro es de raza,{perro1.raza},y es de color,{perro1.color}")
print(f"Tu gato es de raza,{gato1.raza},y es de color,{gato1.color}")

#Autor:Juan Diego Cuartas Casas