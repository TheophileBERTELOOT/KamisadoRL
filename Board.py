import pygame as pg


class Board:
    def __init__(self,screenSizeX,screenSizeY):
        self.screenSizeX = screenSizeX
        self.screenSizeY = screenSizeY
        self.screen = pg.display.set_mode((screenSizeX, screenSizeY))
        self.nbSquare = 8
        self.colors = {'orange':'#CD6C37','pink':'#D85EC1','red':'#CD325A','green':'#029561','blue':'#137CCF','yellow':'#C9B91C','brown':'#472C17','purple':'#7949B5'}
        self.squareSizeX = int(self.screenSizeX/self.nbSquare)
        self.squareSizeY = int(self.screenSizeY / self.nbSquare)


        self.board = self.initBoardColor()

    def initBoardColor(self):
        return [[self.colors['orange'],self.colors['blue'],self.colors['purple'],self.colors['pink'],self.colors['yellow'],self.colors['red'],self.colors['green'],self.colors['brown']],
                [self.colors['red'],self.colors['orange'],self.colors['pink'],self.colors['green'],self.colors['blue'],self.colors['yellow'],self.colors['brown'],self.colors['purple']],
                [self.colors['green'], self.colors['pink'], self.colors['orange'], self.colors['red'],self.colors['purple'], self.colors['brown'], self.colors['yellow'], self.colors['blue']],
                [self.colors['pink'], self.colors['purple'], self.colors['blue'], self.colors['orange'],self.colors['brown'], self.colors['green'], self.colors['red'], self.colors['yellow']],
                [self.colors['yellow'], self.colors['red'], self.colors['green'], self.colors['brown'],self.colors['orange'], self.colors['blue'], self.colors['purple'], self.colors['pink']],
                [self.colors['blue'], self.colors['yellow'], self.colors['brown'], self.colors['purple'],self.colors['red'], self.colors['orange'], self.colors['pink'], self.colors['green']],
                [self.colors['purple'], self.colors['brown'], self.colors['yellow'], self.colors['blue'],self.colors['green'], self.colors['pink'], self.colors['orange'], self.colors['red']],
                [self.colors['brown'], self.colors['green'], self.colors['red'], self.colors['yellow'],self.colors['pink'], self.colors['purple'], self.colors['blue'], self.colors['orange']]]


    def displayBoard(self):
        self.screen.fill((255, 255, 255))
        for i in range(self.nbSquare):
            for j in range(self.nbSquare):
                color = pg.Color(self.board[j][i])
                pg.draw.rect(self.screen,color,pg.Rect(i*self.squareSizeX,j*self.squareSizeY,(i+1)*self.squareSizeX,(j+1)*self.squareSizeY))
        pg.display.flip()