import cdll
from random import randint as ri
import os
from tkinter import *

root = Tk()
root.title("Season Quest")
root.iconbitmap(r"G:\My Drive\School\01_Fall2024\CS210\Project1\images\windowIcon.ico")

board = cdll.MyList(0)

dirCurrent = os.path.dirname(__file__) #'G:\\My Drive\\School\\01_Fall2024\\CS210\\Project1\\images\\'

class Player:
    def __init__(self, _img):
        self.img = _img

dirPlayerImgs = dirCurrent + '\\images\\players\\'
playerImg = [
    '0_player.png', '1_player.png', '2_player.png', '3_player.png'
]

emptyPlayerImg = PhotoImage(file = dirPlayerImgs + 'empty.png')

class Space:
    def __init__(self, _name, _coord, _img, _costMax, _costMin):
        self.name = _name
        self.coord = _coord
        self.img = _img
        self.costMax = _costMin
        self.costMin = _costMax
        self.frame = None
        
spaceName = [
    "Blossomgrove Forest", "Emerald Glade", "Sylvanwood Clearing", "River of Whispers", "Faewater Spring", "Moonlit Pond",
    "Emberglass Desert", "Dunes of Despair", "Ashen Oasis", "Dragonspire Summit", "Magmavine Ridge", "Sunken Flame Gorge",
    "Dreadthorn Thicket", "Gloomroot Grove", "Hollowshade Wood", "Crumbled Ruins", "Forsaken Barrow", "Phantom Moor",
    "Frostveil Crags", "Icebound Cavern", "Glacial Abyss", "Shadowblight Wasteland", "Deadwood Hollow", "Wraithmarsh"
]

# spaceCoord = [
#     [0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6],    #top row
#     [1,6], [2,6], [3,6], [4,6], [5,6],                  #right column
#     [6,6], [6,5], [6,4], [6,3], [6,2], [6,1], [6,0],    #bottom row
#     [5,0], [4,0], [3,0], [2,0], [1,0]                   #left column
# ]

spaceCoord = [
    [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9],    # top row
    [1, 9], [2, 9], [3, 9], [4, 9], [5, 9],                    # right column
    [6, 9], [6, 8], [6, 7], [6, 6], [6, 5], [6, 4], [6, 3],    # bottom row
    [5, 3], [4, 3], [3, 3], [2, 3], [1, 3]                     # left column
]

dirSpaceImgs = dirCurrent + '\\images\\spaces\\'
spaceImg = [
    '00_Blossomgrove_Forest.png', '01_Emerald Glade.png', '02_Sylvanwood Clearing.png', '03_River Of Whispers.png', '04_Faewater Spring.png', '05_Moonlit Pond.png',
    '06_Emberglass Desert.png','07_Dunes of Despair.png','08_Ashen Oasis.png', '09_Dragonspire Summit.png', '10_Magmavine Ridge.png', '11_Sunken Flame Gorge.png',
    '12_Dreadthorn Thicket.png', '13_Gloomroot Grove.png', '14_Hollowshade Wood.png', '15_Crumbled Ruins.png', '16_Forsaken Barrow.png', '17_Phantom Moor.png',
    '18_Frostveil Crags.png', '19_Icebound Cavern.png', '20_Glacial Abyss.png', '21_Shadowblight Wasteland.png', '22_Deadwood Hollow.png', '23_Wraithmarsh.png'
]

cost = [[190, 380], [140, 280], [160, 320], [200, 400], [170, 340], [170, 340],
        [110, 220], [190, 380], [190, 380], [110, 220], [130, 260], [130, 260],
        [130, 260], [100, 200], [190, 380], [100, 200], [130, 260], [170, 340],
        [190, 380], [100, 200], [140, 280], [180, 360], [160, 320], [170, 340],
        [180, 360], [120, 240], [140, 280], [200, 400]]

########### change this to the linked list    
spaces = []
for i in range(24):
    newSpaceInstance = Space(spaceName[i], spaceCoord[i], dirSpaceImgs + spaceImg[i], cost[i][0], cost[i][1])
    spaces.append(newSpaceInstance)

spacePhotoObjArray = []
boardConstructionIndex = 0
for item in spaces:
    newPhotoObj = PhotoImage(file=item.img)
    spacePhotoObjArray.append(newPhotoObj)
    item.frame = LabelFrame(root, text='test')
    item.frame.grid(row=item.coord[0], column=item.coord[1])
    spaceImgLab = Label(item.frame, image=spacePhotoObjArray[boardConstructionIndex])
    spaceImgLab.grid(row=0, column=0, columnspan=4)
    player1ImgLab = Label(item.frame, image=emptyPlayerImg)
    player1ImgLab.grid(row=1, column=0)
    player2ImgLab = Label(item.frame, image=emptyPlayerImg)
    player2ImgLab.grid(row=1, column=1)
    player3ImgLab = Label(item.frame, image=emptyPlayerImg)
    player3ImgLab.grid(row=1, column=2)
    player4ImgLab = Label(item.frame, image=emptyPlayerImg)
    player4ImgLab.grid(row=1, column=3)
    boardConstructionIndex += 1


btn_quit = Button(root, text="QUIT", command=root.quit)
btn_quit.grid(row=0, column=0)

btn_rollDice = Button(root, text="roll dice")
btn_rollDice.grid(row=0, column=1)

btn_three = Button(root, text="btn three")
btn_three.grid(row=0, column=2)

playerPhotoObjArray = []


root.mainloop()