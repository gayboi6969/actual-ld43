import pygame
import gamedisplay
import character as Character
import tiles
import MusicHandler
tiles.tiles()
character = Character.init(10)
displayOS = gamedisplay.init()
tiless = [[20,20],[60,20],[100,20],[140,20],[140,60],[20,100],[60,100],[100,100],[140,100],[800,100]]
MusicHandler.menu.play()
while True:
    displayOS.clock.tick(128)
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
            quit()
        Character.MOVE.wasd(event)
    tiles.tiles.collide(Character.possition.direction,Character.possition.x,Character.possition.y,tiless)
    displayOS.window.fill((255,255,255))
    Character.MOVE.update()
    tiles.tiles.gen(displayOS.window,tiless)
    Character.draw(displayOS.window,character.size)
    pygame.display.update()
