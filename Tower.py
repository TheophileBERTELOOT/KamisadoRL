import pygame as pg

class Tower:
    def __init__(self,indexPlayer,color,colorKey,playerColor,x,y):
        self.indexPlayer = indexPlayer
        self.color = pg.Color(color)
        self.colorKey=colorKey
        self.playerColor = pg.Color(playerColor)
        self.x=x
        self.y=y
