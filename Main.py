import pygame
import gamedisplay
import character as Character
character = Character.init(10)
displayOS = gamedisplay.init()
while True:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
            quit()
        Character.MOVE.wasd(event)
    displayOS.window.fill((255,255,255))
    Character.MOVE.update()
    Character.draw(displayOS.window,character.size)
    pygame.display.update()
