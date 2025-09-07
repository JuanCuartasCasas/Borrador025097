#Autor:Juan Diego Cuartas Casas
#Motivo:Retroalimentacion clases 
#Realizacion Ejercicios de practicas

def ejemplo11():
    print(f"Bienvenido a  ejercicios imprimir por pantalla\n")
    #Ejercicio 1.1
    print("Hola, ya se imprimir frases\n")    
    #Ejercicio 1.2
    x = 25
    print(type(x),x)
    #Ejercicio 1.3
    y = 2.74454
    print(type(y),y)

def ejemplo12():
    print(f"Bienvenido a operciones basicas y bucles \n")
    #Ejercicio 1.4
    sum = 1234+532
    print(type(sum),sum)
    #Ejercicio 1.5
    rest = float(1234-532)
    print(type(rest),rest)
    #Ejercicio 1.6
    mult = 1234*532
    print(type(mult),mult)
    #Ejercicio 1.7
    div = 1234/532
    print(type(div),div)
    print("\n")
    cont = 1
    while (cont <=3):
        print(f"Numero 1: {cont}")
        cont = cont + 1
    print("\n")
    cont = 1
    while (cont <10):
        print(f"Numero 2: {cont}")
        cont = cont +1
    print("\n")
    for num in range(1,10001):
        print(f"Numero 3: {num}")
    print("\n")
         
    
def main ():
    ejemplo11()
    ejemplo12()


if __name__ == "__main__":
    main () 