from Candy import *

numExplotion = 1
class DiscoBallCandy(Candy):
    def __init__(self, color, type, num):
        Candy.__init__(self, color, type, num)

    #Method for disco ball explosion
    def setExplosion(self,matrix,x,y, color):

        matrix[x][y] = " "




