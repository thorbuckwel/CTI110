# A BattleShip Game, There are bugs to work out but it still works
# William Buckwell
# 4/30/18

import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

####### TO DO ########
# If a pship is destroyed it does not turn last button red
# pShips is throwing an error if it crosses another pShip
# Check ship spacing during placement
# Refactor if there is time
######################

# Following varaibles hold how many times ships were hit
carrierHit = 0
battleShipHit = 0
cruiserHit = 0
submarineHit = 0
destroyerHit = 0

# Following list varaibles hold the ships location
shipLocation = []
usedLocations = []
carrier = []
battleShip = []
cruiser = []
submarine = []
destroyer = []

# Following list varaibles hold the player's ships location
pShipLocation = []
pusedLocations = []
pCarrier = ['']
pBattleShip = ['']
pCruiser = ['']
pSubmarine = ['']
pDestroyer = ['']
shipScreenButtons = {}

# Following varaibles hold how many times player ships were hit
pCarrierHit = 0
pBattleShipHit = 0
pCruiserHit = 0
pSubmarineHit = 0
pDestroyerHit = 0


# Following varaible are how big the ship is.
carrierSlot = 5
battleShipSlot = 4
cruiserSlot = 3
submarineSlot = 3
destroyerSlot = 2

# List to hold computer shot history
shotHistory = []

# For players selected direction
selectedDirection = ''

# Level ######Future use######
level = 0

# To determine turn, Odd is player, Even Computer
turn = 0

# Build the TK canvas for the battle field. It also assigns the computers
# ships to random locations
def BattleGrid(self):

          # Assign all ships their locations
          assignShips(carrierSlot)
          assignShips(battleShipSlot)
          assignShips(cruiserSlot)
          assignShips(submarineSlot)
          assignShips(destroyerSlot)
          
          # List needed to assign labels
          letterLabels = ['A','B','C','D','E','F','G','H','I','J']

          # Set the GUI background, rows, and columns
          fm = tk.Frame(root, background="blue")
          fm.rowconfigure( 0, weight=1 )
          fm.columnconfigure( 1, weight=1 )
          fm.grid( row=0, column=0, sticky='nsew' )

          # Put numbered labels in left column
          for row in range(1,11):
               numberLabel = tk.Label(fm, background = "blue", text= row, fg="black")
               numberLabel.grid(row= row, column=0, padx=5, pady=5)

          # Put Letter labels in top row
          for letter in range(0,10):
               letterLabel = tk.Label(fm, background = "blue", text= letterLabels[letter], fg="black")
               letterLabel.grid(row= 0, column= letter+1, padx=5, pady=5)

          
          # Build the Buttons
          builtButtons(fm)

          # Pack up the Frame
          fm.pack()
          
# Builds the Players canvas so they can place their ships. It auto hides the
# direction canvases until they are called
def PlayerGrid(self):

    root.withdraw()
    win3.withdraw()
    win4.withdraw()
    win5.withdraw()
    win6.withdraw()
    win7.withdraw()

    letterLabels = ['A','B','C','D','E','F','G','H','I','J']

    fm2 = tk.Frame(win2, background="blue")
    fm2.rowconfigure( 0, weight=1 )
    fm2.columnconfigure( 1, weight=1 )
    fm2.grid( row=0, column=0, sticky='nsew' )

    # Put numbered labels in left column
    for row in range(1,11):
       numberLabel = tk.Label(fm2, background = "blue", text= row, fg="black")
       numberLabel.grid(row= row, column=0, padx=5, pady=5)

    # Put Letter labels in top row
    for letter in range(0,10):
       letterLabel = tk.Label(fm2, background = "blue", text= letterLabels[letter], fg="black")
       letterLabel.grid(row= 0, column= letter+1, padx=5, pady=5)

    # Build the Buttons
    builtButtons2(fm2)

    fm2.pack()    

    messagebox.showinfo("Place Ship", "Now place your Carrier")

# Since we need to have a diffrent canvas for each direction selection
# this Function determines which Function needs to be called to activate
# the correct canvas
def placePlayerShips(row,column, name):
    
    if len(pCarrier) < 5:
        playerAddCarrier(5,row,column)
    elif len(pBattleShip) < 4:        
        playerAddBattleShip(4,row,column)
    elif len(pCruiser) < 3:
        playerAddCruiser(3,row,column)
    elif len(pSubmarine) < 3:
        playerAddSubmarine(3,row,column)
    elif len(pDestroyer) < 2:
        playerAddDestroyer(2,row,column)

    # After all ships have been assigned display the BattleGrid
    if len(pCarrier) == 5 and len(pBattleShip) == 4 and len(pCruiser) == 3 and len(pSubmarine) == 3 and len(pDestroyer) == 2 :
            root.deiconify()    

# This builds the direction selection canvas for the Carrier placement
def playerAddCarrier(ship, row, col):

    win3.deiconify()
    # 0 Up, 1 Down, 2 left, 3 Right
    direction = [0,1,2,3]

    # Remove direction from list if ship does not fit
    if row < ship:
      direction.remove(0)
    if (ship - row) < -1:
      direction.remove(1)
    if col < ship:
      direction.remove(2)
    if (ship - col) < -1:
      direction.remove(3)    
    
    choice = tk.Frame(win3, background="blue")
    choice.rowconfigure( 0, weight=1 )
    choice.columnconfigure( 1, weight=1 )
    choice.grid( row=0, column=0, sticky='nsew' )

    choice.pack()

    # Build the buttons for the canvas
    for items in direction:
        if items == 0:            
            button201 = (tk.Button(choice,text = 'Up', background = "grey", state='normal', 
                   command= lambda name = 'button201': onClick(0, choice, ship, row, col)))
            button201.grid(row = 1, padx=5, pady=5)
            
    for items in direction:
        if items == 1:            
            button202 = (tk.Button(choice,text = 'Down', background = "grey", state='normal', 
                   command= lambda name = 'button202': onClick(1, choice, ship, row, col)))
            button202.grid(row = 2, padx=5, pady=5)
    for items in direction:
        if items == 2:            
            button203 = (tk.Button(choice,text = 'Left', background = "grey", state='normal', 
                   command= lambda name = 'button203': onClick(2, choice, ship, row, col)))
            button203.grid(row = 3, padx=5, pady=5)
    for items in direction:
        if items == 3:            
            button204 = (tk.Button(choice,text = 'Right', background = "grey", state='normal', 
                   command= lambda name = 'button204': onClick(3, choice, ship, row, col)))
            button204.grid(row = 4, padx=5, pady=5)

# This builds the direction selection canvas for the BattleShip placement
def playerAddBattleShip(ship, row, col):

    win4.deiconify()
    
    # 0 Up, 1 Down, 2 left, 3 Right
    direction = [0,1,2,3]

    # Remove direction from list if ship does not fit
    if row < ship:
      direction.remove(0)
    if (ship - row) < -3:
      direction.remove(1)
    if col < ship:
      direction.remove(2)
    if (ship - col) < -1:
      direction.remove(3)    
    
    choice1 = tk.Frame(win4, background="blue")
    choice1.rowconfigure( 0, weight=1 )
    choice1.columnconfigure( 1, weight=1 )
    choice1.grid( row=0, column=0, sticky='nsew' )

    choice1.pack()

    # Build the buttons for the canvas
    for items in direction:
        if items == 0:            
            button201 = (tk.Button(choice1,text = 'Up', background = "grey", state='normal', 
                   command= lambda name = 'button201': onClick(0, choice1, ship, row, col)))
            button201.grid(row = 1, padx=5, pady=5)
            
    for items in direction:
        if items == 1:            
            button202 = (tk.Button(choice1,text = 'Down', background = "grey", state='normal', 
                   command= lambda name = 'button202': onClick(1, choice1, ship, row, col)))
            button202.grid(row = 2, padx=5, pady=5)
    for items in direction:
        if items == 2:            
            button203 = (tk.Button(choice1,text = 'Left', background = "grey", state='normal', 
                   command= lambda name = 'button203': onClick(2, choice1, ship, row, col)))
            button203.grid(row = 3, padx=5, pady=5)
    for items in direction:
        if items == 3:            
            button204 = (tk.Button(choice1,text = 'Right', background = "grey", state='normal', 
                   command= lambda name = 'button204': onClick(3, choice1, ship, row, col)))
            button204.grid(row = 4, padx=5, pady=5)

# This builds the direction selection canvas for the Cruiser placement            
def playerAddCruiser(ship, row, col):

    win5.deiconify()
    
    # 0 Up, 1 Down, 2 left, 3 Right
    direction = [0,1,2,3]

    # Remove direction from list if ship does not fit
    if row < ship:
      direction.remove(0)
    if (ship - row) < -5:
      direction.remove(1)
    if col < ship:
      direction.remove(2)
    if (ship - col) < -1:
      direction.remove(3)    
    
    choice2 = tk.Frame(win5, background="blue")
    choice2.rowconfigure( 0, weight=1 )
    choice2.columnconfigure( 1, weight=1 )
    choice2.grid( row=0, column=0, sticky='nsew' )

    choice2.pack()

    # Build the buttons for the canvas
    for items in direction:
        if items == 0:            
            button205 = (tk.Button(choice2,text = 'Up', background = "grey", state='normal', 
                   command= lambda name = 'button201': onClick(0, choice2, ship, row, col)))
            button205.grid(row = 1, padx=5, pady=5)
            
    for items in direction:
        if items == 1:            
            button206 = (tk.Button(choice2,text = 'Down', background = "grey", state='normal', 
                   command= lambda name = 'button202': onClick(1, choice2, ship, row, col)))
            button206.grid(row = 2, padx=5, pady=5)
    for items in direction:
        if items == 2:            
            button207 = (tk.Button(choice2,text = 'Left', background = "grey", state='normal', 
                   command= lambda name = 'button203': onClick(2, choice2, ship, row, col)))
            button207.grid(row = 3, padx=5, pady=5)
    for items in direction:
        if items == 3:            
            button208 = (tk.Button(choice2,text = 'Right', background = "grey", state='normal', 
                   command= lambda name = 'button204': onClick(3, choice2, ship, row, col)))
            button208.grid(row = 4, padx=5, pady=5)

# This builds the direction selection canvas for the Submarine placement
def playerAddSubmarine(ship, row, col):

    win6.deiconify()
    
    # 0 Up, 1 Down, 2 left, 3 Right
    direction = [0,1,2,3]

    # Remove direction from list if ship does not fit
    if row < ship:
      direction.remove(0)
    if (ship - row) < -5:
      direction.remove(1)
    if col < ship:
      direction.remove(2)
    if (ship - col) < -1:
      direction.remove(3)    
    
    choice3 = tk.Frame(win6, background="blue")
    choice3.rowconfigure( 0, weight=1 )
    choice3.columnconfigure( 1, weight=1 )
    choice3.grid( row=0, column=0, sticky='nsew' )

    choice3.pack()

    # Build the buttons for the canvas
    for items in direction:
        if items == 0:            
            button209 = (tk.Button(choice3,text = 'Up', background = "grey", state='normal', 
                   command= lambda name = 'button201': onClick(0, choice3, ship, row, col)))
            button209.grid(row = 1, padx=5, pady=5)
            
    for items in direction:
        if items == 1:            
            button210 = (tk.Button(choice3,text = 'Down', background = "grey", state='normal', 
                   command= lambda name = 'button202': onClick(1, choice3, ship, row, col)))
            button210.grid(row = 2, padx=5, pady=5)
    for items in direction:
        if items == 2:            
            button211 = (tk.Button(choice3,text = 'Left', background = "grey", state='normal', 
                   command= lambda name = 'button203': onClick(2, choice3, ship, row, col)))
            button211.grid(row = 3, padx=5, pady=5)
    for items in direction:
        if items == 3:            
            button212 = (tk.Button(choice3,text = 'Right', background = "grey", state='normal', 
                   command= lambda name = 'button204': onClick(3, choice3, ship, row, col)))
            button212.grid(row = 4, padx=5, pady=5)

# This builds the direction selection canvas for the Destroyer placement
def playerAddDestroyer(ship, row, col):

    win7.deiconify()
    
    # 0 Up, 1 Down, 2 left, 3 Right
    direction = [0,1,2,3]

    # Remove direction from list if ship does not fit
    if row < ship:
      direction.remove(0)
    if (ship - row) < -7:
      direction.remove(1)
    if col < ship:
      direction.remove(2)
    if (ship - col) < -1:
      direction.remove(3)    
    
    choice4 = tk.Frame(win7, background="blue")
    choice4.rowconfigure( 0, weight=1 )
    choice4.columnconfigure( 1, weight=1 )
    choice4.grid( row=0, column=0, sticky='nsew' )

    choice4.pack()

    # Build the buttons for the canvas
    for items in direction:
        if items == 0:            
            button213 = (tk.Button(choice4,text = 'Up', background = "grey", state='normal', 
                   command= lambda name = 'button201': onClick(0, choice4, ship, row, col)))
            button213.grid(row = 1, padx=5, pady=5)
            
    for items in direction:
        if items == 1:            
            button214 = (tk.Button(choice4,text = 'Down', background = "grey", state='normal', 
                   command= lambda name = 'button202': onClick(1, choice4, ship, row, col)))
            button214.grid(row = 2, padx=5, pady=5)
    for items in direction:
        if items == 2:            
            button215 = (tk.Button(choice4,text = 'Left', background = "grey", state='normal', 
                   command= lambda name = 'button203': onClick(2, choice4, ship, row, col)))
            button215.grid(row = 3, padx=5, pady=5)
    for items in direction:
        if items == 3:            
            button216 = (tk.Button(choice4,text = 'Right', background = "grey", state='normal', 
                   command= lambda name = 'button204': onClick(3, choice4, ship, row, col)))
            button216.grid(row = 4, padx=5, pady=5)
            
# This is a Function for the buttons it assigns a number to selectedDirection
# then passes it with the other peramters to assignPShip
def onClick(num, choice, ship, row, col):
    global selectedDirection
    selectedDirection = num
    
    assignPShips(selectedDirection, ship, row, col)

def assignPShips(shipDirection, ship, row, col):   
   cross = 'n'
   shipLocation = []

   # Add string postion to the ship's location 
   shipLocation.append(joinNumbers(row,col))     

   # Create and assign rest of the ships location depending on which
   # direction was picked
   if shipDirection == 0:
      for num in range(ship -1):
         row -= 1
         shipLocation.append(joinNumbers(row,col))
   if shipDirection == 1:
      for num in range(ship -1):
         row += 1
         shipLocation.append(joinNumbers(row,col))
   if shipDirection == 2:
      for num in range(ship -1):
         col -= 1
         shipLocation.append(joinNumbers(row,col))
   if shipDirection == 3:
      for num in range(ship -1):
         col += 1
         shipLocation.append(joinNumbers(row,col))

   #### This needs to be reworked, does not work properly ####
   if ship < 5:
       for i in range(len(shipLocation)):
           if shipLocation[i] in pusedLocations:
               shipLocation = []
               print('This ship will cross another ship')
               cross = 'y'

   #### Needs rework goes with above code ####
   if cross == 'n':
       addPLocation(shipLocation, ship)

# This fuction assign the locations in the shipLocation to the proper ship List
# depending on the ships size then assign to usedLocations.
def addPLocation(shipLocation, ship):       

    if ship == 5:
        for i in range(len(shipLocation)):
            pCarrier.append(shipLocation[i])
            pusedLocations.append(shipLocation[i])
    elif ship == 4:
        for i in range(len(shipLocation)):
            pBattleShip.append(shipLocation[i])
            pusedLocations.append(shipLocation[i])
    elif ship == 3:
        if len(pCruiser) < 3:
            for i in range(len(shipLocation)):
                pCruiser.append(shipLocation[i])
                pusedLocations.append(shipLocation[i])
        else:
            for i in range(len(shipLocation)):
                pSubmarine.append(shipLocation[i])
                pusedLocations.append(shipLocation[i])
    else:
        for i in range(len(shipLocation)):
            pDestroyer.append(shipLocation[i])
            pusedLocations.append(shipLocation[i])

    # Then depending on ship size find the button in the button Dictonary and
    # set that button to grey and disable the click option
    if ship == 5:        
        for key, value in shipScreenButtons.items():
            for loc in pCarrier:
                if value == loc:
                    key['background'] = 'grey'
                    key['state'] = 'disabled'
    if ship == 4:        
        for key, value in shipScreenButtons.items():
            for loc in pBattleShip:
                if value == loc:
                    key['background'] = 'grey'
                    key['state'] = 'disabled'
                    
    if ship == 3 and len(pCruiser) > 2:        
        for key, value in shipScreenButtons.items():
            for loc in pCruiser:
                if value == loc:
                    key['background'] = 'grey'
                    key['state'] = 'disabled'
    if ship == 3 and len(pSubmarine) > 2:        
        for key, value in shipScreenButtons.items():
            for loc in pSubmarine:
                if value == loc:
                    key['background'] = 'grey'
                    key['state'] = 'disabled'

    if ship == 2:        
        for key, value in shipScreenButtons.items():
            for loc in pDestroyer:
                if value == loc:
                    key['background'] = 'grey'
                    key['state'] = 'disabled'

    # Do to coding there is a blank in the list to begin with so it needs to be
    # removed so the length will be correct.
    if len(pCarrier) > 5:
        pCarrier.remove('')

    if len(pBattleShip) > 4:
        pBattleShip.remove('')

    if len(pCruiser) > 3:
        pCruiser.remove('')

    if len(pSubmarine) > 3:
        pSubmarine.remove('')

    if len(pDestroyer) > 2:
        pDestroyer.remove('')

    # Withdraw direction canvas then inform the player what ship needs to be placed next. 
    if ship == 5:
        win3.withdraw()
        messagebox.showinfo("Place Ship", "Now place your BattleShip")
    elif ship == 4:
        win4.withdraw()
        messagebox.showinfo("Place Ship", "Now place your Cruiser")
    elif ship == 3 and len(pSubmarine) < 3:
        win5.withdraw()
        messagebox.showinfo("Place Ship", "Now place your Submarine")
    elif ship == 3 and len(pDestroyer) < 2:
        win6.withdraw()
        messagebox.showinfo("Place Ship", "Now place your Destroyer")
    else:
        win7.destroy()
        root.deiconify()
    

# Determine a starting postion, Which way the ship fits, then what direction
# to place the ship.
def assignShips(ship):
   shipLocation = []

   # 0 Up, 1 Down, 2 left, 3 Right
   direction = [0,1,2,3]

   # Dtermine random staring postion
   row = random.randint(1,10)
   col = random.randint(1,10)

   # Add string postion to the ship's location
   shipLocation.append(joinNumbers(row,col))

   # Remove direction from list if ship does not fit
   if row < ship:
      direction.remove(0)
   if (ship - row) < -1:
      direction.remove(1)
   if col < ship:
      direction.remove(2)
   if (ship - col) < -1:
      direction.remove(3)

   # Get a random direction from what is left in the Direction List 
   shipDirection = random.choice(direction)

   # Create and assign rest of the ships location depending on which
   # direction was picked
   if shipDirection == 0:
      for num in range(ship -1):
         row -= 1
         shipLocation.append(joinNumbers(row,col))
   if shipDirection == 1:
      for num in range(ship -1):
         row += 1
         shipLocation.append(joinNumbers(row,col))
   if shipDirection == 2:
      for num in range(ship -1):
         col -= 1
         shipLocation.append(joinNumbers(row,col))
   if shipDirection == 3:
      for num in range(ship -1):
         col += 1
         shipLocation.append(joinNumbers(row,col))

   addLocation(shipLocation, ship)

# With the direction and starting postion fill in the ship locations
def addLocation(shipLocation, ship):

   ##### This needs to be reworked ####
   if len(usedLocations) < 1:
      for i in range(len(shipLocation)):
         usedLocations.append(shipLocation[i])

   # If the ship size is less then 5 then it needs to check if its placement
   # will cross another ship.
   if ship < 5:
      ### Also needs rework this causes an error ###
      for i in range(len(shipLocation)):
         if shipLocation[i] in usedLocations:
            shipLocation = []
            assignShips(ship)
            break
         else:
            usedLocations.append(shipLocation[i])      

   # Depending on the ship size assign location to the correct List
   if ship == 5:
      for i in range(len(shipLocation)):
         carrier.append(shipLocation[i])      
   elif ship == 4:
      for i in range(len(shipLocation)):
         battleShip.append(shipLocation[i])
   elif ship == 3:
      if len(cruiser) < 1:
         for i in range(len(shipLocation)):
            cruiser.append(shipLocation[i])        
      else:
         for i in range(len(shipLocation)):
            submarine.append(shipLocation[i])         
   else:
      for i in range(len(shipLocation)):
         destroyer.append(shipLocation[i])

# Function to change The button color, make it only 1 time clickable
# Also shows a message when a ship is sunk.
def checkHit(button,row,column, name):
   
   location = joinNumbers(row,column)
   
   # Turn button red or white and if reach shipHit limit display the message
   # Also make the buttons diabled to prevent further clicking
   if location in carrier:
      button['background']= "red"
      button['state'] = 'disabled'
      global carrierHit
      carrierHit += 1
      if carrierHit == 5:
         messagebox.showinfo("Destroyed", "You sank my Carrier!")
         checkWin()
   elif location in battleShip:
      button['background']= "red"
      button['state'] = 'disabled'
      global battleShipHit
      battleShipHit += 1
      if battleShipHit == 4:
         messagebox.showinfo("Destroyed", "You sank my BattleShip!")
         checkWin()
   elif location in cruiser:
      button['background']= "red"
      button['state'] = 'disabled'
      global cruiserHit
      cruiserHit += 1
      if cruiserHit == 3:
         messagebox.showinfo("Destroyed", "You sank my Cruiser!")
         checkWin()
   elif location in submarine:
      button['background']= "red"
      button['state'] = 'disabled'
      global submarineHit
      submarineHit += 1
      if submarineHit == 3:
         messagebox.showinfo("Destroyed", "You sank my Submarine!")
         checkWin()
   elif location in destroyer:
      button['background']= "red"
      button['state'] = 'disabled'
      global destroyerHit
      destroyerHit += 1
      if destroyerHit == 2:
         messagebox.showinfo("Destroyed", "You sank my Destroyer!")
         checkWin()
   else:
      button['background']= "blue"
      button['state'] = 'disabled'

   # Computer's turn      
   computerTurn()

# After each shot check to see if someone has won. Display if the player has
# won or lost if the condtions have been meet.
def checkWin():
    
    if carrierHit == 5 and battleShipHit == 4 and cruiserHit == 3 and submarineHit == 3 and destroyerHit == 2:
        messagebox.showinfo("Win", "YOU WIN!!!!!!!")

    if pCarrierHit == 5 and pBattleShipHit == 4 and pCruiserHit == 3 and pSubmarineHit == 3 and pDestroyerHit == 2:
            messagebox.showinfo("Lose", "YOU LOSE!!!!!!!")

# After the player the computer gets a turn this Function will get a random
# number for the row and column and determine if one of the ships are sitting
# in that location. It then turns the button red if there is a ship or it turns
# it white if there is not
def computerTurn():
    
    row = random.randint(1, 10)
    col = random.randint(1, 10)

    shotLocation = joinNumbers(row, col)
    
    global shotHistory
    if shotLocation not in shotHistory:
        shotHistory.append(shotLocation)
        
        if shotLocation in pCarrier:
            global pCarrierHit
            pCarrierHit += 1
            for key, value in shipScreenButtons.items():           
                if value == shotLocation:
                    key['background'] = 'red'
            if pCarrierHit == 5:
                messagebox.showinfo("Destroyed", "I sank your Carrier!")
                checkWin()
        elif shotLocation in pBattleShip:
            global pBattleShipHit
            pBattleShipHit += 1
            for key, value in shipScreenButtons.items():           
                if value == shotLocation:
                    key['background'] = 'red'        
            if pBattleShipHit == 4:
                messagebox.showinfo("Destroyed", "I sank your BattleShip!")
                checkWin()
        elif shotLocation in pCruiser:
            global pCruiserHit
            pCruiserHit += 1
            for key, value in shipScreenButtons.items():           
                if value == shotLocation:
                    key['background'] = 'red'
            if pCruiserHit == 3:
                messagebox.showinfo("Destroyed", "I sank your Cruiser!")
                checkWin()
        elif shotLocation in pSubmarine:
            global pSubmarineHit
            pSubmarineHit += 1
            for key, value in shipScreenButtons.items():           
                if value == shotLocation:
                    key['background'] = 'red'
            if pSubmarineHit == 3:
                messagebox.showinfo("Destroyed", "I sank your Submarine!")
                checkWin()
        elif shotLocation in pDestroyer:
            global pDestroyerHit
            pDestroyerHit += 1
            for key, value in shipScreenButtons.items():           
                if value == shotLocation:
                    key['background'] = 'red'
            if pDestroyerHit == 2:
                messagebox.showinfo("Destroyed", "I sank your Destroyer!")
                checkWin()
        else:
            for key, value in shipScreenButtons.items():           
                if value == shotLocation:
                    key['background'] = 'white'  
    else:
        computerTurn()

# Turn numbers into a string
def joinNumbers(row,col):
   location = [str(row),str(col)]
   location = ''.join(location)

   return location

# Create the Buttons (100 total)
def builtButtons(fm):
   # Row 1 Buttons
          button1 = (tk.Button(fm, background = "grey", text= ' ', state='normal', 
                   command= lambda name = 'button1': checkHit(button1,1,1, name)))
          button1.grid(row= 1, column= 1, padx=5, pady=5)       
          button2 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button2': checkHit(button2,1,2, name)))
          button2.grid(row= 1, column= 2, padx=5, pady=5)
          button3 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button3': checkHit(button3,1,3, name)))
          button3.grid(row= 1, column= 3, padx=5, pady=5)       
          button4 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button4': checkHit(button4,1,4, name)))
          button4.grid(row= 1, column= 4, padx=5, pady=5)
          button5 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button5': checkHit(button5,1,5, name)))
          button5.grid(row= 1, column= 5, padx=5, pady=5)       
          button6 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button6': checkHit(button6,1,6, name)))
          button6.grid(row= 1, column= 6, padx=5, pady=5)
          button7 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button7': checkHit(button7,1,7, name)))
          button7.grid(row= 1, column= 7, padx=5, pady=5)       
          button8 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button8': checkHit(button8,1,8, name)))
          button8.grid(row= 1, column= 8, padx=5, pady=5)
          button9 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button9': checkHit(button9,1,9, name)))
          button9.grid(row= 1, column= 9, padx=5, pady=5)       
          button10 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button10': checkHit(button10,1,10, name)))
          button10.grid(row= 1, column= 10, padx=5, pady=5)

          # Row 2 Buttons
          button11 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button11': checkHit(button11,2,1, name)))
          button11.grid(row= 2, column= 1, padx=5, pady=5)       
          button12 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button12': checkHit(button12,2,2, name)))
          button12.grid(row= 2, column= 2, padx=5, pady=5)
          button13 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button13': checkHit(button13,2,3, name)))
          button13.grid(row= 2, column= 3, padx=5, pady=5)       
          button14 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button14': checkHit(button14,2,4, name)))
          button14.grid(row= 2, column= 4, padx=5, pady=5)
          button15 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button15': checkHit(button15,2,5, name)))
          button15.grid(row= 2, column= 5, padx=5, pady=5)       
          button16 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button16': checkHit(button16,2,6, name)))
          button16.grid(row= 2, column= 6, padx=5, pady=5)
          button17 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button17': checkHit(button17,2,7, name)))
          button17.grid(row= 2, column= 7, padx=5, pady=5)       
          button18 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button18': checkHit(button18,2,8, name)))
          button18.grid(row= 2, column= 8, padx=5, pady=5)
          button19 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button19': checkHit(button19,2,9, name)))
          button19.grid(row= 2, column= 9, padx=5, pady=5)       
          button20 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button20': checkHit(button20,2,10, name)))
          button20.grid(row= 2, column= 10, padx=5, pady=5)

          # Row 3 Buttons
          button21 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button21': checkHit(button21,3,1, name)))
          button21.grid(row= 3, column= 1, padx=5, pady=5)       
          button22 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button22': checkHit(button22,3,2, name)))
          button22.grid(row= 3, column= 2, padx=5, pady=5)
          button23 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button23': checkHit(button23,3,3, name)))
          button23.grid(row= 3, column= 3, padx=5, pady=5)       
          button24 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button24': checkHit(button24,3,4, name)))
          button24.grid(row= 3, column= 4, padx=5, pady=5)
          button25 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button25': checkHit(button25,3,5, name)))
          button25.grid(row= 3, column= 5, padx=5, pady=5)       
          button26 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button26': checkHit(button26,3,6, name)))
          button26.grid(row= 3, column= 6, padx=5, pady=5)
          button27 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button27': checkHit(button27,3,7, name)))
          button27.grid(row= 3, column= 7, padx=5, pady=5)       
          button28 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button28': checkHit(button28,3,8, name)))
          button28.grid(row= 3, column= 8, padx=5, pady=5)
          button29 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button29': checkHit(button29,3,9, name)))
          button29.grid(row= 3, column= 9, padx=5, pady=5)       
          button30 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button30': checkHit(button30,3,10, name)))
          button30.grid(row= 3, column= 10, padx=5, pady=5)

          # Row 4 Buttons
          button31 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button31': checkHit(button31,4,1, name)))
          button31.grid(row= 4, column= 1, padx=5, pady=5)       
          button32 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button32': checkHit(button32,4,2, name)))
          button32.grid(row= 4, column= 2, padx=5, pady=5)
          button33 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button33': checkHit(button33,4,3, name)))
          button33.grid(row= 4, column= 3, padx=5, pady=5)       
          button34 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button34': checkHit(button34,4,4, name)))
          button34.grid(row= 4, column= 4, padx=5, pady=5)
          button35 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button35': checkHit(button35,4,5, name)))
          button35.grid(row= 4, column= 5, padx=5, pady=5)       
          button36 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button36': checkHit(button36,4,6, name)))
          button36.grid(row= 4, column= 6, padx=5, pady=5)
          button37 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button37': checkHit(button37,4,7, name)))
          button37.grid(row= 4, column= 7, padx=5, pady=5)       
          button38 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button38': checkHit(button38,4,8, name)))
          button38.grid(row= 4, column= 8, padx=5, pady=5)
          button39 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button39': checkHit(button39,4,9, name)))
          button39.grid(row= 4, column= 9, padx=5, pady=5)       
          button40 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button40': checkHit(button40,4,10, name)))
          button40.grid(row= 4, column= 10, padx=5, pady=5)

          # Row 5 Buttons
          button41 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button41': checkHit(button41,5,1, name)))
          button41.grid(row= 5, column= 1, padx=5, pady=5)       
          button42 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button42': checkHit(button42,5,2, name)))
          button42.grid(row= 5, column= 2, padx=5, pady=5)
          button43 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button43': checkHit(button43,5,3, name)))
          button43.grid(row= 5, column= 3, padx=5, pady=5)       
          button44 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button44': checkHit(button44,5,4, name)))
          button44.grid(row= 5, column= 4, padx=5, pady=5)
          button45 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button45': checkHit(button45,5,5, name)))
          button45.grid(row= 5, column= 5, padx=5, pady=5)       
          button46 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button46': checkHit(button46,5,6, name)))
          button46.grid(row= 5, column= 6, padx=5, pady=5)
          button47 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button47': checkHit(button47,5,7, name)))
          button47.grid(row= 5, column= 7, padx=5, pady=5)       
          button48 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button48': checkHit(button48,5,8, name)))
          button48.grid(row= 5, column= 8, padx=5, pady=5)
          button49 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button49': checkHit(button49,5,9, name)))
          button49.grid(row= 5, column= 9, padx=5, pady=5)       
          button50 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button50': checkHit(button50,5,10, name)))
          button50.grid(row= 5, column= 10, padx=5, pady=5)

          # Row 6 Buttons
          button51 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button51': checkHit(button51,6,1, name)))
          button51.grid(row= 6, column= 1, padx=5, pady=5)       
          button52 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button52': checkHit(button52,6,2, name)))
          button52.grid(row= 6, column= 2, padx=5, pady=5)
          button53 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button53': checkHit(button53,6,3, name)))
          button53.grid(row= 6, column= 3, padx=5, pady=5)       
          button54 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button54': checkHit(button54,6,4, name)))
          button54.grid(row= 6, column= 4, padx=5, pady=5)
          button55 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button55': checkHit(button55,6,5, name)))
          button55.grid(row= 6, column= 5, padx=5, pady=5)       
          button56 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button56': checkHit(button56,6,6, name)))
          button56.grid(row= 6, column= 6, padx=5, pady=5)
          button57 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button57': checkHit(button57,6,7, name)))
          button57.grid(row= 6, column= 7, padx=5, pady=5)       
          button58 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button58': checkHit(button58,6,8, name)))
          button58.grid(row= 6, column= 8, padx=5, pady=5)
          button59 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button59': checkHit(button59,6,9, name)))
          button59.grid(row= 6, column= 9, padx=5, pady=5)       
          button60 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button60': checkHit(button60,6,10, name)))
          button60.grid(row= 6, column= 10, padx=5, pady=5)

          # Row 7 Buttons
          button61 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button61': checkHit(button61,7,1, name)))
          button61.grid(row= 7, column= 1, padx=5, pady=5)       
          button62 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button62': checkHit(button62,7,2, name)))
          button62.grid(row= 7, column= 2, padx=5, pady=5)
          button63 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button63': checkHit(button63,7,3, name)))
          button63.grid(row= 7, column= 3, padx=5, pady=5)       
          button64 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button64': checkHit(button64,7,4, name)))
          button64.grid(row= 7, column= 4, padx=5, pady=5)
          button65 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button65': checkHit(button65,7,5, name)))
          button65.grid(row= 7, column= 5, padx=5, pady=5)       
          button66 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button66': checkHit(button66,7,6, name)))
          button66.grid(row= 7, column= 6, padx=5, pady=5)
          button67 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button67': checkHit(button67,7,7, name)))
          button67.grid(row= 7, column= 7, padx=5, pady=5)       
          button68 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button68': checkHit(button68,7,8, name)))
          button68.grid(row= 7, column= 8, padx=5, pady=5)
          button69 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button69': checkHit(button69,7,9, name)))
          button69.grid(row= 7, column= 9, padx=5, pady=5)       
          button70 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button70': checkHit(button70,7,10, name)))
          button70.grid(row= 7, column= 10, padx=5, pady=5)

          # Row 8 Buttons
          button71 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button71': checkHit(button71,8,1, name)))
          button71.grid(row= 8, column= 1, padx=5, pady=5)       
          button72 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button72': checkHit(button72,8,2, name)))
          button72.grid(row= 8, column= 2, padx=5, pady=5)
          button73 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button73': checkHit(button73,8,3, name)))
          button73.grid(row= 8, column= 3, padx=5, pady=5)       
          button74 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button74': checkHit(button74,8,4, name)))
          button74.grid(row= 8, column= 4, padx=5, pady=5)
          button75 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button75': checkHit(button75,8,5, name)))
          button75.grid(row= 8, column= 5, padx=5, pady=5)       
          button76 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button76': checkHit(button76,8,6, name)))
          button76.grid(row= 8, column= 6, padx=5, pady=5)
          button77 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button77': checkHit(button77,8,7, name)))
          button77.grid(row= 8, column= 7, padx=5, pady=5)       
          button78 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button78': checkHit(button78,8,8, name)))
          button78.grid(row= 8, column= 8, padx=5, pady=5)
          button79 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button79': checkHit(button79,8,9, name)))
          button79.grid(row= 8, column= 9, padx=5, pady=5)       
          button80 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button80': checkHit(button80,8,10, name)))
          button80.grid(row= 8, column= 10, padx=5, pady=5)

          # Row 9 Buttons
          button81 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button81': checkHit(button81,9,1, name)))
          button81.grid(row= 9, column= 1, padx=5, pady=5)       
          button82 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button82': checkHit(button82,9,2, name)))
          button82.grid(row= 9, column= 2, padx=5, pady=5)
          button83 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button83': checkHit(button83,9,3, name)))
          button83.grid(row= 9, column= 3, padx=5, pady=5)       
          button84 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button84': checkHit(button84,9,4, name)))
          button84.grid(row= 9, column= 4, padx=5, pady=5)
          button85 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button85': checkHit(button85,9,5, name)))
          button85.grid(row= 9, column= 5, padx=5, pady=5)       
          button86 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button86': checkHit(button86,9,6, name)))
          button86.grid(row= 9, column= 6, padx=5, pady=5)
          button87 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button87': checkHit(button87,9,7, name)))
          button87.grid(row= 9, column= 7, padx=5, pady=5)       
          button88 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button88': checkHit(button88,9,8, name)))
          button88.grid(row= 9, column= 8, padx=5, pady=5)
          button89 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button89': checkHit(button89,9,9, name)))
          button89.grid(row= 9, column= 9, padx=5, pady=5)       
          button90 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button90': checkHit(button90,9,10, name)))
          button90.grid(row= 9, column= 10, padx=5, pady=5)

          # Row 10 Buttons
          button91 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button91': checkHit(button91,10,1, name)))
          button91.grid(row= 10, column= 1, padx=5, pady=5)       
          button92 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button92': checkHit(button92,10,2, name)))
          button92.grid(row= 10, column= 2, padx=5, pady=5)
          button93 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button93': checkHit(button93,10,3, name)))
          button93.grid(row= 10, column= 3, padx=5, pady=5)       
          button94 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button94': checkHit(button94,10,4, name)))
          button94.grid(row= 10, column= 4, padx=5, pady=5)
          button95 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button95': checkHit(button95,10,5, name)))
          button95.grid(row= 10, column= 5, padx=5, pady=5)       
          button96 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button96': checkHit(button96,10,6, name)))
          button96.grid(row= 10, column= 6, padx=5, pady=5)
          button97 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button97': checkHit(button97,10,7, name)))
          button97.grid(row= 10, column= 7, padx=5, pady=5)       
          button98 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button98': checkHit(button98,10,8, name)))
          button98.grid(row= 10, column= 8, padx=5, pady=5)
          button99 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button99': checkHit(button99,10,9, name)))
          button99.grid(row= 10, column= 9, padx=5, pady=5)       
          button100 = (tk.Button(fm, background = "grey", text= ' ', 
                   command= lambda name = 'button100': checkHit(button100,10,10, name)))
          button100.grid(row= 10, column= 10, padx=5, pady=5)

# Set up buttons for ship screen (100 buttons)
def builtButtons2(fm):
   # Row 1 Buttons
          button101 = (tk.Button(fm, background = "blue", text= ' ', state='normal', 
                   command= lambda name = 'button101': placePlayerShips(1,1, name)))
          button101.grid(row= 1, column= 1, padx=5, pady=5)
          shipScreenButtons[button101] = '11'
          button102 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button102': placePlayerShips(1,2, name)))
          button102.grid(row= 1, column= 2, padx=5, pady=5)
          shipScreenButtons[button102] = '12'
          button103 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button103': placePlayerShips(1,3, name)))
          button103.grid(row= 1, column= 3, padx=5, pady=5)
          shipScreenButtons[button103] = '13'
          button104 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button104': placePlayerShips(1,4, name)))
          button104.grid(row= 1, column= 4, padx=5, pady=5)
          shipScreenButtons[button104] = '14'
          button105 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button105': placePlayerShips(1,5, name)))
          button105.grid(row= 1, column= 5, padx=5, pady=5)
          shipScreenButtons[button105] = '15'
          button106 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button106': placePlayerShips(1,6, name)))
          button106.grid(row= 1, column= 6, padx=5, pady=5)
          shipScreenButtons[button106] = '16'
          button107 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button107': placePlayerShips(1,7, name)))
          button107.grid(row= 1, column= 7, padx=5, pady=5)
          shipScreenButtons[button107] = '17'
          button108 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button108': placePlayerShips(1,8, name)))
          button108.grid(row= 1, column= 8, padx=5, pady=5)
          shipScreenButtons[button108] = '18'
          button109 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button109': placePlayerShips(1,9, name)))
          button109.grid(row= 1, column= 9, padx=5, pady=5)
          shipScreenButtons[button109] = '19'
          button110 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button110': placePlayerShips(1,10, name)))
          button110.grid(row= 1, column= 10, padx=5, pady=5)
          shipScreenButtons[button110] = '110'

          # Row 2 Buttons
          button111 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button111': placePlayerShips(2,1, name)))
          button111.grid(row= 2, column= 1, padx=5, pady=5)
          shipScreenButtons[button111] = '21'
          button112 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button112': placePlayerShips(2,2, name)))
          button112.grid(row= 2, column= 2, padx=5, pady=5)
          shipScreenButtons[button112] = '22'
          button113 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button113': placePlayerShips(2,3, name)))
          button113.grid(row= 2, column= 3, padx=5, pady=5)
          shipScreenButtons[button113] = '23'
          button114 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button114': placePlayerShips(2,4, name)))
          button114.grid(row= 2, column= 4, padx=5, pady=5)
          shipScreenButtons[button114] = '24'
          button115 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button115': placePlayerShips(2,5, name)))
          button115.grid(row= 2, column= 5, padx=5, pady=5)
          shipScreenButtons[button115] = '25'
          button116 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button116': placePlayerShips(2,6, name)))
          button116.grid(row= 2, column= 6, padx=5, pady=5)
          shipScreenButtons[button116] = '26'
          button117 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button117': placePlayerShips(2,7, name)))
          button117.grid(row= 2, column= 7, padx=5, pady=5)
          shipScreenButtons[button117] = '27'
          button118 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button118': placePlayerShips(2,8, name)))
          button118.grid(row= 2, column= 8, padx=5, pady=5)
          shipScreenButtons[button118] = '28'
          button119 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button119': placePlayerShips(2,9, name)))
          button119.grid(row= 2, column= 9, padx=5, pady=5)
          shipScreenButtons[button119] = '29'
          button120 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button120': placePlayerShips(2,10, name)))
          button120.grid(row= 2, column= 10, padx=5, pady=5)
          shipScreenButtons[button120] = '210'

          # Row 3 Buttons
          button121 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button121': placePlayerShips(3,1, name)))
          button121.grid(row= 3, column= 1, padx=5, pady=5)
          shipScreenButtons[button121] = '31'
          button122 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button122': placePlayerShips(3,2, name)))
          button122.grid(row= 3, column= 2, padx=5, pady=5)
          shipScreenButtons[button122] = '32'
          button123 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button123': placePlayerShips(3,3, name)))
          button123.grid(row= 3, column= 3, padx=5, pady=5)
          shipScreenButtons[button123] = '33'
          button124 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button124': placePlayerShips(3,4, name)))
          button124.grid(row= 3, column= 4, padx=5, pady=5)
          shipScreenButtons[button124] = '34'
          button125 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button125': placePlayerShips(3,5, name)))
          button125.grid(row= 3, column= 5, padx=5, pady=5)
          shipScreenButtons[button125] = '35'
          button126 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button126': placePlayerShips(3,6, name)))
          button126.grid(row= 3, column= 6, padx=5, pady=5)
          shipScreenButtons[button126] = '36'
          button127 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button127': placePlayerShips(3,7, name)))
          button127.grid(row= 3, column= 7, padx=5, pady=5)
          shipScreenButtons[button127] = '37'
          button128 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button128': placePlayerShips(3,8, name)))
          button128.grid(row= 3, column= 8, padx=5, pady=5)
          shipScreenButtons[button128] = '38'
          button129 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button129': placePlayerShips(3,9, name)))
          button129.grid(row= 3, column= 9, padx=5, pady=5)
          shipScreenButtons[button129] = '39'
          button130 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button130': placePlayerShips(3,10, name)))
          button130.grid(row= 3, column= 10, padx=5, pady=5)
          shipScreenButtons[button130] = '310'

          # Row 4 Buttons
          button131 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button131': placePlayerShips(4,1, name)))
          button131.grid(row= 4, column= 1, padx=5, pady=5)
          shipScreenButtons[button131] = '41'
          button132 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button132': placePlayerShips(4,2, name)))
          button132.grid(row= 4, column= 2, padx=5, pady=5)
          shipScreenButtons[button132] = '42'
          button133 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button133': placePlayerShips(4,3, name)))
          button133.grid(row= 4, column= 3, padx=5, pady=5)
          shipScreenButtons[button133] = '43'
          button134 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button134': placePlayerShips(4,4, name)))
          button134.grid(row= 4, column= 4, padx=5, pady=5)
          shipScreenButtons[button134] = '44'
          button135 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button135': placePlayerShips(4,5, name)))
          button135.grid(row= 4, column= 5, padx=5, pady=5)
          shipScreenButtons[button135] = '45'
          button136 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button136': placePlayerShips(4,6, name)))
          button136.grid(row= 4, column= 6, padx=5, pady=5)
          shipScreenButtons[button136] = '46'
          button137 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button137': placePlayerShips(4,7, name)))
          button137.grid(row= 4, column= 7, padx=5, pady=5)
          shipScreenButtons[button137] = '47'
          button138 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button138': placePlayerShips(4,8, name)))
          button138.grid(row= 4, column= 8, padx=5, pady=5)
          shipScreenButtons[button138] = '48'
          button139 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button139': placePlayerShips(4,9, name)))
          button139.grid(row= 4, column= 9, padx=5, pady=5)
          shipScreenButtons[button139] = '49'
          button140 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button140': placePlayerShips(4,10, name)))
          button140.grid(row= 4, column= 10, padx=5, pady=5)
          shipScreenButtons[button140] = '410'

          # Row 5 Buttons
          button141 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button141': placePlayerShips(5,1, name)))
          button141.grid(row= 5, column= 1, padx=5, pady=5)
          shipScreenButtons[button141] = '51'
          button142 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button142': placePlayerShips(5,2, name)))
          button142.grid(row= 5, column= 2, padx=5, pady=5)
          shipScreenButtons[button142] = '52'
          button143 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button143': placePlayerShips(5,3, name)))
          button143.grid(row= 5, column= 3, padx=5, pady=5)
          shipScreenButtons[button143] = '53'
          button144 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button144': placePlayerShips(5,4, name)))
          button144.grid(row= 5, column= 4, padx=5, pady=5)
          shipScreenButtons[button144] = '54'
          button145 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button145': placePlayerShips(5,5, name)))
          button145.grid(row= 5, column= 5, padx=5, pady=5)
          shipScreenButtons[button145] = '55'
          button146 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button146': placePlayerShips(5,6, name)))
          button146.grid(row= 5, column= 6, padx=5, pady=5)
          shipScreenButtons[button146] = '56'
          button147 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button147': placePlayerShips(5,7, name)))
          button147.grid(row= 5, column= 7, padx=5, pady=5)
          shipScreenButtons[button147] = '57'
          button148 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button148': placePlayerShips(5,8, name)))
          button148.grid(row= 5, column= 8, padx=5, pady=5)
          shipScreenButtons[button148] = '58'
          button149 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button149': placePlayerShips(5,9, name)))
          button149.grid(row= 5, column= 9, padx=5, pady=5)
          shipScreenButtons[button149] = '59'
          button150 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button150': placePlayerShips(5,10, name)))
          button150.grid(row= 5, column= 10, padx=5, pady=5)
          shipScreenButtons[button150] = '510'

          # Row 6 Buttons
          button151 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button151': placePlayerShips(6,1, name)))
          button151.grid(row= 6, column= 1, padx=5, pady=5)
          shipScreenButtons[button151] = '61'
          button152 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button152': placePlayerShips(6,2, name)))
          button152.grid(row= 6, column= 2, padx=5, pady=5)
          shipScreenButtons[button152] = '62'
          button153 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button153': placePlayerShips(6,3, name)))
          button153.grid(row= 6, column= 3, padx=5, pady=5)
          shipScreenButtons[button153] = '63'
          button154 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button154': placePlayerShips(6,4, name)))
          button154.grid(row= 6, column= 4, padx=5, pady=5)
          shipScreenButtons[button154] = '64'
          button155 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button155': placePlayerShips(6,5, name)))
          button155.grid(row= 6, column= 5, padx=5, pady=5)
          shipScreenButtons[button155] = '65'
          button156 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button156': placePlayerShips(6,6, name)))
          button156.grid(row= 6, column= 6, padx=5, pady=5)
          shipScreenButtons[button156] = '66'
          button157 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button157': placePlayerShips(6,7, name)))
          button157.grid(row= 6, column= 7, padx=5, pady=5)
          shipScreenButtons[button157] = '67'
          button158 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button158': placePlayerShips(6,8, name)))
          button158.grid(row= 6, column= 8, padx=5, pady=5)
          shipScreenButtons[button158] = '68'
          button159 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button159': placePlayerShips(6,9, name)))
          button159.grid(row= 6, column= 9, padx=5, pady=5)
          shipScreenButtons[button159] = '69'
          button160 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button160': placePlayerShips(6,10, name)))
          button160.grid(row= 6, column= 10, padx=5, pady=5)
          shipScreenButtons[button160] = '610'

          # Row 7 Buttons
          button161 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button161': placePlayerShips(7,1, name)))
          button161.grid(row= 7, column= 1, padx=5, pady=5)
          shipScreenButtons[button161] = '71'
          button162 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button162': placePlayerShips(7,2, name)))
          button162.grid(row= 7, column= 2, padx=5, pady=5)
          shipScreenButtons[button162] = '72'
          button163 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button163': placePlayerShips(7,3, name)))
          button163.grid(row= 7, column= 3, padx=5, pady=5)
          shipScreenButtons[button163] = '73'
          button164 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button164': placePlayerShips(7,4, name)))
          button164.grid(row= 7, column= 4, padx=5, pady=5)
          shipScreenButtons[button164] = '74'
          button165 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button165': placePlayerShips(7,5, name)))
          button165.grid(row= 7, column= 5, padx=5, pady=5)
          shipScreenButtons[button165] = '75'
          button166 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button166': placePlayerShips(7,6, name)))
          button166.grid(row= 7, column= 6, padx=5, pady=5)
          shipScreenButtons[button166] = '76'
          button167 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button167': placePlayerShips(7,7, name)))
          button167.grid(row= 7, column= 7, padx=5, pady=5)
          shipScreenButtons[button167] = '77'
          button168 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button168': placePlayerShips(7,8, name)))
          button168.grid(row= 7, column= 8, padx=5, pady=5)
          shipScreenButtons[button168] = '78'
          button169 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button169': placePlayerShips(7,9, name)))
          button169.grid(row= 7, column= 9, padx=5, pady=5)
          shipScreenButtons[button169] = '79'
          button170 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button170': placePlayerShips(7,10, name)))
          button170.grid(row= 7, column= 10, padx=5, pady=5)
          shipScreenButtons[button170] = '710'

          # Row 8 Buttons
          button171 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button171': placePlayerShips(8,1, name)))
          button171.grid(row= 8, column= 1, padx=5, pady=5)
          shipScreenButtons[button171] = '81'
          button172 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button172': placePlayerShips(8,2, name)))
          button172.grid(row= 8, column= 2, padx=5, pady=5)
          shipScreenButtons[button172] = '82'
          button173 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button173': placePlayerShips(8,3, name)))
          button173.grid(row= 8, column= 3, padx=5, pady=5)
          shipScreenButtons[button173] = '83'
          button174 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button174': placePlayerShips(8,4, name)))
          button174.grid(row= 8, column= 4, padx=5, pady=5)
          shipScreenButtons[button174] = '84'
          button175 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button175': placePlayerShips(8,5, name)))
          button175.grid(row= 8, column= 5, padx=5, pady=5)
          shipScreenButtons[button175] = '85'
          button176 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button176': placePlayerShips(8,6, name)))
          button176.grid(row= 8, column= 6, padx=5, pady=5)
          shipScreenButtons[button176] = '86'
          button177 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button177': placePlayerShips(8,7, name)))
          button177.grid(row= 8, column= 7, padx=5, pady=5)
          shipScreenButtons[button177] = '87'
          button178 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button178': placePlayerShips(8,8, name)))
          button178.grid(row= 8, column= 8, padx=5, pady=5)
          shipScreenButtons[button178] = '88'
          button179 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button179': placePlayerShips(8,9, name)))
          button179.grid(row= 8, column= 9, padx=5, pady=5)
          shipScreenButtons[button179] = '89'
          button180 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button180': placePlayerShips(8,10, name)))
          button180.grid(row= 8, column= 10, padx=5, pady=5)
          shipScreenButtons[button180] = '810'

          # Row 9 Buttons
          button181 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button181': placePlayerShips(9,1, name)))
          button181.grid(row= 9, column= 1, padx=5, pady=5)
          shipScreenButtons[button181] = '91'
          button182 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button182': placePlayerShips(9,2, name)))
          button182.grid(row= 9, column= 2, padx=5, pady=5)
          shipScreenButtons[button182] = '92'
          button183 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button183': placePlayerShips(9,3, name)))
          button183.grid(row= 9, column= 3, padx=5, pady=5)
          shipScreenButtons[button183] = '93'
          button184 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button184': placePlayerShips(9,4, name)))
          button184.grid(row= 9, column= 4, padx=5, pady=5)
          shipScreenButtons[button184] = '94'
          button185 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button185': placePlayerShips(9,5, name)))
          button185.grid(row= 9, column= 5, padx=5, pady=5)
          shipScreenButtons[button185] = '95'
          button186 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button186': placePlayerShips(9,6, name)))
          button186.grid(row= 9, column= 6, padx=5, pady=5)
          shipScreenButtons[button186] = '96'
          button187 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button187': placePlayerShips(9,7, name)))
          button187.grid(row= 9, column= 7, padx=5, pady=5)
          shipScreenButtons[button187] = '97'
          button188 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button188': placePlayerShips(9,8, name)))
          button188.grid(row= 9, column= 8, padx=5, pady=5)
          shipScreenButtons[button188] = '98'
          button189 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button189': placePlayerShips(9,9, name)))
          button189.grid(row= 9, column= 9, padx=5, pady=5)
          shipScreenButtons[button189] = '99'
          button190 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button190': placePlayerShips(9,10, name)))
          button190.grid(row= 9, column= 10, padx=5, pady=5)
          shipScreenButtons[button190] = '910'

          # Row 10 Buttons
          button191 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button191': placePlayerShips(10,1, name)))
          button191.grid(row= 10, column= 1, padx=5, pady=5)
          shipScreenButtons[button191] = '101'
          button192 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button192': placePlayerShips(10,2, name)))
          button192.grid(row= 10, column= 2, padx=5, pady=5)
          shipScreenButtons[button192] = '102'
          button193 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button193': placePlayerShips(10,3, name)))
          button193.grid(row= 10, column= 3, padx=5, pady=5)
          shipScreenButtons[button193] = '103'
          button194 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button194': placePlayerShips(10,4, name)))
          button194.grid(row= 10, column= 4, padx=5, pady=5)
          shipScreenButtons[button194] = '104'
          button195 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button195': placePlayerShips(10,5, name)))
          button195.grid(row= 10, column= 5, padx=5, pady=5)
          shipScreenButtons[button195] = '105'
          button196 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button196': placePlayerShips(10,6, name)))
          button196.grid(row= 10, column= 6, padx=5, pady=5)
          shipScreenButtons[button196] = '106'
          button197 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button197': placePlayerShips(10,7, name)))
          button197.grid(row= 10, column= 7, padx=5, pady=5)
          shipScreenButtons[button197] = '107'
          button198 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button198': placePlayerShips(10,8, name)))
          button198.grid(row= 10, column= 8, padx=5, pady=5)
          shipScreenButtons[button198] = '108'
          button199 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button199': placePlayerShips(10,9, name)))
          button199.grid(row= 10, column= 9, padx=5, pady=5)
          shipScreenButtons[button199] = '109'
          button200 = (tk.Button(fm, background = "blue", text= ' ', 
                   command= lambda name = 'button200': placePlayerShips(10,10, name)))
          button200.grid(row= 10, column= 10, padx=5, pady=5)
          shipScreenButtons[button200] = '1010'

# Set the the App details.        
root = tk.Tk()
w = 373 # width for the Tk root
h = 458 # height for the Tk root
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/12) - (h/12)
root.option_add('*font', ('verdana', 12, 'bold'))
root.title("Battle Screen")
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

win2 = tk.Tk()
w = 373 # width for the Tk root
h = 458 # height for the Tk root
ws = win2.winfo_screenwidth() # width of the screen
hs = win2.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/1.15) - (h/1.15)
win2.option_add('*font', ('verdana', 12, 'bold'))
win2.title("Ship Direction")
win2.geometry('%dx%d+%d+%d' % (w, h, x, y))

win3 = tk.Tk()
w = 100 # width for the Tk root
h = 175 # height for the Tk root
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
ws = win3.winfo_screenwidth() # width of the screen
hs = win3.winfo_screenheight() # height of the screen
win3.option_add('*font', ('verdana', 12, 'bold'))
win3.title("Ship Direction")
win3.geometry('%dx%d+%d+%d' % (w, h, x, y))

win4 = tk.Tk()
w = 100 # width for the Tk root
h = 175 # height for the Tk root
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
ws = win3.winfo_screenwidth() # width of the screen
hs = win3.winfo_screenheight() # height of the screen
win4.option_add('*font', ('verdana', 12, 'bold'))
win4.title("Ship Direction")
win4.geometry('%dx%d+%d+%d' % (w, h, x, y))

win5 = tk.Tk()
w = 100 # width for the Tk root
h = 175 # height for the Tk root
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
ws = win3.winfo_screenwidth() # width of the screen
hs = win3.winfo_screenheight() # height of the screen
win5.option_add('*font', ('verdana', 12, 'bold'))
win5.title("Ship Direction")
win5.geometry('%dx%d+%d+%d' % (w, h, x, y))

win6 = tk.Tk()
w = 100 # width for the Tk root
h = 175 # height for the Tk root
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
ws = win3.winfo_screenwidth() # width of the screen
hs = win3.winfo_screenheight() # height of the screen
win6.option_add('*font', ('verdana', 12, 'bold'))
win6.title("Ship Direction")
win6.geometry('%dx%d+%d+%d' % (w, h, x, y))

win7 = tk.Tk()
w = 100 # width for the Tk root
h = 175 # height for the Tk root
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
ws = win3.winfo_screenwidth() # width of the screen
hs = win3.winfo_screenheight() # height of the screen
win7.option_add('*font', ('verdana', 12, 'bold'))
win7.title("Ship Direction")
win7.geometry('%dx%d+%d+%d' % (w, h, x, y))

display = BattleGrid(root)
display = PlayerGrid(win2)

display = Direction(win3)
display = Direction(win4)
display = Direction(win5)
display = Direction(win6)
display = Direction(win7)

root.mainloop()   

