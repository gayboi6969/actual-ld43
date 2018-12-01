import pygame
import character as Character
class tiles:
    def __init__(self):
        tiles = [[20,20],[40,20],[60,20],[80,20]]
        global TileImg,TImgMask,output
        output = "0|0"
        TileImg = pygame.image.load("images\\tile.png")
        TileImgMask = pygame.mask.from_surface(TileImg)
    def gen(window,tiles):
        global TileImg,TImgMask,output
        for x in tiles:
            window.blit(TileImg,[x[0]-Character.possition.x,x[1]-Character.possition.y])
        #pygame.display.update()
    def collide(direction,x,y,tiless):
        global TileImg,TImgMask,output
        for z in tiless:
            if 295> z[0]-Character.possition.x-10 and 295< z[0]-Character.possition.x+40 and 295> z[1]-Character.possition.y-10 and 295< z[1]-Character.possition.y+40:
                if direction ==0:
                    output = "0|-4"
                if direction ==1:
                    output ="4|0"
                if direction ==2:
                    output = "0|4"
                if direction ==3:
                    output = "-4|0"
                Character.MOVE.change((output).split("|"))
            else:
                output ="0|0"
