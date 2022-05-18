#importaciones
import random

#funciones
def Respuesta_Incorrecta():
    print("\n------------------------------\nrespuesta incorrecta\n------------------------------")
    while True:
        r = str(input("desea volver a intentarlo ? : s/n : "))
        if r.lower() == "n":
            print("\n------------------------------\nAdios\n------------------------------")
            return False
            break  
        if r.lower() == "s":
            return True
            break
        else:
            print("\n------------------------------\nrespuesta incorrecta\n------------------------------")  
        
def Bienvenida():
    print("\n------------------------------")
    print("Bienvenidos al juego")
    print("------------------------------")
    x = str(input("\nDesea comenzar ? s/n : "))
    if x.lower() == "s":
        return True
    elif x.lower() == "n":
        print("\n------------------------------\nAdios\n------------------------------")
    else:
        x = Respuesta_Incorrecta()
        if x == True:
            Bienvenida()

def Modo_Juego():
    print("\n------------------------------")
    print("ELIGE EL MODO DE JUEGO")
    print("------------------------------")
    print("(1) Individual palabras aleatorias\n(2) Con amigos. ingresas la palabra")
    print("------------------------------")  

    modo = str(input("seleciona 1 o 2 : "))
    if modo == "1":
        return 1
    elif modo == "2":
        print("modo 2")
    else:
        x = Respuesta_Incorrecta()
        if x == True:
            Modo_Juego()                  

def Nivel_Modo_Individual():
    print("------------------------------")
    print("BIENVENIDO AL MODO INDIVIDUAL")
    print("------------------------------")
    print("(1) Nivel amateur = maximo de 6 errores")
    print("(2) Nivel intermedio = maximo de 4 errores")
    print("(3) Nivel experto = maximo de 2 errores")
    print("------------------------------")

    nivel = str(input("selecciona el nivel de dificultad : "))
    print("------------------------------")
    if nivel == "1":
        print("\n------------------------------\nNivel Amateur\n------------------------------")
        return 6
    elif nivel == "2":
        print("\n------------------------------\nNivel Intermedio\n------------------------------")
        return 4
    elif nivel == "3":
        print("\n------------------------------\nNivel Experto\n------------------------------")
        return 2
    else:
        x = Respuesta_Incorrecta()
        if x == True:
            Nivel_Modo_Individual()

def Selector_Palabra():
    animales = ["perro","gato","loro","caballo","delfin","vaca"]
    ciudades = ["ibague","cali","pereira","medellin","manizales"]
    paises = ["colombia","mexico","francia","españa","alemania"]
    deportes = ["parkour","motocross","patinaje","natacion","futbol"]
    azar = animales+ciudades+paises+deportes

    print("------------------------------")
    print("(1) animale")
    print("(2) ciudades")
    print("(3) paises")
    print("(4) deportes")
    print("(5) azar")
    print("------------------------------")

    x = str(input("seleccione el tipo de palabra : "))
    if x == "1":
        y = random.choice(animales)
        return y
    elif x == "2":    
        y = random.choice(ciudades)
        return y
    elif x == "3":    
        y = random.choice(paises)
        return y
    elif x == "4":    
        y = random.choice(deportes)
        return y
    elif x == "5":    
        y = random.choice(azar)            
        return y
    else:
        x = Respuesta_Incorrecta()
        if x == True:
            Selector_Palabra()

def Modo_Individual(vidas, palabra):
    lista_palabra = list(palabra)
    cont = len(palabra)
    lista_temporal = []
    palabra_intentos = []
    for i in range(cont):
        lista_temporal.append("_ ")  
    cadena_temporal = " ".join(lista_temporal)
    print(cadena_temporal)

    contador = 0
    ciclo = True
    while ciclo:
        if lista_palabra != lista_temporal:
            if contador != vidas:
                letra = input("introduzca una letra : ")
                bool1 = letra in palabra_intentos
                if bool1 == False: 
                    pocision = 0
                    for i in lista_palabra:
                        if letra == i:
                            lista_temporal[pocision] = letra
                        pocision += 1 
                    print(lista_temporal)  
                    bool2 = letra in lista_palabra
                    if bool2 == False:
                        contador += 1
                else:
                    print("ya dijitaste esta letra")
                    contador += 1     
                palabra_intentos.append(letra)       
            else:
                x = Game_Over()
                if x == True:
                    return True
                elif x == False:
                    return False    
                break  
        else:
            print("\n------------------------------\nFELICIDADES GANASTE!!!\n------------------------------")   
            break      

def Game_Over():
    print("\n------------------------------\nGame Over\n------------------------------")
    while True:
        r = str(input("desea volver a jugar? : s/n : "))
        if r.lower() == "n":
            print("\n------------------------------\nAdios\n------------------------------")
            return False
            break  
        if r.lower() == "s":
            return True
            break
        elif r.lower() == "n":
            return False
            break
        else:
            print("\n------------------------------\nrespuesta incorrecta\n------------------------------")

#cuerpo del codigo                
bienvenida = Bienvenida()
if bienvenida == True:
    modo_juego = Modo_Juego()
    if modo_juego == 1:
        while True:
            vidas = Nivel_Modo_Individual()
            palabra = Selector_Palabra()
            modo_individual = Modo_Individual(vidas, palabra)
            if modo_individual == False:
                break      