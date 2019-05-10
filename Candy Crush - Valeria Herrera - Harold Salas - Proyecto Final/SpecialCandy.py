from Candy import *


class SpecialCandy(Candy):
    def __init(self, color, type, num ):
        Candy.__init__(self, color, type, num )

    #Explosion method for special sweets
    def setExplosion(self,matrix, x,y):
        for i in matrix:
            print("***-***",i)
        if matrix[x][y] != " ":

            if matrix[x][y].getType() == "SPV":
                for i in range(9):
                    matrix[i][y] = " "

            elif matrix[x][y].getType() == "SPH":
                for j in range(9):
                    matrix[x][j] = " "
