import tkinter as tk
import random
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

gamesTxtFile = filedialog.askopenfilename()

gamesList = []
with open(gamesTxtFile, 'r') as file:
    lines = file.readlines()

numberOfLines = len(lines)

for index in range(numberOfLines):
    gamesList.append(lines[index].strip())
gameToPlay = random.randint(0, numberOfLines)
selectedGame = gamesList[gameToPlay]
print('The selected game is', selectedGame)