import pygame,math,random
pygame.init()
screen=pygame.display.set_mode((500,600))
pygame.display.set_caption("space shooter")
bg_image=pygame.image.load("bg2.jpg").convert()
player_image=pygame.image.load("s4.png").convert_alpha()
enemy_image=pygame.image.load("e4.png").convert_alpha()
#BLUE=(0,0,255)
#WHITE=(255,255,255)
player=pygame.Rect(200,200,30,30)
#enemy=pygame.Rect(50,120,30,30)
 
 
xvelocity=[]
yvelocity=[]
angle=0
change=0 
forward=0
distance=5
enemies=[]
enemycount=10

for i in range(enemycount):
    enemies.append(pygame.Rect(random.randint(0,500),random.randint(0,600),5,5))
    xvelocity.append(random.randint(-3, 3))
    yvelocity.append(random.randint(-3, 3))
def newxy(x,y,distance,angle):
    angle=math.radians(angle+90)
    xnew=x+(distance*math.cos(angle))
    ynew=y-(distance*math.sin(angle))
    return xnew,ynew        
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                change=6
            if event.key==pygame.K_RIGHT:
                change=-6
            if event.key==pygame.K_UP:
                forward=True
             
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                change=0
            if event.key==pygame.K_UP:
                forward=False
    i=0
    for enemy in enemies:
        enemy.x=enemy.x+xvelocity[i]
        enemy.y=enemy.y+yvelocity[i]    
        if enemy.x<-250 or enemy.x>600:
           xvelocity[i]=-1*xvelocity[i]
        if enemy.y<-250 or enemy.y>600:
           yvelocity[i]=-1*yvelocity[i]                
        i=i+1
        screen.blit(enemy_image,enemy)
   
    
    if forward:
        player.x,player.y=newxy(player.x, player.y, distance, angle)
    if player.x<0:
        player.x=500
    if player.x>500:
        player.x=0
    if player.y<0:
        player.y=600
    if player.y>600:
        player.y=0   
    angle=angle+change  
    new_image=pygame.transform.rotate(player_image,angle)
    screen.blit(bg_image,[0,0])  
    screen.blit(new_image,player)     
   # pygame.draw.rect(screen,BLUE,player)
    #pygame.draw.rect(screen,WHITE,enemy) 
     
    
    pygame.display.update()
    pygame.time.Clock().tick(30)