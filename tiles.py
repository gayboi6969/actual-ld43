import pygame
class tiles:
    def __init__(self):
        tiles = [[20,20],[40,20],[60,20],[80,20]]
        global TileImg,TImgMask
        TileImg = pygame.image.load("images\\tile.png")
        TileImgMask = pygame.mask.from_surface(TileImg)
    def gen(window,tiles):
        global TileImg,TImgMask
        for x in tiles:
            window.blit(TileImg,x)
        #pygame.display.update()
    def collide(direction,x,y,tiles):
        for z in tiles:
            if x>= z[0] and x>= z[0] and y>= z[1] and y>= z[1]:
                if direction ==0:
                    return "0|-6"
