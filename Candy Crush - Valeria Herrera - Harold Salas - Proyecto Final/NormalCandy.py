from Candy import *

class NormalCandy(Candy):
    def __init__(self, color, type, num):
        Candy.__init__(self, color, type, num )

    #Explosion method for normal sweet

    def setExplosion(self,matrix, x, y):
        for i in matrix:
            print("23223",i)
        print("---------------------------------------------")
        print(x)
        print(y)
        matrix[x][y] = " "