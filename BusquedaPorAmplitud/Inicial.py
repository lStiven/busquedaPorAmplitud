import main
import sys, pygame
import time
from pygame.locals import *

#Clase de la primer imagen (la de ingreso) correspondiente 
#al juego The Legend Of Zelda
def mostrarInicio(b):
    if b:
        width=len(main.matrizInterfaz)
        height=len(main.matrizInterfaz[0])

        screen = pygame.display.set_mode((height*100, width*100))
            
        pygame.display.set_caption("The Legend Of Zelda")

        background_image = pygame.transform.scale( pygame.image.load('./Imagenes/Inicio.jpg'),(height*100, width*100))

        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

        screen.blit(background_image, (0, 0))
        pygame.display.flip()
        time.sleep(3)