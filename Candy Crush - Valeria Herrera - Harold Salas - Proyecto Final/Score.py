#from Main import *

score=[]
topscoresnames = []
from User import *
#-----------------------------------------------------------------------------------------------------------------------
def SaveCurrentPlayer(name, score):  #Save the information in the file

    file=open("TopScore.txt","a")
    file.write(name+"*")
    file.write(str(score)+"*")
    file.write("\n")

    file.close()
#-----------------------------------------------------------------------------------------------------------------------
def CreatePlayer(ratingAux):  #Create objects from the information found in the files
    users=[]
    x=0

    while x<=len(ratingAux)-1:

        newUser=User(ratingAux[x], ratingAux[x+1])
        users.append(newUser)

        x+=2

    ShowBetterPlayers(users)
#-----------------------------------------------------------------------------------------------------------------------
def ShowBetterPlayers(users):
    #function displays the best five scores

    topscoresnames.clear()

    #Validates if the list no more than five scores
    if len(users)>1:
        if len(users)==1:
            bestPlayer=users[0].getName()+ "  "+ str(users[0].getScore())
            secondPlayer="-----------------------------------"
            thirdPlayer="-----------------------------------"
            fourthPlayer="-----------------------------------"
            fifthPlayer="-----------------------------------"

        elif len(users)==2:
            bestPlayer=users[0].getName()+ "  "+ str(users[0].getScore())
            secondPlayer=users[1].getName()+ "  "+ str(users[1].getScore())
            thirdPlayer="-----------------------------------"
            fourthPlayer="-----------------------------------"
            fifthPlayer="-----------------------------------"

        elif len(users)==3:
            bestPlayer=users[0].getName()+ "  "+ str(users[0].getScore())
            secondPlayer=users[1].getName()+ "  "+ str(users[1].getScore())
            thirdPlayer=users[2].getName()+ "  "+ str(users[2].getScore())
            fourthPlayer="-----------------------------------"
            fifthPlayer="-----------------------------------"

        elif len(users)==4:
            bestPlayer=users[0].getName()+ "  "+ str(users[0].getScore())
            secondPlayer=users[1].getName()+ "  "+ str(users[1].getScore())
            thirdPlayer=users[2].getName()+ "  "+ str(users[2].getScore())
            fourthPlayer=users[3].getName()+ "  "+ str(users[3].getScore())
            fifthPlayer="-----------------------------------"

        elif len(users)==5:
            bestPlayer=users[0].getName()+ "  "+ str(users[0].getScore())
            secondPlayer=users[1].getName()+ "  "+ str(users[1].getScore())
            thirdPlayer=users[2].getName()+ "  "+ str(users[2].getScore())
            fourthPlayer=users[3].getName()+ "  "+ str(users[3].getScore())
            fifthPlayer=users[4].getName()+ "  "+ str(users[4].getScore())
        else:
            bestPlayer=users[0].getName()+ "  "+ str(users[0].getScore())
            secondPlayer=users[1].getName()+ "  "+ str(users[1].getScore())
            thirdPlayer=users[2].getName()+ "  "+ str(users[2].getScore())
            fourthPlayer=users[3].getName()+ "  "+ str(users[3].getScore())
            fifthPlayer=users[4].getName()+ "  "+ str(users[4].getScore())


        print("1.",bestPlayer)
        print("2.",secondPlayer)
        print("3.",thirdPlayer)
        print("4.",fourthPlayer)
        print("5.",fifthPlayer)

        topscoresnames.append(bestPlayer)
        topscoresnames.append(secondPlayer)
        topscoresnames.append(thirdPlayer)
        topscoresnames.append(fourthPlayer)
        topscoresnames.append(fifthPlayer)




#-----------------------------------------------------------------------------------------------------------------------
def DeleteScores(): #function clean the file
    file=open("TopScore.txt","w")
    file.close()

#-----------------------------------------------------------------------------------------------------------------------
def fileUpload(users):

    ratings = []
    #Open the file and separates the ".split" and adds them to the list ratings
    file=open("TopScore.txt", "r")  #

    for i in file:
        rating=i.split("*")
        ratings.append(rating)
    file.close()
    #validates that will not fall if the list is empty
    if len(ratings)==0:
        print("No scores recorded")

    else:
        #adds them in different lists, separating the name of your score
        for i in ratings:
            users.append(i[0])
            valor=int(i[1])
            users.append(valor)
            score.append(valor)
        #sort the list of highest to lowest
        score.sort(reverse=True)
        ratings=[]

        #ordered a new user name list with the value
        while score!=[]:
            num=score[0]
            conta=0

            for i in users:
                if i==num:
                    ratings.append(users[conta-1])
                    ratings.append(score[0])
                    users.remove(users[conta])
                    users.remove(users[conta-1])
                    score.remove(score[0])
                    break

                conta+=1

        CreatePlayer(ratings)
