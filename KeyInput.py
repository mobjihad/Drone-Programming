import pygame

def start():

    pygame.init()
    window = pygame.display.set_mode((400,400))


def getKey(keyname):

    key = False

    for inputs in pygame.event.get(): pass
    keyinput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyname))

    if keyinput[myKey]:
        key = True
        pygame.display.update()


    return key

def main():

    if getKey("LEFT"):
        print("Left Key Pressed")
    if getKey("a"):
        print("A Pressed")

if __name__ == '__main__':

    start()
    while True:
        main()
