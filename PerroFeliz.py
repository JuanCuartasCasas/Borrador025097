#Autor:Juan Diego Cuartas Casas
#Motivo:Realización clase 4,hacer al perro feliz

#Constructor
class Perro:
    def __init__(self,edad,nombre,color_ojos):
        self.edad= edad
        self.nombre = nombre
        self.color_ojos =color_ojos

#Metodos
    def acariciar(self):
        print(f"acaricias a tu perro,{self.nombre} se esta poniendo alegre")
    def alimentar(self):
        print(f"tu perro ha comido,sus ojos color {self.color_ojos} brillan,esta muy emocionado")
        
    def pasear(self):
        print(f"llevaste a tu perro {self.nombre} de {self.edad} años de edad a pasear,finalmente es feliz")



print("Bienvenido a cómo hacer feliz a tu perro")

edd=input("¿Cuantos años tiene tu perro? ")
nom = input("¿Cómo se llama tu perro? ")
col = input("¿De qué color son los ojos de tu perro? ")
prueba_perro = Perro(edd,nom,col)
prueba_perro.acariciar()
prueba_perro.alimentar()
prueba_perro.pasear()

#Autor:Juan Diego Cuartas Casas
