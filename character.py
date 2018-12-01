import pygame
class init:
    def __init__(self,size):
        global possition
        possition = self
        possition.x = 0
        possition.y = 0
        possition.x_ = 0
        possition.y_ = 0
        possition.direction = 0
        self.x = possition.x
        self.y = possition.y
        self.size =size # I think that shouldwork
class draw:
    def __init__(self,window,size):
        pygame.draw.rect(window,(0,0,0),(295,295,size,size))
        #pygame.display.update()
class MOVE:
    def change(L):
        global possition
        possition.x -=int(L[0])
        possition.y -=int(L[1])
    def update():
        if abs(possition.x_) + abs(possition.y_) ==1:
            possition.x -=possition.x_
            possition.y +=possition.y_
        if abs(possition.x_) + abs(possition.y_) ==2:
            possition.x -=possition.x_/2
            possition.y +=possition.y_/2
    def wasd(event):
        MOVE.left(event)
        MOVE.right(event)
        MOVE.up(event)
        MOVE.down(event)
    def left(event):
        global possition
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                possition.x_ = 1
                possition.y_ = 0
                possition.direction = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                if possition.x_ == 1:
                    possition.x_ = 0
    def right(event):
        global possition
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                possition.x_ = -1
                possition.y_ = 0
                possition.direction = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                if possition.x_ == -1:
                    possition.x_ = 0
    def up(event):
        global possition
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                possition.y_ = -1
                possition.x_ = 0
                possition.direction = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                if possition.y_ == -1:
                    possition.y_ = 0
    def down(event):
        global possition
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                possition.y_ = 1
                possition.x_ = 0
                possition.direction = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                if possition.y_ == 1:
                    possition.y_ = 0
