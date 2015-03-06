# -*- coding: utf-8 -*-

import random

mensajes = { 
	"T" : "[T] Toman todos",
	"O" : "[O] El jugador que lanzó el dado ordena que tome otro jugador",
	"D" : "[D] Toma el jugador que está a la derecha del jugador que tiró ",
	"I" : "[I] Toma el jugador que está a la izquierda del jugador que tiró",
}

mapa = {
	1: "T",
	2: "O",
	3: "D",
	4: "I",
	5: "T",
	6: "O"
}

dado = random.randint(1,6)

print mensajes[ mapa[dado] ]
