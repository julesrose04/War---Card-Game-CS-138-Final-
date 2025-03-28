from graphics import *
#Draw a button, label
def drawButton(center, win, w, h, text):
    """Draws a button to screen and also a label within the button.

    Args:
        center (Point): Center point of rectangle for button
        win (GraphWin): Which window the button should be printed to
        w (Int): Width of button
        h (Int): Height of button
        text (String): Text for button

    Returns:
        button, label

    Example: myButton = drawButton(Point(250, 400), win, 200, 50, 'string')
    """
    
    #Draw my button

    #Define the center point
    xc, yc = center.getX(), center.getY()
    w, h = w//2, h//2

    #Creating rectangle for the button
    button = Rectangle(Point(xc - w, yc - h), Point(xc + w, yc + h))
    button.setFill('black')
    button.draw(win)

    #Creating label for the button
    label = Text(Point(xc, yc), text)
    label.setFill(color_rgb(154, 154, 154))
    label.draw(win)
    
    return button, label

#Function to check if button was clicked
def clicked(button, point):
    """Checks if button created from drawButton() was clicked

    Args:
        button : Button created from drawButton() function
        point (Point): Point at which mouse is clicked inside the button

    Returns:
        Boolean: Returns True if click is inside button, False if outside

    Example: clicked(myButton, Point(20,50))
    """
    #Getting coordinates from user to see if it is in the button
    xlo, ylo = button.getP1().getX(), button.getP1().getY()
    xhi, yhi = button.getP2().getX() , button.getP2().getY()
    
    x, y = point.getX(), point.getY()
    
    
    return (xlo < x < xhi) and (ylo < y < yhi)

def splashScreen(W, H):

    """Splashscreen function for WAR. Creates two buttons: Start or Quit.

    Args: W, H

    Returns:
    Starts program or Quits depending on which button user clicks.

    Example: 
    """


    win = GraphWin('Main Menu', W, H) #Creating window

    #Drawing background
    background = Image(Point(W//2, H//2), 'BLACKJACK.png')
    background.draw(win)

    #Drawing start button
    startButton = Button(Point(400, 200), win, 200, 50, 'Start Game!', 'gray')
    #Drawing quit button
    quitButton = Button(Point(400, 300), win, 200, 50, 'Quit', 'gray')
    #Drawing rules button
    rulesButton = Button(Point(400, 400), win, 200, 50, 'Rules', 'gray')    

    #Activating buttons so that they are able to be used
    startButton.activate()
    quitButton.activate()
    rulesButton.activate()

    #If statement for clicked start button
    while True:
        p = win.getMouse()
        #Start button on splashscreen
        if startButton.clicked(p):  #If start button is clicked, it will start game
            win2 = GraphWin('War!', 700, 800)
            win2.setBackground('green')
            window2char(win2)
            win.close()
            win2.getMouse()
            return win2 
        #Quit button on splashscreen
        elif quitButton.clicked(p): #If quit button is clicked, it will close the game
            win.close()
            return 'quit'
        #Rules button on splash screen, integrates quit button as well
        elif rulesButton.clicked(p): #If rules button is clicked, opens seperate window for rules
            win3 = GraphWin('War Rules!', W, H)
            rulesBackground = Image(Point(W//2, H//2), 'Blackjack Rules.png')
            rulesBackground.draw(win3)
            #Making rules button
            quitRules = Button(Point(400, 450), win3, 200, 50, 'Menu', 'gray')
            quitRules.activate()
            #If clicked rules button
            while True:
                qRules = win3.getMouse()
                if quitRules.clicked(qRules):
                    win3.close()
                    break

def window2char(win2):


    """Creates character images, names, and card backs for War program

    Args: win2

    Returns:
        Image/Text: character1Image, character2Image, character1Name, character2Name, cardBackchar1, cardBackchar2
    """

    #Creating character images for player 1 and 2
    character1Image = Image(Point(350,50), 'character1.png')
    character1Image.draw(win2)
    
    character2Image = Image(Point(350,750), 'character2.png')
    character2Image.draw(win2)

    #Drawing the player names to the screen
    character1Name = Text(Point(350, 15), 'Computer')
    character1Name.setSize(12)
    character1Name.draw(win2)

    character2Name = Text(Point(350, 785), 'You')
    character2Name.setSize(12)
    character2Name.draw(win2)

    #Drawing the fake card backs to the screen
    cardBackchar1 = Image(Point(350, 150), 'cardBack.png')
    cardBackchar1.draw(win2)

    cardBackchar2 = Image(Point(350, 650), 'cardBack.png')
    cardBackchar2.draw(win2)

    #Returning all of the variables so they can be used
    return character1Image, character2Image, character1Name, character2Name, cardBackchar1, cardBackchar2

def drawCard(win2):
    """" Creates two 'invisible' cards on top of fake card backs

    Args: win2

    Returns: player1card and player2card
    """
    #Creates an invisible card at the same location as card back to be flipped
    player1card = Rectangle(Point(314.5, 197), Point(385.5,103))
    player2card = Rectangle(Point(314.5, 697), Point(385.5, 603))
    
    #Returns player 1 and player 2 card so they can be used
    return player1card and player2card





def randomCard(win2):

    """Generates and draws two random cards for each player

    Returns:
        player1Number
        player1Suit
        player2Number
        player2Suit
        textNumberClone
        textNumber2Clone
    """
    from random import choice
    W, H = 71, 94
    
    #Creating a list for each number/king,queen,jack 
    mylistNumbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']

    #Creating a list for each suit
    mylistSuits = ['♠', '♥', '♦', '♣']

    #Choosing a random number and random suit for each player
    player1Number = choice(mylistNumbers)
    player1Suit = choice(mylistSuits)
    player2Number = choice(mylistNumbers)
    player2Suit = choice(mylistSuits)

    

    #Creating deck and appending player1/2 number and suit into to an empty list
    import random
    deck = []
    for number in mylistNumbers:
        for suit in mylistSuits:
            card = number + 'of' + suit
            deck.append(card)

    #Shuffles the whole deck
    random.shuffle(deck)

    #Assigns each players score to 0 
    player1Score = 0
    player2Score = 0

    #Prints player1/2 score to the screen 
    scoreText1 = Text(Point(150, 130), f"Computer Score: {player1Score}")
    scoreText1.setSize(20)
    scoreText1.setStyle('bold')
    scoreText1.draw(win2)

    scoreText2 = Text(Point(150, 630), f"Your Score: {player2Score}")
    scoreText2.setSize(20)
    scoreText2.setStyle('bold')
    scoreText2.draw(win2)

    
    #Now I need to split the deck in half so each player has 26 cards
    halfDeck = len(deck) // 2
    #Assigns half of the deck to each player using indexing
    player1Deck = deck[:halfDeck]
    player2Deck = deck[halfDeck:]

    #Calculates cards left based on the length of the players1/2 decks
    deckNumShow1 = Text(Point(525,130), f'Cards left: {(len(player1Deck))}')
    deckNumShow1.setSize(20)
    deckNumShow1.draw(win2)
    deckNumShow2 = Text(Point(525,630), f'Cards left: {(len(player2Deck))}')
    deckNumShow2.setSize(20)
    deckNumShow2.draw(win2)

    #Creating/activating button to draw cards
    drawButton = Button(Point(600, 400), win2, 100, 40, 'Draw Card!', 'gray')
    drawButton.activate()

    #Creating/activating button to quit the game while the game runs
    quitButton = Button(Point(600,750), win2, 100, 40, 'Quit','gray')
    quitButton.activate()

    #Function that updates the scores and cards left 
    def updateScoresnCards():
        """Update the displayed scores."""
        scoreText1.setText(f"Computer Score: {player1Score}")
        scoreText2.setText(f"Your Score: {player2Score}")
        deckNumShow1.setText(f'Cards left: {len(player1Deck)}')
        deckNumShow2.setText(f'Cards left: {len(player2Deck)}')
            
    #Main loop for the game logic
    while player1Deck and player2Deck:

        #Wait for Draw Card button click
        while True:
            p = win2.getMouse()
            if drawButton.clicked(p): #If draw button is clicked, break out of this loop and continue
                break
            if quitButton.clicked(p): #If quit button is clicked, close the game
                win2.close()
                break

    #Player 1
        #Pop selects a card from the deck
        player1Card = player1Deck.pop(0)
        player1Number, player1Suit = player1Card.split('of')

    #Player 2
        player2Card = player2Deck.pop(0)
        player2Number, player2Suit = player2Card.split('of')

        #Creates actual card on screen
        player1card = Rectangle(Point(314.5, 197), Point(385.5,103))
        player2card = Rectangle(Point(314.5, 697), Point(385.5, 603))

        #Getting card dimensions
        player1card.setFill('white')
        player1card.setOutline('black')
        player1card.draw(win2)

        player2card.setFill('white')
        player2card.setOutline('black')
        player2card.draw(win2)
        #Getting center point of cards
        centerCard1 = player1card.getCenter()
        centerCard2 = player2card.getCenter()

        #Getting x and y coordinates of center
        centerX = centerCard1.getX()
        centerY = centerCard1.getY()

        centerX2 = centerCard2.getX()
        centerY2 = centerCard2.getY()

        #Drawing suit to center
        textSuit1 = Text(centerCard1, player1Suit)
        textSuit1.setSize(20)
        textSuit1.draw(win2)

        textSuit2 = Text(centerCard2, player2Suit)
        textSuit2.setSize(20)
        textSuit2.draw(win2)

        textNumber = Text(Point(centerX-25.5,centerY-60), player1Number)
        textNumber.setSize(17)
        textNumber.draw(win2)

        textNumber2 = Text(Point(centerX2-25.5, centerY2+40), player2Number)
        textNumber2.setSize(17)
        textNumber2.draw(win2)
        
        #Moving card to give the illusion that the card is being drawn from the deck
        player1card.move(0,125)
        player2card.move(0,-125)

        textSuit1.move(0,125)
        textSuit2.move(0,-125)

        textNumber.move(0,150)
        textNumber2.move(0, -200)

        textNumberClone = textNumber.clone()
        textNumberClone.move(53, 71)
        textNumberClone.draw(win2)

        textNumber2Clone = textNumber2.clone()
        textNumber2Clone.move(53, 71)
        textNumber2Clone.draw(win2)


        #Creating a dictionary to keep track of number values of each card.
        #Jacks - 11, Queen - 12, King - 13, Ace - 14

        cardValues = {
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            '10':10,
            'J':11,
            'Q':12,
            'K':13,
            'A':14
        }
        #Looks up value of card in dictionary and assigns variable to it 
        player1Value = cardValues[player1Number]
        player2Value = cardValues[player2Number]

        #Time to create the logic to start the game!
        if player1Value > player2Value:  #Compares player1/2 value to determine winner of round
            time.sleep(1)
            winRound1 = Text(Point(700//2, 800//2), 'Computer wins the round!')
            winRound1.setSize(20)
            winRound1.draw(win2)
            time.sleep(3)
            winRound1.undraw()
            player1Score += 2   #Updates player score so that whoever wins gets both cards added to score

        elif player1Value < player2Value:  #Compares player1/2 value to determine winner of round
            time.sleep(1)
            winRound2 = Text(Point(700//2, 800//2), 'You win the round!')
            winRound2.setSize(20)
            winRound2.draw(win2)
            player2Score += 2 
            time.sleep(3)
            winRound2.undraw()
            

        elif player1Value == player2Value: #Checks for tie, doesn't award any points for a tie
            time.sleep(1)
            warTie = Text(Point(700//2, 800//2), 'Its a tie!')
            warTie.setSize(20)
            warTie.draw(win2)
            time.sleep(3)
            warTie.undraw()

        updateScoresnCards()  #Calls to function to update scores and card values        

    #Logic to determine winner
    if player1Score > player2Score: #Compares final player1/2 scores to determine winner of the game
        endGame = Text(Point(700//2, 800//2), 'Computer wins game!')
        endGame.setSize(25)
        endGame.draw(win2)
        time.sleep(3)
        endGame.undraw()
        

    elif player2Score > player1Score: #Compares final player1/2 scores to determien winner of the game
        endGame = Text(Point(700//2, 800//2), 'You win the game!')
        endGame.setSize(25)
        endGame.draw(win2) 
        time.sleep(3)
        endGame.undraw()
        

    else: #Determines if game is a tie
        endGame = Text(Point(700//2, 800//2), 'The game is a tie!')
        endGame.setSize(25)
        endGame.draw(win2)   
        time.sleep(3)
        endGame.undraw()   
    #Returns player1/2 number and suits
    return (player1Number, player1Suit, player2Number, player2Suit)



class Button:
    """Class that is a remake of drawButton function, no label required
    """
    def __init__(self, center, win, w, h, text, color):
        """Creates a button

        Args:
            center (point): 
            win: _description_
            w (int): _description_
            h (int): _description_
            text (string): _description_
            color (color): _description_
        """
        self.center = center.clone()
        self.win = win
        self.text = text
        self.color = color
        self.active = False


        #Define the center point
        xc, yc = center.getX(), center.getY()
        w, h = w//2, h//2

        rect = self.rect = Rectangle(Point(xc - w, yc - h), Point(xc + w, yc + h))
        rect.setFill(color)
        rect.draw(win)

        label = self.label = Text(Point(xc, yc), text)
        label.setFill(color_rgb(154, 154, 154))
        label.draw(win)

        self.deactivate()
        
        self.width, self.height = w, h
    
    def clicked(self, p):
        """Determines if Button was clicked from Button class

        Args:
            p (Point): Point where user clicked

        Returns:
            Boolean: True if Button is clicked, False if button isn't clicked
        """
        rect = self.rect
        xlo, ylo = rect.getP1().getX(), rect.getP1().getY()
        xhi, yhi = rect.getP2().getX() , rect.getP2().getY()
    
        x, y = p.getX(), p.getY()
    
    
        return (xlo < x < xhi) and (ylo < y < yhi) and self.active
    
    def activate(self):
        """Activates button, which it allows it to be clicked.
        """
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """Deactivates button, which doesn't allow it to be clicked.
        """
        self.label.setFill('lightgray')
        self.rect.setWidth(1)
        self.active = False
    