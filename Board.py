import pygame as pg

from Tower import Tower


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
        self.game = self.initGame()

    def initBoardColor(self):
        return [[self.colors['orange'],self.colors['blue'],self.colors['purple'],self.colors['pink'],self.colors['yellow'],self.colors['red'],self.colors['green'],self.colors['brown']],
                [self.colors['red'],self.colors['orange'],self.colors['pink'],self.colors['green'],self.colors['blue'],self.colors['yellow'],self.colors['brown'],self.colors['purple']],
                [self.colors['green'], self.colors['pink'], self.colors['orange'], self.colors['red'],self.colors['purple'], self.colors['brown'], self.colors['yellow'], self.colors['blue']],
                [self.colors['pink'], self.colors['purple'], self.colors['blue'], self.colors['orange'],self.colors['brown'], self.colors['green'], self.colors['red'], self.colors['yellow']],
                [self.colors['yellow'], self.colors['red'], self.colors['green'], self.colors['brown'],self.colors['orange'], self.colors['blue'], self.colors['purple'], self.colors['pink']],
                [self.colors['blue'], self.colors['yellow'], self.colors['brown'], self.colors['purple'],self.colors['red'], self.colors['orange'], self.colors['pink'], self.colors['green']],
                [self.colors['purple'], self.colors['brown'], self.colors['yellow'], self.colors['blue'],self.colors['green'], self.colors['pink'], self.colors['orange'], self.colors['red']],
                [self.colors['brown'], self.colors['green'], self.colors['red'], self.colors['yellow'],self.colors['pink'], self.colors['purple'], self.colors['blue'], self.colors['orange']]]

    def initGame(self):
        colors = self.colors.keys()
        p0Towers = []
        p1Towers = []
        p0Color = '#ffffff'
        p1Color = '#000000'
        i = 0
        for color in self.board[0]:
            p0Towers.append(Tower(0,color,p0Color,i,0))
            i+=1
        i-=1
        for color in self.board[0]:
            p1Towers.append(Tower(1, color, p1Color, i,7))
            i -= 1
        return [p0Towers,
                [0 for _ in range(self.nbSquare)],
                [0 for _ in range(self.nbSquare)],
                [0 for _ in range(self.nbSquare)],
                [0 for _ in range(self.nbSquare)],
                [0 for _ in range(self.nbSquare)],
                [0 for _ in range(self.nbSquare)],
                p1Towers]

    def displayPlayers(self):
        for i in range(self.nbSquare):
            for j in range(self.nbSquare):
                square = self.game[j][i]
                if square != 0:
                    pg.draw.circle(self.screen, square.playerColor, (square.x*self.squareSizeX+self.squareSizeX/2,
                                                               square.y*self.squareSizeY+self.squareSizeY/2),
                                   self.squareSizeX/4)
                    pg.draw.circle(self.screen, square.color, (square.x * self.squareSizeX + self.squareSizeX / 2,
                                                               square.y * self.squareSizeY + self.squareSizeY / 2),
                                   self.squareSizeX/6)

    def displayBoard(self):
        for i in range(self.nbSquare):
            for j in range(self.nbSquare):
                color = pg.Color(self.board[j][i])
                pg.draw.rect(self.screen,color,pg.Rect(i*self.squareSizeX,j*self.squareSizeY,(i+1)*self.squareSizeX,(j+1)*self.squareSizeY))


    def displayAll(self):
        self.screen.fill((255, 255, 255))
        self.displayBoard()
        self.displayPlayers()
        pg.display.flip()