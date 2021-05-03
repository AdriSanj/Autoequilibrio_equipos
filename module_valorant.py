# -*- coding: utf-8 -*-
"""
Created on Mon May  3 12:12:25 2021

@author: adria
"""

import random
from math import trunc

#----------------------------------------------------------#

class Player:
    def __init__(self, name , stats):
        # Inicialización de la clase.
        self.set_name(name)
        self.set_stats(stats)
        
    def set_name(self, name):
        # Permite poner un nombre al jugador
        # Si lo introducido no es una cadena de caracteres, no asigna nada.
        if type(name) == str:
            self.name = name
        else:
            print("Formato del nombre introducido inválido")
    
    def set_stats(self, stats):
        # Permite introducir la puntuacion.
        # Si lo introducido no es un número, no asigna nada.
        if type(stats) == float or type(stats) == int:
            self.stats = stats
        else:
            print("Formato de la puntuación introducida inválida")
    
    def print_name(self):
        # Saca por pantalla el nombre del jugador.
        print(self.name)
    
    def print_stat(self):
        # Saca por pantalla la puntuación del jugador.
        print(self.stats)
        
    def get_stat(self):
        # Permite obtener la puntuación asignada para darle el valor a otra variable.
        return self.stats

#----------------------------------------------------------#

class Team(Player):
    # Clase equipo. Por defecto tomamos que el número de jugadores permitidos
    # es 5 (por ser Valorant, pero por si se aplica a otro juego la función
    # set_max_players nos lo permite cambiar), y el sistema de puntuación por
    # defecto es de diez puntos como máximo por jugador. Lo dicho, también 
    # se puede cambiar al gusto.
    
    def __init__(self, list_players, max_players = 5):
        # Inicializador de la clase.
        self.asignation(list_players)
        self.set_max_players(max_players)
        
    def asignation(self, list_players):
        if type(list_players) == list:
            self.list_players = list_players
        else:
            print("Formato introducido para la lista de jugadores no válido")
    
    def set_max_players(self, max_players):
        if type(max_players) == int:
            self.max_players = max_players
        else:
            print("Formato introducido para el máximo de jugadores no válido.")
    
    def print_teamplayers(self):
        for i in range(self.max_players):
            self.list_players[i].print_name()
    
    def get_team_points(self):
        team_points = 0
        for i in range(self.max_players):
            team_points += self.list_players[i].get_stat()
        return team_points

#----------------------------------------------------------#

def player_selection(L):
    # Función para generar equipos de forma aleatoria. 
    # Los primeros índices generados de forma aleatoria son para el equipo L1,
    # mientras que los ultimos son para el equipo L2.
    
    L1 = []         # Equipo 1
    L2 = []         # Equipo 2
    L_size = int(len(L)) # Cantidad de jugadores
    Inputs = random.sample(range(0,L_size), L_size)            # Generamos una lista de numeros
                                            # aleatorios sin repeticion
    #print(Inputs)
    if L_size % 2 == 0:
        # Se ejecutan estos bucles en caso de que el numero de jugadores
        # sea par.
        for i in range(int(L_size/2)):
            L1.append(L[Inputs[i]])
        for j in range(int(L_size/2.), L_size):
            L2.append(L[Inputs[j]])
    else:
        # En caso de que sean impares, se ejecutan estos otros.
        for i in range(int(trunc(L_size/2.))):
            L1.append(L[Inputs[i]])
        for j in range(int(trunc(L_size/2.)), L_size):
            L2.append(L[Inputs[j]])
    return L1, L2

#----------------------------------------------------------#

def team_asignation(L, err_puntuacion = 3):
    # Por defecto, con el sistema de puntuación en 10, el 3 parece 
    # la diferencia de puntuación más justo (a mi criterio, pero
    # obviamente se puede cambiar).
    while(True):
        # Crea dos equipos con la función player_selection
        L1,L2 = player_selection(L)
        # Una vez creadas las listas de jugadores y puntuaciones, se
        # introducen en la clase Team, junto con el número de jugadores de
        # cada equipo.
        T1 = Team(L1, len(L1))
        T2 = Team(L2, len(L2))
    
        if abs(T1.get_team_points()-T2.get_team_points())<= err_puntuacion:
            break
    
    return T1, T2

#----------------------------------------------------------#