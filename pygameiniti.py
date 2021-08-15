import pygame as pg

from colorsys import hsv_to_rgb 

FPS = 30  
WIND = (287,75) 

print("Déplacer le curseur avec les flèches")
print("Maintenir SHIFT pour aller plus vite")

pg.init()
f = pg.display.set_mode(WIND,pg.RESIZABLE)
pg.display.set_caption("Color visualizer")
fpsClock = pg.time.Clock()
font = pg.font.SysFont('consolas', 75) #police//roxane
coul={"r":0x00,'v':0x00,"b":0x00}
selec=0 # selecteur dans la liste
optio=list(coul.keys()) # liste des keys
boucle = True
p={}

try:
    while boucle:
        pg.display.flip()

        f.fill((coul["r"], coul["v"], coul["b"]))
        
        format(coul["r"],"02")
        text1 = font.render("#"+format(coul["r"],"02x")+\
                           format(coul["v"],"02x")+\
                           format(coul["b"],"02x"),
                           True, (255,255,255))

        if p.get(pg.K_LSHIFT) or p.get(pg.K_RSHIFT):
            if p.get(pg.K_UP):
                coul[optio[selec]]+=1
                if coul[optio[selec]] not in range(255):coul[optio[selec]]= coul[optio[selec]]%255
            elif p.get(pg.K_DOWN):
                coul[optio[selec]]-=1
                if coul[optio[selec]] not in range(255):coul[optio[selec]]= coul[optio[selec]]%255
    
        for event in pg.event.get():  # QUAND la touche est appuyée
            if event.type == pg.QUIT:
                boucle = False
                print(" Fin du jeu  babe")
            elif event.type == pg.KEYDOWN:
                touche=event.dict['key']
                p[touche]=True
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
            elif event.type==pg.KEYUP:
                p[touche]=False
            elif event.type==pg.VIDEORESIZE:
                WIND=(event.w,event.h)
                    
        if selec==0: triip=(255,0,0)
        elif selec==1: triip=(0,255,0)
        else: triip=(0,0,255)
        text2 = font.render(" "+"  "*(selec)+"__",False, triip)
        text_rect=text1.get_rect()
        pos=(WIND[0]/2-text_rect.w/2,WIND[1]/2-text_rect.h/2)
        f.blit(text1, pos)
        f.blit(text2, pos)

        fpsClock.tick(FPS)
except:
    pg.quit()
    raise
pg.quit()
