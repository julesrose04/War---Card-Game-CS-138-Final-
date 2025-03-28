from graphics import *
from myFinalFunctions import *
import random
import time

#Width and height of main menu only.
#win2 dimensions: 700 x 800
W, H = 800, 513
#Defining main menu with splashScreen function.
win2 = splashScreen(W, H)

#Creating start button for game window.
drawCardButton, drawLabel = drawButton(Point(700//2, 800//2), win2, 200, 50, 'Click to begin!')

#Function for handling logic behind end game
def exitScreen():
    """Creates two buttons for end game then creates logic for replaying the game after end game
        is reached. 

    Returns:
        'play' if user chooses to replay game - opens splashscreen and allows user to replay
        'quit' if user chooses to quit game - closes win2
    """
    #Creating button to allow player to play again
    playAgainButton = Button(Point(700//2, 365), win2, 200, 50, 'Menu', 'gray')
    playAgainButton.activate()

    #Creating new quit button for end game
    quitButton2 = Button(Point(700//2, 430), win2, 200, 50, 'Quit', 'gray')
    quitButton2.activate()

    #Covering the quit button that was displayed during the game.
    quitCover = Rectangle(Point(530, 700), Point(650, 775))
    quitCover.setFill('green')
    quitCover.setOutline('green')
    quitCover.draw(win2)

    #Covering the draw card button that was displayed during the game.
    drawCover = Rectangle(Point(500, 710), Point(700, 790))
    drawCover.setFill('green')
    drawCover.setOutline('green')
    drawCover.draw(win2)

    #While loop to determine which button was clicked at end game
    #Restart to menu or quit the game 
    while True:
        p = win2.getMouse()

        if playAgainButton.clicked(p):
    
            for items in win2.items[:]:
                items.undraw()
            return 'play'
        elif quitButton2.clicked(p):
            win2.close()
            return 'quit'

#While loop to check if quit button in game window was clicked.
while True:
    p = win2.getMouse()
    #If statement to check that begin button was clicked, then 
    #starts main function for game
    if clicked(drawCardButton, p):
        drawCardButton.undraw()
        drawLabel.undraw()
        randomCard(win2)   #Main function for the game

        #Handles logic for endgame
        result = exitScreen()
        if result == 'play': #If user hits menu
            win2.close() #Close game screen
            win2 = splashScreen(W,H) #Reopen splashscreen
            drawCardButton, drawLabel = drawButton(Point(700//2, 800//2), win2, 200, 50, 'Click to begin!')
        elif result == 'quit': #If user hits quit, exit game
            break