# -*- coding: utf-8 -*-
"""
Created on Mon May  3 12:32:28 2021

@author: adria
"""


from module_valorant import *

# Jugadores, puntuaciones.

p1 = Player('Adri', 6)

p2 = Player('Pablo', 10)

p3 = Player('Hans', 8)

p4 = Player('Helena', 8)

p5 = Player('Anton', 6)

p6 = Player('Saul', 10)

p7 = Player('Raku', 7)

p8 = Player('Alex', 7)

# Lista de los jugadores de la partida.

Jugadores = [p1, p2, p3, p4, p5, p6, p7, p8]

# Distribución de equipos.

err_puntuacion = 3

T1,T2 = team_asignation(Jugadores, err_puntuacion)

print("Equipo 1")
print("Integrantes:")
T1.print_teamplayers()
print("Puntuación del equipo 1: ", T1.get_team_points())
print("#---------------------------#")
print("Equipo 2")
print("Integrantes:")
T2.print_teamplayers()
print("Puntuación del equipo 2: ", T2.get_team_points())

