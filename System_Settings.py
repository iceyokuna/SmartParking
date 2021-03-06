import pygame
import os

#Initialization
pygame.init()
display_width = 715
display_height = 527
window_title = "Smart Parking"

#Color
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
PURPLE = (229,0,255)
BLUE = (0,0,225)
GREEN = (0,255,0)
CYAN = (92, 247, 223)

#Font
font1 = pygame.font.SysFont("Times New Roman, Arial", 30)
font2 = pygame.font.SysFont("Times New Roman, Arial", 20)
font3 = pygame.font.SysFont("Times New Roman, Arial", 60)

#Text in EditMap
panelText = font1.render("Menu Panel",True, WHITE)
parkingText = font1.render("Car Park",True, BLACK)
wallText = font1.render("Wall",True, BLACK)
entranceText = font1.render("Entrance",True,WHITE)
exitText = font1.render("Exit",True,BLACK)
pathText = font1.render("Path",True,BLACK)


saveText = font2.render("Save",True,BLACK)
loadText = font2.render("Load",True,BLACK)
clearText = font2.render("Clear",True,BLACK)


#Text in Simulation
carEntranceText1 = font1.render("Entrance 1",True,WHITE)
carEntranceText2 = font1.render("Entrance 2",True,WHITE)
decText1 = font3.render("-",True,BLACK)
incText1 = font3.render("+",True,BLACK)
decText2 = font3.render("-",True,BLACK)
incText2 = font3.render("+",True,BLACK)

startText = font1.render("Start!",True,BLACK)
stopText = font1.render("Stop/Pause",True,BLACK)
exitText2 = font1.render("Exit",True,BLACK)


#picture
menuPic = pygame.image.load(os.path.join("photo","backgroundMenu.png"))
mainMenuPic = pygame.image.load(os.path.join("photo","mainMenu.png"))

editButtonPic = pygame.image.load(os.path.join("photo","createButton.png"))
simulateButtonPic = pygame.image.load(os.path.join("photo","simulateButton.png"))
exitButtonPic = pygame.image.load(os.path.join("photo","exitButton.png"))




#System Property
margin = 1
block = 20

#Setup
window = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Smart Parking")
clock=pygame.time.Clock()
