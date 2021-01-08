import pygame
from pygame.locals import *
from time import sleep
from random import randrange

pygame.init()

#Set the screen size and window title
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height))
title = pygame.display.set_caption('Spot The Difference')

#Set the images and noises
difference = pygame.image.load("/home/pi/python/difference/spot_the_diff.png")
zombie = pygame.image.load("/home/pi/python/difference/scary_face.png")
scream = pygame.mixer.Sound("/home/pi/python/difference/scream.wav")

#Optional setting to make sure the image fills the screen
difference = pygame.transform.scale(difference, (width, height))
zombie = pygame.transform.scale(zombie, (width, height))

#Set the first image and update the display
screen.blit(difference, (0,0))
pygame.display.update()

#Set the image to show for a random time between 5 and 15 seconds)
sleep(randrange(5,15))

#Play the scream and show the scary picture
scream.play()
sleep(0.4)
screen.blit(zombie, (0,0))
pygame.display.update()
sleep(3)

#Stop the scream and quit the program
scream.stop()
pygame.quit()