import pygame
import sys
import time
import random
pygame.init()
game_over=False
screen=pygame.display.set_mode((500,500))
player1_pos=[300,350]
player2_pos=[100,350]
jumpCount=10
isJump=False
jumpCount2=10
isJump2=False
clock=pygame.time.Clock()
ch1=0
ch2=0
BG=pygame.image.load("data/BGI.jpg")
BG=pygame.transform.scale(BG,(500,500))
pygame.mixer.music.load("data/BG.wav") 
pygame.mixer.music.play(-1,0.0)
left=pygame.image.load("data/left.png")
left=pygame.transform.scale(left,(60,150))
jump=pygame.image.load("data/jump.png")
jump=pygame.transform.scale(jump,(60,150))
right=pygame.image.load("data/right.png")
right=pygame.transform.scale(right,(60,150))
stand=pygame.image.load("data/stand.png")
stand=pygame.transform.scale(stand,(60,150))
left2=pygame.image.load("data/left2.png")
left2=pygame.transform.scale(left2,(60,150))
jump2=pygame.image.load("data/jump2.png")
jump2=pygame.transform.scale(jump2,(60,150))
right2=pygame.image.load("data/right2.png")
right2=pygame.transform.scale(right2,(60,150))
stand2=pygame.image.load("data/stand2.png")
stand2=pygame.transform.scale(stand2,(60,150))
spit=pygame.image.load("data/spit-.png")
spit=pygame.transform.scale(spit,(30,30))
spit2=pygame.image.load("data/spit2.png")
spit2=pygame.transform.scale(spit2,(30,30))
jumpS=pygame.mixer.Sound("data/11.wav")
spitS=pygame.mixer.Sound("data/spitsound.wav")
hitS=pygame.mixer.Sound("data/hurt.wav")
won=pygame.mixer.Sound("data/win.wav")
player1_bombs=[]
player2_bombs=[]
hit1=0
hit2=0
myFont=pygame.font.SysFont("monospace",45)
label=myFont.render("RED",1,(255,0,0))
screen.blit(label,(0,0))


#function to draw both the characters
def draw(ch,x,y,ch2,x2,y2):
    label=myFont.render("RED",1,(255,0,0))
    screen.blit(label,(400,0))
    label1=myFont.render("BLUE",1,(0,0,255))
    screen.blit(label1,(0,0))
    pygame.draw.rect(screen,(255,0,0),[250+(hit1*50),50,(5-hit1)*50,20])
    pygame.draw.rect(screen,(0,0,255),[0,50,(5-hit2)*50,20])
    if ch==0:
        screen.blit(stand,[x,y])
    if ch==1:
        screen.blit(left,[x,y])
    if ch==2:
        screen.blit(right,[x,y])
    if ch==3:
        screen.blit(jump,[x,y])
    if ch2==0:
        screen.blit(stand2,[x2,y2])
    if ch2==1:
        screen.blit(left2,[x2,y2])
    if ch2==2:
        screen.blit(right2,[x2,y2])
    if ch2==3:
        screen.blit(jump2,[x2,y2])



#function to make the bullets moving horizontally
def updateB1(x):
    for i in x:
        if i[2]==1 :
            i[0]-=5
        if i[2]==2:
            i[0]+=5
        if i[2]==3:
            if i[3]==1:
               i[0]+=5
            if i[3]==2:
                i[0]-=5
        if i[0]<20 or i[0]>480:
            x.pop(0)


#function to draw the bullets
def drawB1(x):
    for i in x:
        if i[2]==1:
            screen.blit(spit2,[i[0],i[1]])
        if i[2]==2:
            screen.blit(spit,[i[0],i[1]])
        if i[2]==3:
            if i[3]==1:
                screen.blit(spit,[i[0],i[1]])
            if i[3]==2:
                screen.blit(spit2,[i[0],i[1]])   



#function to detect any collusion bw the players and the bullets
def coll(booms,player):
    for i in booms:
        if i[0]<player[0] and player[0]-i[0]<=20:
            if i[1]<player[1] and player[1]-i[1]<=20:
                booms.pop(0)
                return True
            if i[1]>player[1] and i[1]-player[1]<=150:
                booms.pop(0)
                return True
        if i[0]>player[0] and i[0]-player[0]<60:
            if i[1]<player[1] and player[1]-i[1]<=20:
                booms.pop(0)
                return True
            if i[1]>player[1] and i[1]-player[1]<=150:
                booms.pop(0)
                return True


#the main loop
while not game_over:

        #code for the moment of player1
        ch1=0
        ch11=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player1_pos[0]> 10: 
            player1_pos[0]-= 10
            ch1=1
        if keys[pygame.K_RIGHT] and player1_pos[0] < 450:
            ch1=2
            player1_pos[0]+= 10
        if not(isJump): 
            if keys[pygame.K_UP]:
                jumpS.play()
                isJump = True
        else:
            if jumpCount >= -10:
                ch1=3
                player1_pos[1]-= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = False
        if keys[pygame.K_KP1] and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            if keys[pygame.K_RIGHT]:
                ch11=1
            if keys[pygame.K_LEFT]:
                ch11=2
            if len(player1_bombs)<1:
                spitS.play()
                player1_bombs.append([player1_pos[0],player1_pos[1]+10,ch1,ch11])




        #code for the moment of player2
        ch2=0
        ch22=0
        if keys[pygame.K_a] and player2_pos[0]> 10: 
            player2_pos[0]-= 10
            ch2=1
        if keys[pygame.K_d] and player2_pos[0] < 450:
            ch2=2
            player2_pos[0]+= 10
        if not(isJump2): 
            if keys[pygame.K_w]:
                jumpS.play()
                isJump2 = True
        else:
            if jumpCount2 >= -10:
                ch2=3
                player2_pos[1]-= (jumpCount2 * abs(jumpCount2)) * 0.5
                jumpCount2 -= 1
            else: 
                jumpCount2 = 10
                isJump2=False
        if keys[pygame.K_f] and (keys[pygame.K_a] or keys[pygame.K_d]):
            if keys[pygame.K_d]:
                ch22=1
            if keys[pygame.K_a]:
                ch22=2
            if len(player2_bombs)<1:
                spitS.play()
                player2_bombs.append([player2_pos[0],player2_pos[1]+10,ch2,ch22])



        screen.fill((255,255,255))
        screen.blit(BG,[0,0])


        #to check if anyone was WON
        if hit2==6:
            won.play()
            label10=myFont.render("RED WINS",1,(255,0,0))
            screen.blit(label10,(200,200))
            if jumpCount >= -10:
                ch1=3
                player1_pos[1]-= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else: 
                jumpCount = 10
                isJump = True
            
        if hit1==6:
            won.play()
            label10=myFont.render("BLUE WINS",1,(0,0,255))
            screen.blit(label10,(200,200))
            if jumpCount2 >= -10:
                ch2=3
                player2_pos[1]-= (jumpCount2 * abs(jumpCount2)) * 0.5
                jumpCount2 -= 1
            else: 
                jumpCount2 = 10
                isJump2=True
        #calling the function to draw the characters
        draw(ch1,player1_pos[0],player1_pos[1],ch2,player2_pos[0],player2_pos[1])

        #calling the function to update the bombs
        updateB1(player1_bombs)
        updateB1(player2_bombs)

        #calling the function to draw the bombs
        drawB1(player1_bombs)
        drawB1(player2_bombs)

        clock.tick(20)
        pygame.display.update()


        #code to fine the life left in the players
        if coll(player1_bombs,player2_pos):
            hitS.play()
            if hit2<5:
                hit2+=1
            if hit2 >= 5:
                hit2+=1
                
               
        if coll(player2_bombs,player1_pos):
            hitS.play()
            if hit1<5:
                hit1+=1
            if hit1==5:
               hit1+=1
