#import SpecialCandy, NormalCandy, DiscoBallCandy
#from Main import *

list=["BLU","RED","YEL","ORA","GRE"]
listSpec = ["BLU","RED","YEL","ORA","GRE","MUL"]
listObjects=[]
vertObjsList = []

class Candy():
    def __init__(self, color, type, num):
        self.__color = color
        self.__type = type
        self.__num = num

    def getColor(self):
        return self.__color
    def getType(self):
        return self.__type
    def getNum(self):
        return self.__num

    def addCandy(self,candy):
        listObjects.append(candy)

    def setExplosion(self,matrix,x,y):
        pass


