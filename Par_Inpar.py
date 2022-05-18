#FUNCIONES
def Par_inpar(x):
    o = x%2
    if o == 0:
        return True
    else:
        return False    

def cont():
    r = input("desea volver a intentarlo ?  S/N").lower()

    if r == "s":
        return True
    if r == "n":   
        return False 

def despedida():
    print("Gracias por utilizar la aplicacion. MSCC")        

#CODIGO FUENTE

n = input("cual es tu nombre  ")
conta = 1  
bx = True

while bx:

    try:
        if conta == 1:
            x = int(input("hola "+n+" dijite un numero del 1 al 100 "))
        else:
            x = int(input("hola de nuevo "+n+" dijite un numero del 1 al 100 "))

        if x >= 1 and x <= 100:
            r = Par_inpar(x)
            if r is True:
                print(n+" El numero "+str(x)+" es un numero PAR")
                rr = cont()
                if rr == False:
                    bx = False
                    despedida()
                else:    
                    conta += 1      
            else:   
                print(n+" El numero "+str(x)+" es un numero INPAR")
                rr = cont()
                if rr == False:
                    bx = False
                    despedida()
                else:    
                    conta += 1
        else:
            print("numero incorrecto")
            rr = cont()
            if rr == False:
                bx = False  
                despedida()
            else:      
                conta += 1         
    except:
        print("incorrecto")
        rr = cont()
        if rr == False:
            bx = False
            despedida()
        else:    
            conta += 1




