from random import randint,random

"""
Invisible.py: 
    Sorteo del amigo invisible. Permite meter incompatibilidades.
"""

# Participantes en el sorteo
# participantes = ["Patricia","Antonio","Maria","Nacho","Fer","Gema","Domingo","Maricarmen"]
participantes = []

# Sorteos parciales realizados
regalados = {}

# Realiza el sorteo parcial para un participante
def sortear(participante):
    candidatos = []

    # Montamos la lista de posibles candidatos para este participante
    for part in participantes:
        if part not in regalados.values()  \
           and part != participante:

           candidatos.append(part)

    if candidatos:
       # Numero entero entre [ori,dest]
       pos = randint(0, len(candidatos)-1)

       regalados[participante] = candidatos[pos]
       return pos 
    else:
       return -1

# Muestra el resultado del sorteo
def mostrar_resultados():
    print("*********************************")
    print("      Resultado del sorteo       ")
    print("*********************************")
    for regalando in regalados:
        print(f"{regalando} regala a {regalados[regalando]}")
    print("*********************************")

"""
Proceso principal
"""
# Pedimos por pantalla los participantes en el sorteo. Finaliza con intro.
while True:
    participante = input("Introduzca el nombre del participante (intro para finalizar): ")

    if participante == "":
       break
    else:        
       participantes.append(participante)                 

# Realizamos el sorteo
if len(participantes) % 2 == 0 and len(participantes) > 0:
   for participante in participantes: 
       if sortear(participante) < 0:
          # Se ha dado un caso en el que no hay solución posible
          break    
   if len(regalados) == len(participantes):
       mostrar_resultados()
   else:
      print("No se han encontrado soluciones posibles para el sorteo")    
else:
   print("El número de participantes debe ser mayor que cero y par")