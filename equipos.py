# -*- coding: utf-8 -*-
"""
Created on Mon May  3 12:32:28 2021

@author: adria
"""
from module_valorant import *

# Se lee el archivo con esos datos como ejemplo del funcionamiento del
# código. 
Jugadores = read_stat_doc()

#err_puntuacion = 3

T1,T2 = team_asignation(Jugadores)

print("Equipo 1")
print("Integrantes:")
T1.print_teamplayers()
print("Puntuación del equipo 1: ", T1.get_team_points())
print("#---------------------------#")
print("Equipo 2")
print("Integrantes:")
T2.print_teamplayers()
print("Puntuación del equipo 2: ", T2.get_team_points())

