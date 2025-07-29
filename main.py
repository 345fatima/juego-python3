# importando el modulo os
import os 
from data.datos import Lista_menu
from programas.sumas  import sumar2
from Game.Juego import juego_1


 # limpiar la terminal 
os.system("cls")

estado = True

# bucle que depende de la variable estado 
while estado:
      print("+-----------------------------+)")
      print("|Fatima              2025  v.1|")
      print("|                              |")
      print(f"|[1] : {Lista_menu [0]}")
      print(f"|[2] : {Lista_menu [1]}")
      print(f"|[3] : {Lista_menu [2]}")
      print(f"|[4] : {Lista_menu [3]}")
      print(f"|[5] : {Lista_menu [4]}") 
      print(f"|[0] : salir")
      
      # respuesta al dato ingresado
      
      r = int(input("|[?]:"))
    
      # pregunta si el dato ingresado es una de las opciones disponibles
      if r == 0:
       estado = False
      elif r == 1: 
          sumar2()
      if r == 5: 
          juego_1()

    # limpiar la terminal 
    # os.system("cls")

# código fuera del bucle, se ejecuta si el bucle deja de ser Verdadero
print("[Saliendo del progrma. . .]")      




    