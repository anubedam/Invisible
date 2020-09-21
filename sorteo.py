from random import randint,random

"""
Invisible.py: 
    Sorteo del amigo invisible. Permite meter incompatibilidades.
"""

# Participantes en el sorteo
participantes = []

# Incompatibilidades
incompatibles = {}

# Sorteos parciales realizados
regalados = {}

# Realiza el sorteo parcial para un participante
def sortear(participante):
    candidatos = []

    # Montamos la lista de posibles candidatos para este participante
    for part in participantes:
        if part not in regalados.values() and \
           part not in incompatibles[participante] and \
           part != participante:

           candidatos.append(part)
           
    if candidatos:
       # Numero entero entre [ori,dest]
       pos = randint(0, len(candidatos)-1)

       regalados[participante] = candidatos[pos]
       return pos 
    else:
       return -1

# Mostrar un encabezado de texto
def mostrar_encabezado(mensaje):
    print("\n*************************************")
    print(f"{mensaje}")
    print("*************************************\n")

# Muestra el resultado del sorteo
def mostrar_resultados():
    for regalando in regalados:
        print(f"{regalando} regala a {regalados[regalando]}")
    print("*********************************\n")

"""
Proceso principal
"""

mostrar_encabezado("Participantes en el Sorteo")

# Pedimos por pantalla los participantes en el sorteo. Finaliza con intro.
while True:
    participante = input("Introduzca el nombre del participante (intro para finalizar): ")

    if participante == "":
       break
    else:        
       participantes.append(participante)
       # Creamos los incompatibles como un conjunto vacío
       incompatibles[participante] = set()

# Pedimos por pantalla los incompatibles
mostrar_encabezado("Incompatibilidades de candidatos")

for part in participantes:
    incomp = input(f"Introduzca incompatibles para {part} (separados por comas): ").split(",")
    if incomp[0]!="":
       for inc in incomp:
           incompatibles[part].add(inc)
           incompatibles[inc].add(part)

# Realizamos el sorteo
if len(participantes) % 2 == 0 and len(participantes) > 0:
   for participante in participantes: 
       if sortear(participante) < 0:
          # Se ha dado un caso en el que no hay solución posible
          break    
   if len(regalados) == len(participantes):
       mostrar_encabezado("Resultado del Sorteo")
       mostrar_resultados()
   else:
      print("No se han encontrado soluciones posibles para el sorteo")    
else:
   print("El número de participantes debe ser mayor que cero y par")