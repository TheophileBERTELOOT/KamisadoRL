import pygame as pg

class Tower:
    def __init__(self,indexPlayer,color,playerColor,x,y):
        self.indexPlayer = indexPlayer
        self.color = pg.Color(color)
        self.playerColor = pg.Color(playerColor)
        self.x=x
        self.y=y
