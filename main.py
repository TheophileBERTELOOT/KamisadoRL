import pygame as pg

from Board import Board

pg.init()
running = True
SCREEN_SIZE_X = 1000
SCREEN_SIZE_Y = 1000
board = Board(SCREEN_SIZE_X,SCREEN_SIZE_Y)
while running:
    board.displayAll()
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

pg.quit()