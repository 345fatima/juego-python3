import os
import readchar  
from mapa import cargar_mapa 

estado_juego = True 

def juego_1():
    
    #iniciar juego 

    Tecla = readchar. readchar()

    if Tecla in ("w", "s", "a", "d"):
        cargar_mapa(Tecla)

    elif Tecla == "Q": 
        
        estado_juego = False 
    
    
while estado_juego:
    juego_1()
    
