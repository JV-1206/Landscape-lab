tools = [
    {
        "name": "college students",
        "wage": 250,
        "cost": 500
    },
    {
    "name": 'a battery-powered lawnmower',
    "wage": 100,
    "cost": 250
  },
  {
    "name": 'an old-timey push lawnmower',
    "wage": 50,
    "cost": 35
  },
  {
    "name": 'scissors',
    "wage": 5,
    "cost": 5
  },
  {
    "name": 'teeth',
    "wage": 1,
    "cost": 0
  }
]

# player dictionary (object)

player = {
    'currentTool': tools.pop(),
    "bankAccount": 0
}


# ACTIONS ===========================

# Game start
def startGame():
    print("Start earning money today with your new business")

    # Begin game functionality 
    showStatus()

    askForAction()






def showStatus():
    print("Current tool: " + player["currentTool"]["name"] + " // Bank account balance: " + str(player["bankAccount"]))



def cutGrass():
    player["bankAccount"] += player["currentTool"]["wage"]

    print(" Workin' hard or hardly workin'! You earned " + str(player["currentTool"]["wage"]) + " today using " + player["currentTool"]["name"])

    checkWin()
   

def buyTool():
    if (player["bankAccount"] >= tools[len(tools) - 1]["cost"]):
        
        player["bankAccount"] -= tools[len(tools) - 1]["cost"]

        player["currentTool"] = tools.pop()

        print("You just bought " + player["currentTool"]["name"] + " for $" + str(player["currentTool"]["cost"]))

        showStatus()
        askForAction()
    else:
        print("You can't afford " + tools[len(tools) - 1]["name"] + " Keep on hustlin'")

        askForAction()

def askForAction():
  playerChoice = ""
  if(len(tools) > 0):
      playerChoice = input("What do you want to do? (buy tool / cut grass)").lower()

  else:
      print("No more tools left, keeping working until you reach $1,000!")
      playerChoice = input("You HAVE TO cut grass! (type 'cut grass')").lower()

  if (playerChoice == "cut grass"):
      cutGrass()
  elif (playerChoice == "buy tool" and len(tools) > 0):
      buyTool()
  else:
      print("Invalid input, please try again!")
      askForAction()


def checkWin():
    if(player["bankAccount"] >= 1000 and player["currentTool"]["name"] == "college students"):
        print("You won!! Woohoo! (Give your students a raise!!!!)")

    else: 
        print("Not quite there yet, keep on chugging")
        showStatus()
        askForAction()


# Get the game to
startGame()