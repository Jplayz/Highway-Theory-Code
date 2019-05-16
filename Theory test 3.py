import easygui as eg
import random

#Dictionary with all the signs in
def ListInit():
    global SignsDict
    global WrongAns
    SignsDict = [
        "AheadOnly.gif",
        "Crossroads.gif",
        "CycleRoute.gif",
        "FallingRocks.gif",
        "LevelCrossing.gif",
        "MinimumSpeed.gif",
        "NoCycles.gif",
        "NoEntry.gif",
        "NoMotorVehicles.gif",
        "NoOvertaking.gif",
        "NoStopping.gif",
        "NoThroughRoad.gif",
        "NoVehiclesCarryingExplosives.gif",
        "NoVehiclesOverThisHeight.gif",
        "OpeningBridgeAhead.gif",
        "Sidewinds.gif",
        "SteepHill.gif",
        "TurnLeft.gif",
        "UnevenRoads.gif"]

    #Keeps track of all the wrong signs
    WrongAns = []

#Sets up the startmenu which will be called later
def StartMenu():
    choice = eg.buttonbox("HIGHWAY CODE TEST", choices=("Start","Quit"))

    #This starts the quiz
    if choice == "Start":
        ListInit()
        Counter = 0
        Marks = 0
        Quiz(Counter,Marks)

    #This closes the quiz
    elif choice == "Quit":
        exit()

        
def Quiz(Counter, Marks):
    Counter += 1

    #This will generate the correct answer for the question
    AnswerGen = random.randint(0,len(SignsDict)-1)
    Answer = SignsDict[AnswerGen]                       #Gets the correct answers
    del SignsDict[AnswerGen]                            #Removes it from index so it won't return in this set of questioning
    ClearAns = Answer.split(".")                        #Removes the .gif part
    Message = "Which of is {}?".format(ClearAns[0])
    images = GetImages(Answer)
    
    Question = eg.buttonbox(msg=Message, choices=["Pass"], images=images) #This sets up the button box

    #Checks to see if answer is correct
    if Question == Answer:
        Marks += 1

    if Question != Answer:
        WrongAns.append(ClearAns[0])

    #Moves the program on when Counter limit is reached    
    if Counter == 5:
        FinalResults(Marks)

        
    Quiz(Counter,Marks)



def GetImages(Answer):
    Images = [None, None, None]                         #Sets up the array of images

    #Generating the two other images
    ImageGen1 = random.randint(0,len(SignsDict)-1)      
    ImageGen2 = random.randint(0,len(SignsDict)-1)

    #Finds the placement of the images in the array
    OtherImage1 = SignsDict[ImageGen1]
    OtherImage2 = SignsDict[ImageGen2]

    ImageCheck = True
    #Checking that they aren't duplicates
    while ImageCheck == True:
        if OtherImage1 == OtherImage2:
            OtherImage2 = random.randint(0,len(SignsDict))
            
        else:
            ImageCheck = False

    OtherImage = [OtherImage1, OtherImage2]             #Array with the extra images in
    Placement = random.randint(0,2)
    Images[Placement] = Answer

    #Filling up the rest of the array
    for x in range(0,3):
        if Images[x] == None:
            Images[x] = OtherImage[0]
            del OtherImage[0]

        else:
            next

    return Images

def FinalResults(Marks):
    Message = """Thank you for taking the test,you scored {} out of 5.
The signs you need to work on are as followed {}""".format(Marks,WrongAns)
    eg.msgbox(msg=Message)
    StartMenu()
    
    
StartMenu()
