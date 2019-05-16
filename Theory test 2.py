import easygui as eg

#Sets up the startmenu which will be called later
def StartMenu():
    choice = eg.buttonbox("HIGHWAY CODE TEST", choices=("Start","Quit"))

    #This starts the quiz
    if choice == "Start":
        Quiz()

    #This closes the quiz
    elif choice == "Quit":
        next


#Setting up quiz
def Quiz():
    Marks = 0 #Sets up a counter for the marks
    Wrong = [] #Sets up a list with all the images user needs to learn

#-
    #Setting up question one
    images = "AheadOnly.gif","FallingRocks.gif","SteepHill.gif" #This is the list of images which will be used
    Question = eg.buttonbox(msg="Which of these warns of falling rocks?", choices=["Pass"], images=images) #This sets up the button box

    #Checking the answer is correct
    if Question == "FallingRocks.gif":
        Marks += 1
        eg.msgbox("You got it correct!", ok_button="Next")
        
    else:
        eg.msgbox("You got it wrong!", ok_button="Next")
        Wrong.append("FallingRocks.gif")

#-
    #Setting up question two
    images = "NoStopping.gif","NoOvertaking.gif","AheadOnly.gif" #This is the list of images which will be used
    Question = eg.buttonbox(msg="Which of these means ‘No stopping’?", choices=["Pass"], images=images) #This sets up the button box

    #Checking the answer is correct
    if Question == "NoStopping.gif":
        Marks += 1
        eg.msgbox("You got it correct!", ok_button="Next")
        
    else:
        eg.msgbox("You got it wrong!", ok_button="Next")
        Wrong.append("NoStopping.gif")

#-
    #Setting up question three
    images = "Sidewinds.gif","TurnLeft.gif","NoEntry.gif" #This is the list of images which will be used
    Question = eg.buttonbox(msg="Which of these means there are strong side winds?", choices=["Pass"], images=images) #This sets up the button box

    #Checking the answer is correct
    if Question == "Sidewinds.gif":
        Marks += 1
        eg.msgbox("You got it correct!", ok_button="Next")
        
    else:
        eg.msgbox("You got it wrong!", ok_button="Next")
        Wrong.append("Sidewinds.gif")
        
        
        
    #Setting up question four
    images = "NoMotorVehicles.gif","CycleRoute.gif","NoVehiclesOverThisHeight.gif" #This is the list of images which will be used
    Question = eg.buttonbox(msg="Which of these means no motor vehicles allowed?", choices=["Pass"], images=images) #This sets up the button box

    #Checking the answer is correct
    if Question == "NoMotorVehicles.gif":
        Marks += 1
        eg.msgbox("You got it correct!", ok_button="Next")
        
    else:
        eg.msgbox("You got it wrong!", ok_button="Next")
        Wrong.append("NoMotorVehicles.gif")
        







StartMenu()
