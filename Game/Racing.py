import pygame
import sys
from pygame.locals import *

# Define window dimensions
WINDOWWIDTH = 400
WINDOWHEIGHT = 600

# Initialize Pygame
pygame.init()

# Set up the display
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('RACING') 

# Define constants for the game
FPS = 60
fpsClock = pygame.time.Clock()

# Load background image and set background speed
BGSPEED = 1.5
BGIMG = pygame.image.load('path') # Link path picture background

# Load car image and set car dimensions and speed
CARWIDTH = 40
CARHEIGHT = 60
CARSPEED = 3
CARIMG = pygame.image.load('path') # Link path picture car

# Define the margin for the car's movement
X_MARGIN = 80

class Background():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = BGSPEED
        self.img = BGIMG
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def draw(self):
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y-self.height)))

    def update(self):
        self.y += self.speed
        if self.y > self.height:
            self.y -= self.height

class Car():
    def __init__(self):
        self.width = CARWIDTH
        self.height = CARHEIGHT
        self.x = (WINDOWWIDTH-self.width)/2
        self.y = (WINDOWHEIGHT-self.height)/2
        self.speed = CARSPEED

    def draw(self):
        DISPLAYSURF.blit(CARIMG, (int(self.x), int(self.y)))

    def update(self, moveLeft, moveRight, moveUp, moveDown):
        if moveLeft:
            self.x -= self.speed
        if moveRight:
            self.x += self.speed
        if moveUp:
            self.y -= self.speed
        if moveDown:
            self.y += self.speed

        if self.x < X_MARGIN:
            self.x = X_MARGIN
        if self.x + self.width > WINDOWWIDTH - X_MARGIN:
            self.x = WINDOWWIDTH - X_MARGIN - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > WINDOWHEIGHT:
            self.y = WINDOWHEIGHT - self.height

def gameStart():
    pass

def gamePlay(bg, car):
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    moveLeft = True
                if event.key == K_RIGHT:
                    moveRight = True
                if event.key == K_UP:
                    moveUp = True
                if event.key == K_DOWN:
                    moveDown = True
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    moveLeft = False
                if event.key == K_RIGHT:
                    moveRight = False
                if event.key == K_UP:
                    moveUp = False
                if event.key == K_DOWN:
                    moveDown = False

        DISPLAYSURF.fill((0, 0, 0))  # Fill the screen with black color
        bg.draw()
        bg.update()
        car.draw()
        car.update(moveLeft, moveRight, moveUp, moveDown)
        pygame.display.update()
        fpsClock.tick(FPS)

def gameOver():
    pass

def main():
    bg = Background()
    car = Car()
    gameStart()

    while True:
        gamePlay(bg, car)
        gameOver()

if __name__ == '__main__':
    main()
