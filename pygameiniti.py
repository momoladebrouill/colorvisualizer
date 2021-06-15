import pygame as pg
from turtle import Vec2D
from math import sqrt
from random import randrange,seed
from colorsys import hsv_to_rgb 
# Constantes :
FPS = 30  # les fps tabernak
WIND = (287,75) # dimentions de la fentere x y
seed() #planter la graine d'aletaioire
print("Déplacer le curseur avec les flèches")
print("Maintenir LSHIFT pour aller plus vite")
""" Rappels:
.---------------- + x
|
|
|
|
|
|
|
+ y
"""
pg.init()
f = pg.display.set_mode(size=WIND)
pg.display.set_caption("Color visualizer")
fpsClock = pg.time.Clock()
font = pg.font.SysFont('consolas', 75) #police//roxane
coul={"r":0x00,'v':0x00,"b":0x00}
selec=0 # selecteur dans la liste
optio=list(coul.keys()) # liste des keys
boucle = True
lutins=[]

try:
    while boucle:
        # Actualiser:
        pg.display.flip()

        # Appliquer les images de fond sur la fenetre
        s = pg.Surface(WIND)  # piqué sur stackoverflow pour avoir un fond avec un alpha
        s.set_alpha(255)
        s.fill((coul["r"], coul["v"], coul["b"]))
        f.blit(s, (0, 0))
        
        format(coul["r"],"02")
        text1 = font.render("#"+format(coul["r"],"02x")+\
                           format(coul["v"],"02x")+\
                           format(coul["b"],"02x"),
                           True, (255,255,255))
        f.blit(text1, (0,0))
        p = pg.key.get_pressed()
        if p[pg.K_LSHIFT] or p[pg.K_RSHIFT]:
            if p[pg.K_UP]:
                coul[optio[selec]]+=1
                if coul[optio[selec]] not in range(255):coul[optio[selec]]= coul[optio[selec]]%255
            elif p[pg.K_DOWN]:
                coul[optio[selec]]-=1
                if coul[optio[selec]] not in range(255):coul[optio[selec]]= coul[optio[selec]]%255
    
        for event in pg.event.get():  # QUAND la touche est appuyée
            if event.type == pg.QUIT:
                boucle = False
                print(" Fin du jeu  babe")
            elif event.type == pg.KEYDOWN:
                touche=event.dict['key']
                    
                if touche == pg.K_RIGHT:
                    selec+=1
                    if selec not in range(len(optio)):selec=selec%len(optio)
                if touche == pg.K_LEFT:
                    selec-=1
                    if selec not in range(len(optio)):selec=selec%len(optio)
                if touche == pg.K_UP:
                    coul[optio[selec]]+=1
                    if coul[optio[selec]] not in range(255):coul[optio[selec]]= coul[optio[selec]]%255
                if touche == pg.K_DOWN:
                    coul[optio[selec]]-=1
                    if coul[optio[selec]] not in range(255):coul[optio[selec]]= coul[optio[selec]]%255
                    
        if selec==0: triip=(255,0,0)
        elif selec==1: triip=(0,255,0)
        else: triip=(0,0,255)
        text2 = font.render(" "+"  "*(selec)+"__",False, triip)
        f.blit(text2, (0,0))

        fpsClock.tick(FPS)
except:
    pg.quit()
    raise
pg.quit()
