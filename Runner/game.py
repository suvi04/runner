import random
from tkinter import font
import time
import pygame
import sys
screen=pygame.display.set_mode((1000,600))
pygame.init()
clock=pygame.time.Clock()
font_type=pygame.font.Font("/home/suvansh/Documents/py projects/Py_game/Runner/font/SuperMario256.ttf",50)
gravity=0
score=0
game_active=True

#########     SURFACES     ##########
sky_surf=pygame.image.load("Py_game/Runner/gfx/sky.png").convert_alpha()
ground_surf=pygame.image.load("Py_game/Runner/gfx/ground.png").convert_alpha()
fly_surf=pygame.image.load("Py_game/Runner/gfx/fly.png").convert_alpha()
fly_surf=pygame.transform.rotozoom(fly_surf,0,1.5)
enemy_surf=pygame.image.load("Py_game/Runner/gfx/enemy.png").convert_alpha()
enemy_surf=pygame.transform.rotozoom(enemy_surf,0,0.45)
turtle_surf=pygame.image.load("Py_game/Runner/gfx/turtle.png").convert_alpha()
turtle_surf=pygame.transform.rotozoom(turtle_surf,0,1.2)
player_surf=pygame.image.load("Py_game/Runner/gfx/player.png").convert_alpha()
game_over_surf=font_type.render("You lost!",True,"white")



#########     RECTANGLES     ##########
sky_rect=sky_surf.get_rect(topleft=(0,0))
ground_rect=ground_surf.get_rect(topleft=(0,400))
fly_rect=fly_surf.get_rect(center=(800,150))
enemy_rect=enemy_surf.get_rect(bottomleft=(900,420))
turtle_rect=turtle_surf.get_rect(bottomleft=(800,420))
player_rect=player_surf.get_rect(bottomleft=(50,420))
game_over_rect=game_over_surf.get_rect(center=(500,400))


while True:
    game_active=True
    score_surf=font_type.render("Score : "+str(round(score,0)),True,"black")
    score_rect=score_surf.get_rect(center=(500,80))

    score+=0.2
    keys=pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    if game_active==True:
        keys=pygame.key.get_pressed()

        gravity+=1

    #######     BLIT     ######   
        screen.blit(sky_surf,sky_rect)
        screen.blit(ground_surf,ground_rect)
        screen.blit(fly_surf,fly_rect)
        screen.blit(enemy_surf,enemy_rect)
        screen.blit(turtle_surf,turtle_rect)
        screen.blit(player_surf,player_rect)
        screen.blit(score_surf,score_rect)

    ######      MOTION      #########
        turtle_rect.x-=2.6
        if turtle_rect.x<-20:
            turtle_rect.x=1080
        enemy_rect.x-=2.9
        if enemy_rect.x<-30:
            enemy_rect.x=1200
            score+=12
        fly_rect.x-=4
        if fly_rect.x<-40:
            fly_rect.x=1000
            fly_rect.y=150
        player_rect.y+=gravity
        keys=pygame.key.get_pressed()
        if player_rect.y>=340:
            player_rect.y=340
            if keys[pygame.K_SPACE]:
                        gravity=-26
            if keys[pygame.K_LCTRL]:
                        gravity=-20    
        if keys[pygame.K_LEFT]:
            player_rect.x-=4
        if keys[pygame.K_RIGHT]:
            player_rect.x+=4
        
    #########       GAMEOVER        ########
        if player_rect.colliderect(turtle_rect) or player_rect.colliderect(fly_rect) or player_rect.colliderect(enemy_rect):
            game_active=False
            score=0
        

    if game_active==False:
        screen.fill((201, 148, 227))
        screen.blit(game_over_surf,game_over_rect)
        pygame.display.update()
        fly_rect.x=1000
        fly_rect.y=200
        enemy_rect.x=1200
        turtle_rect.x=1080
        player_rect.x=20
        player_rect.y=30
        time.sleep(0.9)
        pygame.display.update()

    ###### SPEEDING UP  ######
    fly_rect.x-=0.1
    enemy_rect.x-=0.1
    turtle_rect.x-=0.1
        





    pygame.display.update()
    clock.tick(60)