import main
import pygame
import time
import Inicial

Inicial.mostrarInicio(True)

#Se toman las coordenadas que están en el main
coordenadaPuerta= main.run1()
for i in range(len(coordenadaPuerta)):
    for j in range(len(coordenadaPuerta[0])):
        if(coordenadaPuerta[i][j]==4):
            coorX=i*100
            coorY=j*100

# Lista con coordenadas para llegar a la llave
recorrido = main.run()

#Lista con coordenadas para llegar a la puerta
recorridoPuerta=main.run2()

pygame.init()

pygame.display.set_caption("The Legend Of Zelda")

#El tamaño se ajusta al tamaño de los datos leídos desde el txt,
#para crear en la impresión una representación real de los datos (Link, Muros, Suelo, y demás)
width=len(main.matrizInterfaz)
height=len(main.matrizInterfaz[0])

#width*100 y height*100 -> se multiplica por 100 dado a que las imágenes son de dicha dimensión
#y lo que se pretende es una representación visual del archivo de texto
pantalla = pygame.display.set_mode((height*100,width*100))

#Variables para cada imagen respecto al personaje en carpeta
verde = 0
muro = 1
llave = 2
ganon = 3
puerta = 4
link = 5

#Inicio contadorJ en -100 para que la posición inicial sea 0
contadorJ=-100
contadorI=0

x=0
y=0
#Impresión en pantalla de matriz del txt
for i in range(width):
    for j in range(height):
        print(main.matrizInterfaz[i][j],end='')
    print()

# Imágenes utilizadas
Link= pygame.transform.scale( pygame.image.load("./Imagenes/linkFrontal.png"), (70, 70) )
enemigo=pygame.transform.scale( pygame.image.load("./Imagenes/ganon.png").convert_alpha(), (100, 100) )
suelo= pygame.transform.scale( pygame.image.load("./Imagenes/grass.png").convert_alpha(), (100, 100))
escudo=pygame.transform.scale( pygame.image.load("./Imagenes/sword.png").convert_alpha(), (100, 100) )
portal= pygame.transform.scale( pygame.image.load("./Imagenes/portal.png"), (100, 100))
up= pygame.transform.scale( pygame.image.load("./Imagenes/up.png"), (70, 70) )
rigth= pygame.transform.scale( pygame.image.load("./Imagenes/linkDer.png"),(70, 70) )
left= pygame.transform.scale( pygame.image.load("./Imagenes/linkIzq.png"), (70, 70) )
down= pygame.transform.scale( pygame.image.load("./Imagenes/linkFrontal.png"), (70, 70))
roca=pygame.transform.scale( pygame.image.load("./Imagenes/wall.png"), (100, 100) )
transformado=pygame.transform.scale( pygame.image.load("./Imagenes/linkFrontal.png"), (70, 70))

#Representación de los datos del txt de manera visual
for i in range(width):
    #Para continuar con cada posición durante la impresión en pantalla
    contadorI=0
    contadorJ+=100
    for j in range(height):
        #Imprimo el personaje según el número del txt
        if main.matrizInterfaz[i][j]==verde:
            imagen=suelo
            pantalla.blit(imagen,(contadorI,contadorJ))
            contadorI+=100

        if main.matrizInterfaz[i][j]==muro:
            imagen=roca
            pantalla.blit(imagen,(contadorI,contadorJ))
            contadorI+=100

        if main.matrizInterfaz[i][j]==llave:
            imagen=escudo
            pantalla.blit(imagen,(contadorI,contadorJ))
            contadorI+=100
            
        if main.matrizInterfaz[i][j]==ganon:
            imagen=enemigo
            pantalla.blit(imagen,(contadorI,contadorJ))
            contadorI+=100

        if main.matrizInterfaz[i][j]==puerta:
            imagen=portal
            pantalla.blit(imagen,(contadorI,contadorJ))
            contadorI+=100

        if main.matrizInterfaz[i][j]==link:
            imagen=suelo
            pantalla.blit(imagen, (contadorI,contadorJ)) 
            y=contadorI
            x=contadorJ
            contadorI+=100

# actualiza la pantalla
pygame.display.flip()
#Para actualizar la pantalla
pygame.display.update()

#k permite la sucesión de datos de una lista de coordenadas
#a seguir para llegar a cada meta (llave y puerta)
k=0  

#Para la reproducción de música
reloj = pygame.time.Clock()
 
#Carga de audio (.mp3) correspondiente al sonido de
#fondo del juego Legend Of Zelda
pygame.mixer.music.load("./Sonido/TLOF.mp3")
pygame.mixer.music.play(5)

#Para la impresión del primer link
contador=0

#Bucle infinito
while True:
    
    #se recorre la lista del main que representa los valores tanto de x como de y
    #que mejor resulten para llegar a la meta (llaves)
    if k<=len(recorrido)-2:

        time.sleep(0.3)
        #Dado a que en l lista recorrido los valores aparecen 1ro de x, 2do de y
        #3ro de x ... y así sucesivamente
        contadorJ=recorrido[k]
        contadorI=recorrido[k+1]
        #le sumo dos para no repetir valores
        k+=2

        #Impresión del seguimiento de los pasos de Link 
        if(contador==0):
            pantalla.blit(suelo,(y*100,x*100))
            pantalla.blit(Link,((contadorI*100)+20,(contadorJ*100)+20))
            contador+=1
        else:
            if(contadorJ>x):
                pantalla.blit(suelo,(y*100,x*100))
                pantalla.blit(down,((contadorI*100)+20,(contadorJ*100)+20))
            if(contadorJ<x):
                pantalla.blit(suelo,(y*100,x*100))
                pantalla.blit(up,((contadorI*100)+20,(contadorJ*100)+20))
            if(contadorI>y):
                pantalla.blit(suelo,(y*100,x*100))
                pantalla.blit(rigth,((contadorI*100)+20,(contadorJ*100)+20))
            if(contadorI<y):
                pantalla.blit(suelo,(y*100,x*100))
                pantalla.blit(left,((contadorI*100)+20,(contadorJ*100)+20))

        pygame.display.flip()
        #Retorna un solo evento de la cola de eventos
        pygame.display.update()
        event = pygame.event.wait()

        x=contadorJ
        y=contadorI

        #Si se presiona el botón 'cerrar' de la ventana
        if event.type == pygame.QUIT:
            #Detiene la aplicación
            break
    else:
        #Impresión de Link en la posición de la llave
        pantalla.blit(suelo,(contadorI*100,contadorJ*100))
        pantalla.blit(transformado,((contadorI*100)+20,(contadorJ*100)+20))
        pantalla.blit(portal,(coorY,coorX))

        pygame.display.flip()
        #Retorna un solo evento de la cola de eventos
        pygame.display.update()
        event = pygame.event.wait()

        #Si se presiona el botón 'cerrar' de la ventana
        if event.type == pygame.QUIT:
            #Detiene la aplicación
            break
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.stop()
    reloj.tick(20)