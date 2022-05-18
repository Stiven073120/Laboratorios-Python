#juego de adivinar palabras "mad lib"
#modo personalizado ya que no entendi la version americana 

# importaciones 
import random as random

#funciones
def Convertidor_cadena_lista(cadena):
    lista = cadena.split(" ")
    return lista

def Convertidor_lista_cadena(lista):
    cadena = " ".join(lista)
    return cadena    

def Convertidor_texto(x):
    lista = Convertidor_cadena_lista(x)
    cont = len(lista)-1
    palabra = random.randint(1, cont)
    esp = "-"*(len(lista[palabra]))
    lista[palabra] = esp
    cadena_lista = Convertidor_lista_cadena(lista)

    return cadena_lista, palabra

def validacion(lista, cont):
    c = True
    while c:
        r = str(input("\nR//: "))
        if r == lista[cont]:
            print("perfect")
            break
        else:
            while True:
                r = input("error s/n: ")
                if r.lower() == "n":
                    print("adios")
                    c = False
                    break
                elif r.lower() == "s":
                    break
                else:
                    print("dato incorrecto")    
    return

print("Ingresa tres textos \n")
x1 = input("Texto uno: \n \n")
#x2 = input("Texto dos: \n \n")
#x3 = input("Texto tres: \n \n")

lista1 = Convertidor_cadena_lista(x1)

cadena_lista1, palabra1 = Convertidor_texto(x1)
print("Start\n"+cadena_lista1)
validacion(lista1, palabra1)


"""
# Mad Libs Generator - Charles Joseph Monaghan 11/10/2017
# Traducido por Anartz Mugika Ledo 23/04/2021

# Loop back to this point once code finishes
loop = 1

while (loop < 10):

    # Todas las preguntas que se le realiza al usuario para que las conteste
    noun = input("Selecciona un sustantivo: ")
    p_noun = input("Selecciona un sustantivo en plural: ")
    noun2 = input("Selecciona un sustantivo: ")
    place = input("Nombra un lugar: ")
    adjective = input("Selecciona un adjetivo (Describe una palabra): ")
    noun3 = input("Selecciona un sustantivo: ")

    # Displays the story based on the users input
    print ("------------------------------------------")
    print ("Be kind to your",noun,"- footed", p_noun)
    print ("For a duck may be somebody's", noun2,",")
    print ("Be kind to your",p_noun,"in",place)
    print ("Where the weather is always",adjective,".")
    print ()
    print ("You may think that is this the",noun3,",")
    print ("Well it is.")
    print ("------------------------------------------")

    # Loop back to "loop = 1"
    loop = loop + 1

"""    