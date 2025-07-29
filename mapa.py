import os
from modulos.menu import cargar_menu
#Realizamos invisible y visible nuestro texto 
width_mapa = 30
heigth_mapa = 20 
espacio_invisible = "   "
espacio_lleno= "[  ]"

coordenada_personaje = [5,10]
personaje =  "ᐅ"

#Damos indicaciones de como lo queremos 
def cargar_mapa(mover_personaje):
  
    # Menú  
    
    os.system("cls")
    if mover_personaje == "w":
        personaje =  "⯭"
        coordenada_personaje[0] -=1
    
    elif mover_personaje == "s":
        personaje =  "⯯"
        coordenada_personaje[0] +=1

    elif mover_personaje == "a":
        personaje =  "⯬"
        coordenada_personaje[1] -=1

    elif mover_personaje == "d":
        personaje =  "⯮"
        coordenada_personaje[1] +=1
    
    print("+" + "-"*90 + "+")
    for cada_fila  in range(heigth_mapa):
        print ("|", end="")
        for cada_bloque in range(width_mapa):

            if(coordenada_personaje [0]==cada_fila and coordenada_personaje[1]== cada_bloque):
             print(f" {personaje} ", end ="")
            else:
               print(espacio_invisible, end= "") 

#Imprimimos nuestras indicaciones 
        print("|")
    print("+" + "-"*90 + "+")