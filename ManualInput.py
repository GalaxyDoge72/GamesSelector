import random

gamesList = []

gameCount = int(input("How many games do you have? "))

for index in range(gameCount):
    toAdd = input("What is the game's title? ")
    gamesList.append(toAdd)

gameToPlay = random.randint(0, (gameCount - 1))
selectedGame = gamesList[gameToPlay]
print("The randomly chosen game is: " + selectedGame )
input('Press any button to exit...')
