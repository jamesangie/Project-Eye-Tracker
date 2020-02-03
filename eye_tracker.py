"""
Project Name: Eye Tracker simulator
Author: James Z
Date: nov/7/2019
"""
import pygame
import os
## multitimer is the timer that can start and
# stop multiple times unlike threading.timer
# which sucks
import multitimer as mt

## initialing variables
x = y = 0
running = 1
screen = pygame.display.set_mode((800, 540))
p = (x, y)
timer_on = False
distracted = False
monitor = False
os.system('cls')
# define timer t and vibration function
print("Give the time inverval in seconds: ")
interval = input()
def vibration():
    print("seat and wheel vibration created")
t = mt.MultiTimer(3, vibration, runonstart=False)


os.system('cls')
while running:
    # background image displayed
    event = pygame.event.poll()
    image = pygame.image.load("chenei.jpg")
    if event.type == pygame.QUIT:
        running = 0
    # get the mouse position
    elif event.type == pygame.MOUSEMOTION:
        p = event.pos
    # show the mouse pos by click
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print(event.pos)
    # area that driver is distracted
    monitor = p[0] > 334 and p[0] < 467 and p[1] < 176 and p[1] > 126
    distracted = monitor or p[1] > 178 or p[1] < 42 or p[1] > (p[0]*1.837838-48.054076) or p[1] > (p[0]*(-1.728395)+1349.308642)
    # set timer is distracted. vibrate when time up
    if distracted and timer_on is False:
        t.start()
        timer_on = True
    # cancel the timer and stop the vibration when look back to the good area
    elif not(distracted) and timer_on is True:
        timer_on = False
        t.stop()
        os.system('cls')

    screen.fill((0, 0, 0))
    screen.blit(image, (0, 0))

    pygame.display.flip()