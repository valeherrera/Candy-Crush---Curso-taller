import pygame, pygame.font, pygame.event, pygame.draw, string, random
from pygame.locals import *
from Candy import *
import SpecialCandy, DiscoBallCandy, NormalCandy
from User import *
from Score import *
users=[]

#-----------------------------------------------------------------------------------------------------------------------
matrix = []
#Window's size
name=""
width = 800
height = 600

#Image's size
widthMatrix =72
heightMatrix =65
border = 2

#init the pygame and the window
pygame.init()
window = pygame.display.set_mode((width,height))

pygame.display.set_caption("Candy Crush")#name of the window

#load the audio of the window
# music1 = "audio/04 - Good People.mp3"
# music3 = "audio/1 - Imagine Dragons - Radioactive.mp3"
# music5 = "audio/05 Tear In My Heart.mp3"
# music6 = "audio/06 - Sitting, Waiting, Wishing.mp3"
# music8 = "audio/10. I Like Dirt.mp3"
# music9 = "audio/4 - Imagine Dragons - Demons.mp3"
# music10 = "audio/01 - Better Together.mp3"
# music11 = "audio/1 - The Black Keys - Weight Of Love.mp3"
# music12 = "audio/07 Any Colour You Like.mp3"
# music13 = "audio/Of Monsters and Men Empire.mp3"
# music14 = "audio/Sublime Santeria.mp3"
#
# musicList = [music1,music3,music5,music6,music8,music9,music10, music11,music12,music13,music14]

score = 0


#load the image in the window
grid = pygame.image.load("images/grid.png").convert_alpha()
background = pygame.image.load("images/background.jpg")

buttonStart = pygame.image.load("images/boton.png").convert_alpha()
buttonScores = pygame.image.load("images/boton scores.png").convert_alpha()

labelScore = pygame.image.load("images/label moves.png").convert_alpha()

nameInput = pygame.image.load("images/NameInput.png").convert_alpha()
scoreinput = pygame.image.load("images/ScoreInput.png").convert_alpha()

scoreTable = pygame.image.load("images/scoresTable.png").convert_alpha()

window.blit(background, (0,0))
window.blit(grid, (0, 0))
window.blit(buttonStart, (300, 375))
window.blit(buttonScores, (300, 350))


#play the music of the game
sound = "audio/bomb.mp3"
pygame.mixer.music.load(sound)


clock = pygame.time.Clock()

#load of the images of the objects
white = pygame.image.load("images/selection.png").convert_alpha()
red = pygame.image.load("images/red.png").convert_alpha()
blue = pygame.image.load("images/blue.png").convert_alpha()
orange = pygame.image.load("images/orange.png").convert_alpha()
green = pygame.image.load("images/green.png").convert_alpha()
yellow = pygame.image.load("images/yellow.png").convert_alpha()

colorNull = pygame.image.load("images/selection.png").convert_alpha()

specBlueVert = pygame.image.load("images/blue-vert.png").convert_alpha()
specGreeVert = pygame.image.load("images/green-vert.png").convert_alpha()
specOranVert = pygame.image.load("images/orange-vert.png").convert_alpha()
specRedVert = pygame.image.load("images/red-vert.png").convert_alpha()
specYellVert = pygame.image.load("images/yellow-vert.png").convert_alpha()

specBlueHorz = pygame.image.load("images/blue-horiz.png").convert_alpha()
specGreeHorz = pygame.image.load("images/green-horiz.png").convert_alpha()
specOranHorz = pygame.image.load("images/orange-horiz.png").convert_alpha()
specRedHorz = pygame.image.load("images/red-horiz.png").convert_alpha()
specYellHorz = pygame.image.load("images/yellow-horiz.png").convert_alpha()

multiColor = pygame.image.load("images/bola de disco.png").convert_alpha()

colorList = (green,red,blue,orange,yellow)

#-----------------------------------------------------------------------------------------------------------------------


def CreateMatrix():
    imagen=""
    x=0
    while x <=len(list)-1:
        candy=NormalCandy.NormalCandy(list[x], "normal",x)

        candy.addCandy(candy)
        x+=1


    ### create the array 9x9 loop
    i=0
    while i in range(9):
        #creade all de row without a value
        row=[0]*9
        for j in range(9):#insert a rondom value

            row[j] = random.choice(listObjects)
            if j >= 2:#if exist 3 values or more validetes if exist consecutives

                if row[j] == row[j-1] == row[j-2]:#if exist 3 consecutives
                    new = random.choice(listObjects)#choose a new random object of the list


                    while new == row[j]:#this random object has to be different of the consecutive objects
                        new = random.choice(listObjects)

                    row[j-1] = new#change the value of the object in the middle
                    print(row[j-1])
                    print(new)

        matrix.append(row)#add the row in the array grid
        i+=1




    print("--------------------------------------------------------")

    #validetes if exist consecutives objects in the columns
    for i in range(9):

        for j in range(9):
            #create a new list with the list of objects
            copyListObj = listObjects[:]

            if j >= 2:#if exist 3 or more objectes in the colum

                if matrix[j][i] == matrix[j-1][i] == matrix[j-2][i]:#if exist 3 consecutives
                    copyListObj.remove(matrix[j][i])#remove this of the copy of the list of objects and choose a random of it
                    new = random.choice(copyListObj)
                    print(new)
                    print(matrix[j][i])
                    #validation of some exceptions that can happend
                    ##forms a consecutive with the new random object choose around
                    if i >= 2 and i+2 < 9:
                        while new == matrix[j][i-1] == matrix[j][i+1] or new == matrix[j][i-1] == matrix[j][i-2] or new == matrix[j][i+1] == matrix[j][i+2] or new == matrix[j-1][i] == matrix[j-2][i]:
                            new = random.choice(copyListObj)


                    if i == 1:
                        while new == matrix[j][i-1] == matrix[j][i+1]or new == matrix[j][i+1] == matrix[j][i+2]or new == matrix[j-1][i] == matrix[j-2][i]:
                            new = random.choice(copyListObj)


                    if i == 0:
                        while new == matrix[j][i+1] == matrix[j][i+2] or new == matrix[j-1][i] == matrix[j-2][i] :
                            new = random.choice(copyListObj)


                    if i == 9:
                        while new == matrix[j][i-1] == matrix[j][i+1] or new == matrix[j][i-1] == matrix[j][i-2] or new == matrix[j-1][i] == matrix[j-2][i]:
                            new = random.choice(copyListObj)


                    if i > 9:
                        while new == matrix[j][i+1] == matrix[j][i+2]or new == matrix[j][i-1] == matrix[j][i-2] or new == matrix[j][i-1] == matrix[j][i+1] or new == matrix[j-1][i] == matrix[j-2][i]:
                            new = random.choice(copyListObj)


                    matrix[j][i] = new

    print("--------------------------------------------------------")
    menu()
#-----------------------------------------------------------------------------------------------------------------------

def addColor():
    for row in range(9):
            varColor = ""

            for column in range(9):
                #colorList = (green,red,blue,orange,yellow)

                #searchPlays()

                if matrix[row][column] == " ":
                    varColor = colorNull

                elif matrix[row][column].getColor() == "BLU" and matrix[row][column].getType() == "normal":
                    varColor = blue

                elif matrix[row][column].getColor() == "RED" and matrix[row][column].getType() == "normal":
                    varColor = red

                elif matrix[row][column].getColor() == "YEL" and matrix[row][column].getType() == "normal":
                    varColor = yellow

                elif matrix[row][column].getColor() == "ORA" and matrix[row][column].getType() == "normal":
                    varColor = orange

                elif matrix[row][column].getColor() == "GRE" and matrix[row][column].getType() == "normal":
                    varColor = green

                elif matrix[row][column].getColor() == "GRE" and matrix[row][column].getType() == "SPV":
                    varColor = specGreeVert

                elif matrix[row][column].getColor() == "BLU" and matrix[row][column].getType() == "SPV":
                    varColor = specBlueVert

                elif matrix[row][column].getColor() == "ORA" and matrix[row][column].getType() == "SPV":
                    varColor = specOranVert

                elif matrix[row][column].getColor() == "RED" and matrix[row][column].getType() == "SPV":
                    varColor = specRedVert

                elif matrix[row][column].getColor() == "YEL" and matrix[row][column].getType() == "SPV":
                    varColor = specYellVert

                elif matrix[row][column].getColor() == "GRE" and matrix[row][column].getType() == "SPH":
                    varColor = specGreeHorz

                elif matrix[row][column].getColor() == "BLU" and matrix[row][column].getType() == "SPH":
                    varColor = specBlueHorz

                elif matrix[row][column].getColor() == "ORA" and matrix[row][column].getType() == "SPH":
                    varColor = specOranHorz

                elif matrix[row][column].getColor() == "RED" and matrix[row][column].getType() == "SPH":
                    varColor = specRedHorz

                elif matrix[row][column].getColor() == "YEL" and matrix[row][column].getType() == "SPH":
                    varColor = specYellHorz

                elif matrix[row][column].getColor() == "MUL" and matrix[row][column].getType() == "SPM":
                    varColor = multiColor

                window.blit(varColor,[((border+widthMatrix) * column + border),
                                      ((border+heightMatrix) * row + border),])


    #global matrix
    return
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#Game funtions: menu, score, game play
#-----------------------------------------------------------------------------------------------------------------------

def menu():

    window.blit(background, (0,0))
    window.blit(buttonStart, (300, 325))
    window.blit(buttonScores, (300, 375))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                    exit()
            if event.type == MOUSEBUTTONDOWN:
                x_mouse, y_mouse = pygame.mouse.get_pos()

                print(x_mouse, y_mouse)
                if 309 <= x_mouse <= 487 and 331 <= y_mouse <= 360:
                    GamePlay()
                elif 307 <= x_mouse <= 488 and 381 <= y_mouse <= 410:
                    fileUpload(users)
                    ShowBetterPlayers(users)
                    topScore()

        window.blit(background, (0,0))
        window.blit(buttonStart, (300, 325))
        window.blit(buttonScores, (300, 375))

        pygame.display.update()

def topScore():

    SaveCurrentPlayer(name, score)
    fileUpload(users)
    ShowBetterPlayers(users)

    topscoresnames

    font = pygame.font.Font(None, 25)
    topscores1 = font.render(topscoresnames[1],1,(255,255,255))
    topscores2 = font.render(topscoresnames[2],1,(255,255,255))
    topscores3 = font.render(topscoresnames[3],1,(255,255,255))
    topscores4 = font.render(topscoresnames[4],1,(255,255,255))
    topscores5 = font.render(topscoresnames[5],1,(255,255,255))

    window.blit(background, (0, 0))
    window.blit(scoreTable, (0, 0))
    window.blit(topscores1, (300, 350))
    window.blit(topscores2, (300, 380))
    window.blit(topscores3, (300, 410))
    window.blit(topscores4, (300, 440))
    window.blit(topscores5, (300, 480))

    pygame.display.update()


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                    exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_BACKSPACE:
                    menu()
                elif event.key == K_RETURN:
                    pass

        window.blit(background, (0, 0))
        window.blit(scoreTable, (0, 0))
        window.blit(topscores1, (300, 350))
        window.blit(topscores2, (300, 380))
        window.blit(topscores3, (300, 410))
        window.blit(topscores4, (300, 440))
        window.blit(topscores5, (300, 480))
        pygame.display.update()


    fileUpload(users)
    ShowBetterPlayers(users)

    exit()

def GamePlay():
    global score
    global name

    firstSelect = []
    secundSelect = []
    moveOK = False

    moves = 50

    font = pygame.font.Font(None, 25)
    msn = font.render(str(moves),1,(255,255,255))
    scr = font.render(str(score),1,(255,255,255))


    window.blit(background, (0,0))
    window.blit(grid, (0, 0))
    window.blit(labelScore, (0, 0))


    window.blit(msn, (725, 150))
    window.blit(scr, (700, 300))

    pygame.display.update()

    addColor()

    gameLoop = True

    while gameLoop:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameLoop = False

            if event.type == pygame.KEYDOWN:

                if  event.key == pygame.K_ESCAPE:
                    menu()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseButton = pygame.mouse.get_pressed()

                print(mouseButton)

                if pygame.mouse.get_pressed() == (1, 0, 0) and moves > 0:

                    pygame.mouse.get_rel()
                    pos = pygame.mouse.get_pos()
                    column = pos[0] // (widthMatrix + border)
                    row = pos[1] // (heightMatrix + border)

                    if column < 9 and row < 9 :

                        if firstSelect == []:

                            firstSelect.append(row)
                            firstSelect.append(column)
                            secundSelect.clear()

                            window.blit(white,[((border+widthMatrix) * firstSelect[1] + border),((border+heightMatrix) * firstSelect[0] + border),])

                        if (firstSelect != [] and column == firstSelect[1]+1 and row == firstSelect[0]) or (firstSelect != [] and column >= 0 and column == firstSelect[1]-1 and row == firstSelect[0]) or (firstSelect != [] and row == firstSelect[0]+1 and column == firstSelect[1]) or (firstSelect != [] and row >= 0 and row == firstSelect[0]-1 and column == firstSelect[1]):

                            if matrix[firstSelect[0]][firstSelect[1]].getType() == "SPM":

                                print(matrix[firstSelect[0]][firstSelect[1]].getType())
                                print(matrix[row][column])
                                matrix[firstSelect[0]][firstSelect[1]] = matrix[row][column]
                                discBallPlay(matrix[row][column], firstSelect[0],firstSelect[1])

                                pygame.mixer.music.play()

                            else:
                                secundSelect.append(row)
                                secundSelect.append(column)
                                secund = matrix[secundSelect[0]][secundSelect[1]]
                                first = matrix[firstSelect[0]][firstSelect[1]]
                                matrix[secundSelect[0]][secundSelect[1]] = first
                                matrix[firstSelect[0]][firstSelect[1]] = secund

                            window.blit(background, (0,0))
                            window.blit(grid, (0,0))
                            window.blit(labelScore, (0, 0))

                            addColor()

                            msn = font.render(str(moves),1,(255,255,255))
                            scr = font.render(str(score),1,(255,255,255))

                            window.blit(msn, (725, 150))
                            window.blit(scr, (700, 300))


                            moveOK = True

                        else:
                            firstSelect.clear()
                            firstSelect.append(row)
                            firstSelect.append(column)
                            secundSelect.clear()

                            window.blit(background, (0,0))
                            window.blit(grid, (0,0))
                            window.blit(labelScore, (0, 0))

                            addColor()
                            msn = font.render(str(moves),1,(255,255,255))
                            scr = font.render(str(score),1,(255,255,255))
                            window.blit(msn, (725, 150))
                            window.blit(scr, (700, 300))

                            window.blit(white,[((border+widthMatrix) * firstSelect[1] + border),((border+heightMatrix) * firstSelect[0] + border),])

                    if moveOK:

                            GameMoves(row,column)
                            pygame.mixer.music.play()
                            searchPlays(row,column)
                            pygame.mixer.music.play()
                            window.blit(background, (0,0))
                            window.blit(grid, (0,0))
                            window.blit(labelScore, (0, 0))

                            addColor()
                            moves -=1

                            msn = font.render(str(moves),1,(255,255,255))
                            scr = font.render(str(score),1,(255,255,255))

                            window.blit(msn, (725, 150))
                            window.blit(scr, (700, 300))
                            firstSelect.clear()

                            secundSelect.clear()
                            moveOK = False

                            #############search of more consecutives forms

                    print("Click ", pos, "Coordenadas de la retícula: ", row, column)


                elif moves==0:
                    GameOver()

        pygame.display.flip()
        pygame.display.update()

    menu()

def GameOver():
    global name, score

    window.blit(background, (0,0))
    window.blit(scoreinput, (0, 0))
    window.blit(nameInput, (0,0))

    font = pygame.font.Font(None, 25)
    enter=False

    while enter == False:

        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.unicode.isalpha():
                    name+=event.unicode
                elif event.key==K_SPACE:
                    name+=" "
                elif event.key==K_BACKSPACE:
                    name=name[:-1]

                elif event.key==K_RETURN:
                    enter=True

        window.blit(background,(0,0))
        window.blit(nameInput, (0, 0))
        window.blit(scoreinput, (0, 0))
        block=font.render(name,True,(255,255,255))
        scoreBlock=font.render(name,True,(255,255,255))
        rect=block.get_rect()
        rect.center=window.get_rect().center
        window.blit(block,(325,350))
        window.blit(scoreBlock,(325,350))
        scr = font.render(str(score),1,(255,255,255))
        window.blit(scr, (330, 470))
        pygame.display.flip()



    SaveCurrentPlayer(name, score)
    fileUpload(users)
    ShowBetterPlayers(users)

    score = 0
    name = ""
    topScore()

    menu()

#-----------------------------------------------------------------------------------------------------------------------
def GameMoves(x,y):
    global score


    #This function serves to identify that play is you want to perform
    #and depending on what it calls the method of each class and exploits


    if y-1 >=0 and matrix[x][y-1].getColor()==matrix[x][y].getColor():
        if y-2 >=0 and matrix[x][y-2].getColor()==matrix[x][y].getColor():
            if y+1 < 9 and matrix[x][y+1].getColor()==matrix[x][y].getColor():
                if y+2 < 9 and matrix[x][y+2].getColor()==matrix[x][y].getColor():

                    if matrix[x][y-1] != " ":
                        matrix[x][y-1].setExplosion(matrix,x,y-1)    # Here the disco ball is created by the formation of five sweet
                    if matrix[x][y-2] != " ":
                        matrix[x][y-2].setExplosion(matrix,x,y-2)     # J1
                    if matrix[x][y] != " ":
                        matrix[x][y].setExplosion(matrix,x,y)
                    if matrix[x][y+1] != " ":
                        matrix[x][y+1].setExplosion(matrix,x,y+1)
                    if matrix[x][y+2] != " ":
                        matrix[x][y+2].setExplosion(matrix,x,y+2)
                    for t in matrix:
                        print(t)

                    newCandy=DiscoBallCandy.DiscoBallCandy("MUL", "SPM",3)
                    matrix[x][y]=newCandy

                    waterFall(x,y)

                    score+=(50*5)

                else:

                    if x-1 >= 0 and matrix[x-1][y].getColor()==matrix[x][y].getColor():
                        if x-2 >= 0 and matrix[x-2][y].getColor()==matrix[x][y].getColor():

                            SweetSpecialColor=matrix[x][y].getColor()
                            newCandy=SpecialCandy.SpecialCandy(SweetSpecialColor,"SPH", 7 )

                            if matrix[x][y-1] != " ":
                                matrix[x][y-1].setExplosion(matrix,x,y-1)
                            if matrix[x][y] != " ":
                                matrix[x][y].setExplosion(matrix,x,y)       # J14
                            if matrix[x][y-2] != " ":
                                matrix[x][y-2].setExplosion(matrix,x,y+2)
                            if matrix[x][y+1] != " ":
                                matrix[x][y+1].setExplosion(matrix,x,y+1)
                            if matrix[x-1][y] != " ":
                                matrix[x-1][y].setExplosion(matrix,x-1,y)
                            if matrix[x-2][y] != " ":
                                matrix[x-2][y].setExplosion(matrix,x-2,y)

                            matrix[x][y]=newCandy

                            waterFall(x,y)

                            score+=(50*6)

                            return

                    else:
                        if x+1 < 9 and matrix[x+1][y].getColor()==matrix[x][y].getColor():
                            if x+2 < 9 and matrix[x+2][y].getColor()==matrix[x][y].getColor():

                                if matrix[x][y-1] != " ":
                                    matrix[x][y-1].setExplosion(matrix,x,y-1)
                                if matrix[x][y] != " ":
                                    matrix[x][y].setExplosion(matrix,x,y)       # J19
                                if matrix[x][y-2] != " ":
                                    matrix[x][y-2].setExplosion(matrix,x,y-2)
                                if matrix[x][y+1] != " ":
                                    matrix[x][y+1].setExplosion(matrix,x,y+1)
                                if matrix[x+1][y] != " ":
                                    matrix[x+1][y].setExplosion(matrix,x+1,y)
                                if matrix[x+2][y] != " ":
                                    matrix[x+2][y].setExplosion(matrix,x+2,y)

                                waterFall(x,y)

                                score+=(50*6)

                                return
                         #*********************************************
                        else:

                            sweetSpecialColor=matrix[x][y].getColor()

                            if matrix[x][y-1] != " ":
                                matrix[x][y-1].setExplosion(matrix,x,y-1)
                            if matrix[x][y] != " ":
                                matrix[x][y].setExplosion(matrix,x,y)       # J2
                            if matrix[x][y-2] != " ":
                                matrix[x][y-2].setExplosion(matrix,x,y-2)
                            if matrix[x][y+1] != " ":
                                matrix[x][y+1].setExplosion(matrix,x,y+1)

                            newCandy=SpecialCandy.SpecialCandy(sweetSpecialColor,"SPH", 7)

                            matrix[x][y]=newCandy

                            waterFall(x,y)

                            score+=(50*4)

                            return
            else:

                if x-1 >= 0 and matrix[x-1][y].getColor() == matrix[x][y].getColor():
                    if x-2 >= 0 and matrix[x-2][y].getColor() == matrix[x][y].getColor():
                        if x+1 < 9 and matrix[x+1][y].getColor() == matrix[x][y].getColor():

                            if matrix[x][y-2] != " ":
                                matrix[x][y-2].setExplosion(matrix,x,y-2)
                            if matrix[x][y-1] != " ":
                                matrix[x][y-1].setExplosion(matrix,x,y-1)     # J16
                            if matrix[x][y] != " ":
                                matrix[x][y].setExplosion(matrix,x,y)
                            if matrix[x-1][y] != " ":
                                matrix[x-1][y].setExplosion(matrix,x-1,y)
                            if matrix[x-2][y] != " ":
                                matrix[x-2][y].setExplosion(matrix,x-2,y)
                            if matrix[x+1][y] != " ":
                                matrix[x+1][y].setExplosion(matrix,x+1,y)

                            waterFall(x,y)

                            score+=(50*6)

                            return
                #********************************************************+
                    else:
                        if x+1 < 9 and matrix[x+1][y].getColor()==matrix[x][y].getColor():
                            if x+2 >= 0 and matrix[x+2][y].getColor()==matrix[x][y].getColor():

                                if matrix[x][y-2] != " ":
                                    matrix[x][y-2].setExplosion(matrix,x,y-2)
                                if matrix[x][y-1] != " ":
                                    matrix[x][y-1].setExplosion(matrix,x,y-1)     # J20
                                if matrix[x][y] != " ":
                                    matrix[x][y].setExplosion(matrix,x,y)
                                if matrix[x-1][y] != " ":
                                    matrix[x-1][y].setExplosion(matrix,x-1,y)
                                if matrix[x+2][y] != " ":
                                    matrix[x+2][y].setExplosion(matrix,x+2,y)
                                if matrix[x+1][y] != " ":
                                    matrix[x+1][y].setExplosion(matrix,x+1,y)

                                waterFall(x,y)
                                score+=(50*6)
                                return
                else:

                    if matrix[x][y-2] != " ":
                        matrix[x][y-2].setExplosion(matrix,x,y-2)
                    if matrix[x][y-1] != " ":
                        matrix[x][y-1].setExplosion(matrix,x,y-1)     # J3
                    if matrix[x][y] != " ":
                        matrix[x][y].setExplosion(matrix,x,y)

                    waterFall(x,y)
                    score+=(50*3)

                    return
        elif y+1 < 9 and matrix[x][y+1].getColor()==matrix[x][y].getColor():
            if y+2 < 9 and matrix[x][y+2].getColor()==matrix[x][y].getColor():
                if y-1 >= 0 and matrix[x][y-1].getColor()==matrix[x][y].getColor():

                    if x-1 >= 0 and matrix[x-1][y].getColor()==matrix[x][y].getColor():
                        if x-2 >= 0 and matrix[x-2][y].getColor()==matrix[x][y].getColor():

                            if matrix[x][y-2] != " ":
                                matrix[x][y-2].setExplosion(matrix,x,y-1)
                            if matrix[x][y] != " ":
                                matrix[x][y].setExplosion(matrix,x,y)       # J15
                            if matrix[x][y+1] != " ":
                                matrix[x][y+1].setExplosion(matrix,x,y+1)
                            if matrix[x][y+2] != " ":
                                matrix[x][y+2].setExplosion(matrix,x,y+2)
                            if matrix[x-1][y] != " ":
                                matrix[x-1][y].setExplosion(matrix,x,y-1)
                            if matrix[x-2][y] != " ":
                                matrix[x-2][y].setExplosion(matrix,x-2,y)
                            waterFall(x,y)
                            score+=(50*6)

                            return


                    elif x+1 < 9 and matrix[x+1][y].getColor()==matrix[x][y].getColor():
                        if x+2 < 9 and matrix[x+2][y].getColor()==matrix[x][y].getColor():

                            if matrix[x][y-1] != " ":
                                matrix[x][y-1].setExplosion(matrix,x,y-1)
                            if matrix[x][y] != " ":
                                matrix[x][y].setExplosion(matrix,x,y)       # J18
                            if matrix[x][y+1] != " ":
                                matrix[x][y+1].setExplosion(matrix,x,y+1)
                            if matrix[x][y+2] != " ":
                                matrix[x][y+2].setExplosion(matrix,x,y+2)
                            if matrix[x+1][y] != " ":
                                matrix[x+1][y].setExplosion(matrix,x+1,y)
                            if matrix[x+2][y] != " ":
                                matrix[x+2][y].setExplosion(matrix,x+2,y)

                            waterFall(x,y)
                            score+=(50*6)

                            return


                    else:

                        sweetSpecialColor=matrix[x][y].getColor()
                        newCandy=SpecialCandy.SpecialCandy(sweetSpecialColor,"SPH", 7)

                        if matrix[x][y-1] != " ":
                            matrix[x][y-1].setExplosion(matrix,x,y-1)
                        if matrix[x][y] != " ":
                            matrix[x][y].setExplosion(matrix,x,y)       # J4
                        if matrix[x][y+1] != " ":
                            matrix[x][y+1].setExplosion(matrix,x,y+1)
                        if matrix[x][y+2] != " ":
                            matrix[x][y+2].setExplosion(matrix,x,y+2)

                        matrix[x][y]=newCandy
                        waterFall(x,y)
                        score+=(50*4)

                        return

            elif y-1 >= 0 and matrix[x][y-1].getColor()==matrix[x][y].getColor():

                if matrix[x][y-1] != " ":
                    matrix[x][y-1].setExplosion(matrix,x,y-1)
                if matrix[x][y] != " ":
                    matrix[x][y].setExplosion(matrix,x,y)    #J6
                if matrix[x][y+1] != " ":
                    matrix[x][y+1].setExplosion(matrix,x,y+1)

                waterFall(x,y)
                score+=(50*3)

                return

    elif y+1 < 9 and matrix[x][y+1].getColor()==matrix[x][y].getColor():
        if y+2 < 9 and matrix[x][y+2].getColor()==matrix[x][y].getColor():
            if x-1 >= 0 and matrix[x-1][y].getColor()==matrix[x][y].getColor():


                if x-2 >= 0 and matrix[x-2][y].getColor()==matrix[x][y].getColor():
                    if x+1 < 9 and matrix[x+1][y].getColor()==matrix[x][y].getColor():

                        SweetSpecialColor=matrix[x][y].getColor()
                        newCandy=SpecialCandy.SpecialCandy(SweetSpecialColor,"SPH",7)

                        if matrix[x-1][y] != " ":
                            matrix[x-1][y].setExplosion(matrix,x-1,y)
                        if matrix[x-2][y] != " ":
                            matrix[x-2][y].setExplosion(matrix,x-2,y)
                        if matrix[x+1][y] != " ":
                            matrix[x+1][y].setExplosion(matrix,x+1,y)
                        if matrix[x][y] != " ":
                            matrix[x][y].setExplosion(matrix,x,y)
                        if matrix[x][y+1] != " ":
                            matrix[x][y+1].setExplosion(matrix,x,y+1)  # J13
                        if matrix[x][y+2] != " ":
                            matrix[x][y+2].setExplosion(matrix,x,y+2)

                        matrix[x+1][y]=newCandy
                    #function to lower candy
                        waterFall(x,y)
                        score+=(50*6)

                        return

                else:
                    if x+1 < 9 and matrix[x+1][y].getColor()==matrix[x][y].getColor():
                        if x+2 < 9 and matrix[x+2][y].getColor()==matrix[x][y].getColor():

                            if matrix[x-1][y] != " ":
                                matrix[x-1][y].setExplosion(matrix,x-1,y)
                            if matrix[x+2][y] != " ":
                                matrix[x+2][y].setExplosion(matrix,x+2,y)
                            if matrix[x+1][y] != " ":
                                matrix[x+1][y].setExplosion(matrix,x+1,y)
                            if matrix[x][y] != " ":
                                matrix[x][y].setExplosion(matrix,x,y)
                            if matrix[x][y+1] != " ":
                                matrix[x][y+1].setExplosion(matrix,x,y+1)     # J17
                            if matrix[x][y+2] != " ":
                                matrix[x][y+2].setExplosion(matrix,x,y+2)

                            waterFall(x,y)
                            score+=(50*6)
                            return


            else:

                if matrix[x][y] != " ":
                    matrix[x][y].setExplosion(matrix,x,y)
                if matrix[x][y+1] != " ":
                    matrix[x][y+1].setExplosion(matrix,x,y+1)  #J5
                if matrix[x][y+2] != " ":
                    matrix[x][y+2].setExplosion(matrix,x,y+2)

                waterFall(x,y)
                score+=(50*3)

                return
#-----------------------------------------------------------------------------------------------------------
    #This "else" validates the vertical plays
    else:
        if x-1 >= 0 and matrix[x-1][y].getColor()==matrix[x][y].getColor():
            if x-2 >= 0 and matrix [x-2][y].getColor()==matrix[x][y].getColor():
                if x+1 < 9 and matrix[x+1][y].getColor()==matrix[x][y].getColor():
                    if x+2 < 9 and matrix[x+2][y].getColor()==matrix[x][y].getColor():

                        newCandy=DiscoBallCandy.DiscoBallCandy("MUL", "SPM", 8)

                        if matrix[x-2][y] != " ":
                            matrix[x-2][y].setExplosion(matrix,x-2,y)
                        if matrix[x-1][y] != " ":
                            matrix[x-1][y].setExplosion(matrix,x-1,y)
                        if matrix[x][y] != " ":
                            matrix[x][y].setExplosion(matrix,x,y)               # J7
                        if matrix[x+1][y] != " ":
                            matrix[x+1][y].setExplosion(matrix,x+1,y)
                        if matrix[x+2][y] != " ":
                            matrix[x+2][y].setExplosion(matrix,x+2,y)

                        matrix[x+2][y]=newCandy
                        waterFall(x,y)
                        score+=(50*5)

                        return
                    else:

                        sweetSpecialColor=matrix[x][y].getColor()
                        newCandy=SpecialCandy.SpecialCandy(sweetSpecialColor, "SPV", 9)

                        if matrix[x-2][y] != " ":
                            matrix[x-2][y].setExplosion(matrix,x-2,y)
                        if matrix[x-1][y] != " ":
                            matrix[x-1][y].setExplosion(matrix,x-1,y)
                        if matrix[x][y] != " ":
                            matrix[x][y].setExplosion(matrix,x,y)   # J8
                        if matrix[x+1][y] != " ":
                            matrix[x+1][y].setExplosion(matrix,x+1,y)

                        matrix[x+1][y]=newCandy
                        waterFall(x,y)
                        score+=(50*4)

                        return

                else:

                    if matrix[x-2][y] != " ":
                        matrix[x-2][y].setExplosion(matrix,x-2,y)
                    if matrix[x-1][y] != " ":
                        matrix[x-1][y].setExplosion(matrix,x-1,y)  # J9
                    if matrix[x][y] != " ":
                        matrix[x][y].setExplosion(matrix,x,y)

                    waterFall(x,y)
                    score+=(50*3)

                    return

            elif x+1 < 9 and matrix[x+1][y].getColor() == matrix[x][y].getColor():
                if x+2 < 9 and matrix[x+2][y].getColor()==matrix[x][y].getColor():

                    SweetSpecialColor=matrix[x][y].getColor()
                    newCandy=SpecialCandy.SpecialCandy(SweetSpecialColor,"SPV", 9)

                    if matrix[x-1][y] != " ":
                        matrix[x-1][y].setExplosion(matrix,x-1,y)
                    if matrix[x][y] != " ":
                        matrix[x][y].setExplosion(matrix,x,y)      # J10
                    if matrix[x+1][y] != " ":
                        matrix[x+1][y].setExplosion(matrix,x+1,y)
                    if matrix[x+2][y] != " ":
                        matrix[x+2][y].setExplosion(matrix,x+2,y)

                    matrix[x+2][y]=newCandy
                    waterFall(x,y)
                    score+=(50*4)

                    return

                else:

                    if matrix[x-1][y] != " ":
                        matrix[x-1][y].setExplosion(matrix,x-1,y)
                    if matrix[x][y] != " ":
                        matrix[x][y].setExplosion(matrix,x,y)   # J11
                    if matrix[x+1][y] != " ":
                        matrix[x+1][y].setExplosion(matrix,x+1,y)

                    waterFall(x,y)
                    score+=(50*3)

                    return

        elif x+1 < 9 and matrix[x+1][y].getColor()==matrix[x][y].getColor():
            if x+2 < 9 and matrix[x+2][y].getColor()==matrix[x][y].getColor():

                if matrix[x][y] != " ":
                    matrix[x][y].setExplosion(matrix,x,y)
                if matrix[x+1][y] != " ":
                    matrix[x+1][y].setExplosion(matrix,x+1,y)  #J12
                if matrix[x+2][y] != " ":
                    matrix[x+2][y].setExplosion(matrix,x+2,y)

                waterFall(x,y)
                score+=(50*3)

                return

#-----------------------------------------------------------------------------------------------------------------------
def discBallPlay(color,x,y):

    global score

    numExplotions = 0

    j = 0
    while j < 9:#loop for the columns

        for i in range(9):#autoincrese loop for the rows

            if matrix[i][j] != " " and matrix[i][j].getColor() == color.getColor() :#if the object is like the color select
                    matrix[i][j].setExplosion(matrix, i, j) #if is the color, delete with 0
                    numExplotions += 1
        j+=1

    matrix[x][y] = " "
    waterFall(x,y)
    refill(x,y)
    score += (numExplotions*50)

#-----------------------------------------------------------------------------------------------------------------------

def searchConsecutive(i,j,color):

    aux_i = i
    aux_j = j
    conterHorz =1
    counter = 0

    first_j = j
    last_j = j

    first_i = i
    last_i = i

    special_i = ""
    special_j = ""

    specialHorz = False
    specialVert = False


    while aux_j-1 >= 0:
        if matrix[i][aux_j-1].getColor() == color.getColor():
            if matrix[i][aux_j-1].getType() == "SPV":
                specialVert = True
            if matrix[i][aux_j-1].getType() == "SPH":
                specialHorz = True

            aux_j-=1
            conterHorz +=1
            first_j = aux_j
        else:
            break
    aux_j = j
    while aux_j+1 < 9:
        if matrix[i][aux_j+1].getColor() == color.getColor():
            if matrix[i][aux_j+1].getType() == "SPV":
                specialVert = True
                special_j = aux_j+1
            if matrix[i][aux_j+1].getType() == "SPH":
                specialHorz = True
                special_j = aux_j+1

            aux_j+=1
            conterHorz +=1
            last_j = aux_j
        else:
            break
    print(specialVert,specialHorz)

    if conterHorz < 3:
        first_j = j
        last_j = j
        conterHorz = 1
        counter += conterHorz

    elif conterHorz >= 3:
        counter += conterHorz
        if conterHorz == 3:
            if specialHorz or specialVert:
                if specialHorz:
                    for y in range(9):
                        matrix[i][y] = ""
                if specialVert:
                    for x in range(9):
                        matrix[x][special_j] = ""
            else:
                while conterHorz > 0:

                    matrix[i][first_j] = ""
                    if first_j < 9 and first_j < last_j:

                        first_j +=1
                        conterHorz -= 1
                    else:
                        break
        elif conterHorz == 4:

            while conterHorz > 0:

                if first_j == j:
                    colorSpec = matrix[i][j].getColor()
                    candySpec = Candy(colorSpec, "SPH",6)
                    matrix[i][j] = candySpec

                elif first_j < 9 and first_j <= last_j:
                    matrix[i][first_j] = ""

                first_j +=1
                conterHorz -= 1


        elif conterHorz == 5:

            while conterHorz >= 0:
                if first_j == j:
                    colorSpec = matrix[i][j].getColor()
                    candySpec = Candy("MUL", "SPM",6)
                    matrix[i][j] = candySpec

                if first_j < 9 and first_j <= last_j:

                    matrix[i][first_j] = ""
                    first_j +=1
                    conterHorz -= 1

                first_j +=1
                conterHorz -= 1

    waterFall()
    specialHorz = False
    specialVert = False

    conterVert = 1
    aux_i = i
    while aux_i-1 >= 0:
        if matrix[aux_i-1][j].getColor() == color.getColor():
            if matrix[aux_i-1][j].getType() == "SPV":
                specialVert = True
            if matrix[aux_i-1][j].getType() == "SPH":
                specialHorz = True


            aux_i-=1
            conterVert +=1
            first_i = aux_i
        else:
            break
    aux_i = i
    while aux_i+1 < 9:
        if matrix[aux_i+1][j].getColor() == color.getColor():
            if matrix[aux_i+1][j].getType() == "SPV":
                specialVert = True
            if matrix[aux_i+1][j].getType() == "SPH":
                specialHorz = True

            aux_i+=1
            conterVert +=1
            last_i = aux_i
        else:
            break


    if conterVert < 3:
        first_i = i
        last_i = i
        conterVert = 1
        counter += conterHorz


    elif conterVert >= 3:
        counter += conterHorz


        if conterVert == 3:
            if specialHorz or specialVert:
                if specialHorz:
                    for y in range(9):
                        matrix[i][y] = ""
                if specialVert:
                    for x in range(9):
                        matrix[x][j] = ""
            else:
                while conterVert > 0:
                    matrix[first_i][j] = ""

                    if first_i < 9 and first_i < last_i:

                        first_i +=1
                        conterVert -= 1
                    else:
                        break

        elif conterVert == 4:
            colorSpec = matrix[i][j].getColor()
            candySpec = Candy(colorSpec, "SPV",6)
            matrix[last_i][j] = candySpec

            while conterVert > 0:

                if first_i == i:
                    first_i +=1
                    conterVert -= 1

                elif first_i != i and first_i < 9 and first_i <= last_i:
                    matrix[first_i][j] = ""
                    first_i +=1
                    conterVert -= 1

                first_i +=1
                conterVert -= 1



        elif conterVert == 5:

            while conterVert > 0:

                if first_i == i:
                    candySpec = Candy("MUL", "SPM",6)
                    matrix[last_i][j] = candySpec

                elif first_i < 9 and first_i < last_i:
                    matrix[i][first_i] = ""

                first_i +=1
                conterHorz -= 1

    waterFall()

#-----------------------------------------------------------------------------------------------------------------------
def waterFall(x,y):

    spacesCont =0
    aux_i = 0
    j = 0
    while j < 9:#loop for the columns

        for i in range(9):#autoincrese loop for the rows
            print(i)
            if matrix[i][j] == " " :#if the object is like the color select
                spacesCont += 1 #var to count the spaces


            if i <= 8 and spacesCont != 0:#z
                aux_i = i-1

                if matrix[i][j] == " " and i > 0:

                    while aux_i >= 0:

                        while aux_i >= 0 and matrix[aux_i][j] == " " and spacesCont > 0:
                            aux_i -= 1

                        if aux_i >= 0:
                            while matrix[i][j] != " " and i > 0:
                                i-=1

                            if i > 0:
                                matrix[i][j] = matrix[aux_i][j]
                                matrix[aux_i][j] = " "
                                aux_i -=1

            spacesCont = 0
        j+=1

    refill(x,y)

#-----------------------------------------------------------------------------------------------------------------------
def searchPlays(x,y):

    global score

    i=0
    while i+2 < 9:
        j=0

        while  j < 9:

            if matrix[i][j].getColor() == matrix[i+1][j].getColor() == matrix[i+2][j].getColor():

                color = matrix[i][j]

                spacesCont = 3
                if i+3 < 9 and matrix[i+3][j].getColor() == color.getColor():#dulce especial vertical......

                    if i+4 < 9 and matrix[i+4][j].getColor() == color.getColor():

                        #se crea la bola de disco
                        candyBall = Candy("MUL", "SPM",6)
                        matrix[i+4][j] = candyBall

                        spacesCont += 1

                    elif i+3 < 9 and matrix[i+3][j].getColor() == color.getColor():

                        colorSpec = color.getColor()
                        candySpec = SpecialCandy.SpecialCandy(colorSpec, "SPV",6)
                        matrix[i+3][j] = candySpec

                if spacesCont == 3:
                    if matrix[i][j] != " ":
                        matrix[i][j].setExplosion(matrix,i,j)
                    elif matrix[i+1][j] != " ":
                        matrix[i+1][j].setExplosion(matrix,i+1,j)
                    if matrix[i+2][j] != " ":
                        matrix[i+2][j].setExplosion(matrix,i+2,j)

                    first_i = i+2
                    last_i = i-1

                    if matrix[last_i][j] != " ":
                        print(matrix[last_i][j])

                        while first_i >= 0 and last_i >=0 and matrix[first_i][j] == " " and matrix[last_i][j] != " ":

                            matrix[first_i][j] = matrix[last_i][j]
                            matrix[last_i][j]=" "
                            first_i -=1
                            last_i -=1

                    score +=(50*3)
                    waterFall(x,y)
                    i= 0
                    j= -1

                if spacesCont == 4:

                    if matrix[i][j] != " ":
                        matrix[i][j].setExplosion(matrix,i,j)
                    elif matrix[i+1][j] != " ":
                        matrix[i+1][j].setExplosion(matrix,i+1,j)
                    elif matrix[i+2][j] != " ":
                        matrix[i+2][j].setExplosion(matrix,i+2,j)
                    elif matrix[i+3][j] != " ":
                        matrix[i+3][j].setExplosion(matrix,i+3,j)

                    first_i = i+3
                    last_i = i-1

                    if matrix[last_i][j] != " ":

                        while first_i >= 0 and last_i >=0 and matrix[first_i][j] == " " and matrix[last_i][j] != " ":

                            matrix[first_i][j] = matrix[last_i][j]
                            matrix[last_i][j]=" "
                            first_i -=1
                            last_i -=1
                        score +=(50*4)
                    waterFall(x,y)
                    i= 0
                    j= -1

                spacesCont = 0
            j +=1
        i +=1


    i=0
    while i < 9:
        j=0

        while j < 7:

            if matrix[i][j].getColor() == matrix[i][j+1].getColor() == matrix[i][j+2].getColor():
                color = matrix[i][j]

                spacesCont = 3
                if j+4 < 9 and matrix[i][j+3].getColor() == matrix[i][j+4].getColor() == color.getColor():#dulce especial vertical.....
                #se crea la bola de disco

                        candyBall = Candy("MUL", "SPM",6)
                        matrix[i][j+4] = candyBall
                        matrix[i][j+3].setExplosion(matrix,i,j+3)
                        spacesCont += 1

                elif j+3 < 9 and matrix[i][j+3].getColor() == color.getColor():
                            #se crea el dulce especial vertical en la pocision

                        colorSpec = color.getColor()
                        candySpec = SpecialCandy.SpecialCandy(colorSpec, "SPH",6)
                        matrix[i][j+3] = candySpec

                if spacesCont == 3:
                    if matrix[i][j] != " ":
                        matrix[i][j].setExplosion(matrix,i,j)
                    elif matrix[i][j+1] != " ":
                        matrix[i][j+1].setExplosion(matrix,i,j+1)
                    elif matrix[i][j+2] != " ":
                        matrix[i][j+2].setExplosion(matrix,i,j+2)

                    first_i = i
                    aux_i = i-1
                    while aux_i >= 0 and matrix[aux_i][j] != " " and matrix[first_i][j] == " ":

                        matrix[first_i][j] = matrix[aux_i][j]
                        matrix[first_i][j+1] = matrix[aux_i][j+1]
                        matrix[first_i][j+2] = matrix[aux_i][j+2]

                        matrix[aux_i][j]=" "
                        matrix[aux_i][j+1]=" "
                        matrix[aux_i][j+2]=" "

                        aux_i -=1
                        first_i -=1
                    score +=(50*3)
                    waterFall(x,y)
                    i= 0
                    j= -1

                if spacesCont == 4:

                    if matrix[i][j] != " ":
                        matrix[i][j].setExplosion(matrix,i,j)
                    elif matrix[i][j+1] != " ":
                        matrix[i][j+1].setExplosion(matrix,i,j+1)
                    elif matrix[i][j+2] != " ":
                        matrix[i][j+2].setExplosion(matrix,i,j+2)
                    if matrix[i][j+3] != " ":
                        matrix[i][j+3].setExplosion(matrix,i,j+3)

                    first_i = i
                    aux_i = i-1
                    while aux_i >= 0 and matrix[aux_i][j] != " " and matrix[first_i][j] == " ":

                        matrix[first_i][j] = matrix[aux_i][j]
                        matrix[first_i][j+1] = matrix[aux_i][j+1]
                        matrix[first_i][j+2] = matrix[aux_i][j+2]
                        matrix[first_i][j+3] = matrix[aux_i][j+2]

                        matrix[aux_i][j]=" "
                        matrix[aux_i][j+1]=" "
                        matrix[aux_i][j+2]=" "
                        matrix[aux_i][j+3]=" "

                        aux_i -=1
                        first_i -=1
                    score +=(50*4)
                    waterFall(x,y)
                    i= 0
                    j= -1

                spacesCont = 0

            j +=1
        i +=1

#-----------------------------------------------------------------------------------------------------------------------
def refill(x,y):
    i=8
    while i >= 0:
        j=8
        while  j >= 0 :
            aux_i = i
            while aux_i >= 0 and matrix[aux_i][j] == " ":

                    num=random.randint(1,4)
                    matrix[i][j] = listObjects[num]
                    aux_i-=1
            j-=1
        i-=1
    searchPlays(x,y)


    return

#-----------------------------------------------------------------------------------------------------------------------
CreateMatrix()
menu()
#-----------------------------------------------------------------------------------------------------------------------