import pygame as pg
import math
from Tower import Tower
import numpy as np

class Board:
    def __init__(self,screenSizeX,screenSizeY):
        self.screenSizeX = screenSizeX
        self.screenSizeY = screenSizeY
        self.screen = pg.display.set_mode((screenSizeX, screenSizeY))
        self.nbSquare = 8
        self.colors = {'orange':'#CD6C37','pink':'#D85EC1','red':'#CD325A','green':'#029561','blue':'#137CCF','yellow':'#C9B91C','brown':'#472C17','purple':'#7949B5'}
        self.squareSizeX = int(self.screenSizeX/self.nbSquare)
        self.squareSizeY = int(self.screenSizeY / self.nbSquare)
        self.p0Towers = []
        self.p1Towers = []
        self.board = self.initBoardColor()
        self.currentTurn=0
        self.playerTurn=0
        self.selectedTower=None
        self.lastTurnColor=None
        self.initPlayers()


    def initBoardColor(self):
        return [['orange','blue','purple','pink','yellow','red','green','brown'],
                ['red','orange','pink','green','blue','yellow','brown','purple'],
                ['green', 'pink', 'orange', 'red','purple', 'brown', 'yellow', 'blue'],
                ['pink', 'purple', 'blue', 'orange','brown', 'green', 'red', 'yellow'],
                ['yellow', 'red', 'green', 'brown','orange', 'blue', 'purple', 'pink'],
                ['blue', 'yellow', 'brown', 'purple','red', 'orange', 'pink', 'green'],
                ['purple', 'brown', 'yellow', 'blue','green', 'pink', 'orange', 'red'],
                ['brown', 'green', 'red', 'yellow','pink', 'purple', 'blue', 'orange']]

    def initPlayers(self):

        p0Towers = []
        p1Towers = []
        p0Color = '#ffffff'
        p1Color = '#000000'
        i = 0
        colors = ['orange','blue','purple','pink','yellow','red','green','brown']
        for color in colors:
            p0Towers.append(Tower(0,self.colors[color],color,p0Color,i,0))
            i+=1
        self.p0Towers = p0Towers
        i=0
        for color in colors.__reversed__():
            p1Towers.append(Tower(1, self.colors[color],color, p1Color, i,7))
            i += 1
        self.p1Towers = p1Towers


    def displayPlayers(self):
        for tower in self.p0Towers+self.p1Towers:
            if self.selectedTower != None:
                if self.selectedTower.x == tower.x and self.selectedTower.y == tower.y:
                    pg.draw.circle(self.screen, pg.Color('#FF0000'),
                                   (tower.x * self.squareSizeX + self.squareSizeX / 2,
                                    tower.y * self.squareSizeY + self.squareSizeY / 2),
                                   self.squareSizeX /3)
            pg.draw.circle(self.screen, tower.playerColor, (tower.x*self.squareSizeX+self.squareSizeX/2,
                                                       tower.y*self.squareSizeY+self.squareSizeY/2),
                           self.squareSizeX/4)
            pg.draw.circle(self.screen, tower.color, (tower.x * self.squareSizeX + self.squareSizeX / 2,
                                                       tower.y * self.squareSizeY + self.squareSizeY / 2),
                           self.squareSizeX/6)


    def displayBoard(self):
        for i in range(self.nbSquare):
            for j in range(self.nbSquare):
                color = pg.Color(self.colors[self.board[j][i]])
                pg.draw.rect(self.screen,color,pg.Rect(i*self.squareSizeX,j*self.squareSizeY,(i+1)*self.squareSizeX,(j+1)*self.squareSizeY))




    def displayAll(self):
        self.screen.fill((255, 255, 255))
        self.displayBoard()
        self.displayPlayers()
        pg.display.flip()


    def victoryCheck(self):
        for tower in self.p0Towers:
            if tower.y == 7:
                print('player 1 WIN !!! Congrats !')
                return 1
        for tower in self.p1Towers:
            if tower.y == 0:
                print('player 0 WIN !!! Congrats !')
                return 0
        return -1


    def handlePlayerClick(self,pos):
        if self.selectedTower == None and self.currentTurn==0:
            self.playerSelectTower(pos)
        else:
            self.playerSelectDestination(pos)

    def findTowerPerCoordinates(self,playerIndex,x,y):
        if playerIndex == 0:
            for tower in self.p0Towers:
                if tower.x == x and tower.y == y:
                    return tower
        else:
            for tower in self.p1Towers:
                if tower.x == x and tower.y == y:
                    return tower
        return None
    def playerSelectTower(self,pos):
        x = math.trunc(pos[0]/self.squareSizeX)
        y = math.trunc(pos[1]/self.squareSizeY)
        selectedSquare = self.findTowerPerCoordinates(self.playerTurn,x,y)
        if selectedSquare != None:
            if selectedSquare.indexPlayer == self.playerTurn:
                self.selectedTower = selectedSquare

    def changeTurn(self):
        if self.playerTurn == 0:
            self.playerTurn = 1
        else:
            self.playerTurn = 0
        self.currentTurn+=1

    def isAbleToMove(self,tower):
        if tower.indexPlayer == 0:
            coordToCheck = [(tower.y+1,tower.x),]
            if tower.x-1 > 0:
                coordToCheck.append(((tower.x-1,tower.y+1)))
            if tower.x+1<self.nbSquare:
                coordToCheck.append(((tower.x + 1, tower.y + 1)))
        else:
            coordToCheck = [(tower.x, tower.y - 1)]
            if tower.x-1 > 0:
                coordToCheck.append(((tower.x-1,tower.y-1)))
            if tower.x+1<self.nbSquare:
                coordToCheck.append(((tower.x + 1, tower.y -1)))

        nbBlock = 0
        for coord in coordToCheck:
            alreadyCheckedThisOne = False
            for testedTower in self.p0Towers+self.p1Towers:
                if testedTower.x == coord[0] and testedTower.y == coord[1] and not alreadyCheckedThisOne:
                    nbBlock+=1
                    alreadyCheckedThisOne = True

        if nbBlock == len(coordToCheck):
            return False
        else:
            return True


    def isTHereATowerInDiagonale(self,tower,destY,destX):
        difXGlobal = abs(destX-tower.x)
        difYGlobal = abs(destY-tower.y)
        if difYGlobal != difXGlobal :
            return True

        for checkTower in self.p0Towers+self.p1Towers:
            if checkTower.x != tower.x or checkTower.y != tower.y :
                difX = abs(checkTower.x-tower.x)
                difY = abs(checkTower.y-tower.y)
                if difY == difX:
                    if tower.indexPlayer == 0:
                        inFront = checkTower.y > tower.y
                    else:
                        inFront = checkTower.y< tower.y
                    if inFront:
                        checkLeftRight = np.sign(checkTower.x-tower.x) == np.sign(destX-tower.x)
                        if difY<=difYGlobal and checkLeftRight:
                            return True
        return False

    def isThereATowerInFront(self,tower,destY,destX):
        if destX != tower.x:
            return True
        towardBot = True
        if destY<tower.y:
            towardBot = False
        for checkTower in self.p0Towers+self.p1Towers:
            if checkTower.x != tower.x or checkTower.y != tower.y:
                if checkTower.x == tower.x:
                    if towardBot and checkTower.y > tower.y and checkTower.y < destY:
                        return True
                    elif not towardBot and checkTower.y<tower.y and checkTower.y>destY:
                        return True
        return False

    def NoRetreat(self,tower,destY):
        if tower.indexPlayer == 0 and destY>tower.y:
            return True
        elif tower.indexPlayer == 1 and destY<tower.y:
            return True
        else:
            return False


    def squareIsEmpty(self,x,y):
        for tower in self.p0Towers+self.p1Towers:
            if tower.x == x and tower.y == y:
                return False
        return True

    def selectLastTurnColorTower(self):
        if self.playerTurn == 0:
            checkTowers = self.p0Towers
        else:
            checkTowers = self.p1Towers
        for tower in checkTowers:
            if tower.colorKey == self.lastTurnColor:
                self.selectedTower = tower
        if not self.isAbleToMove(self.selectedTower):
            self.changeTurn()
            self.lastTurnColor = self.board[self.selectedTower.y][self.selectedTower.x]
            self.selectLastTurnColorTower()


    def playerSelectDestination(self,pos):
        x = math.trunc(pos[0] / self.squareSizeX)
        y = math.trunc(pos[1] / self.squareSizeY)
        if self.squareIsEmpty(x,y):
            if not self.isThereATowerInFront(self.selectedTower,y,x) or not self.isTHereATowerInDiagonale(self.selectedTower,y,x):
                if self.NoRetreat(self.selectedTower,y):
                    self.selectedTower.y = y
                    self.selectedTower.x = x
                    self.lastTurnColor = self.board[y][x]
                    self.selectedTower = None
                    self.changeTurn()
                    if self.currentTurn > 0:
                        self.selectLastTurnColorTower()
                    else:
                        self.lastTurnColor = self.board[self.selectedTower.y][self.selectedTower.x]

