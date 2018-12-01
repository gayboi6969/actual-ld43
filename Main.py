import pygame
import gamedisplay
import character as Character
import tiles
tiles.tiles()
character = Character.init(10)
displayOS = gamedisplay.init()
while True:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
            quit()
        Character.MOVE.wasd(event)
    tiles.tiles.collide(Character.possition.direction,Character.possition.x,Character.possition.x,[[20,20],[60,20],[100,20],[140,20]])
    displayOS.window.fill((255,255,255))
    Character.MOVE.update()
    tiles.tiles.gen(displayOS.window,[[20,20],[60,20],[100,20],[140,20]])
    Character.draw(displayOS.window,character.size)
    pygame.display.update()
