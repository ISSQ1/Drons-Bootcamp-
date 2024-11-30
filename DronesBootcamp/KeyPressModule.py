import pygame

def init(): #initailize a window
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def getKey(KeyName):
    ans = False
    for eve in pygame.event.get(): pass
    KeyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(KeyName))  #key{LEFT}
    if KeyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey("LEFT"):
        print("Left Key pressed")
    if getKey("RIGHT"):
        print("Right Key pressed");


if __name__ == '__main__':
    init()
    while True:
        main()