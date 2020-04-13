import pygame
import random
pygame.init()
food_img=pygame.image.load(r'C:\Users\jagat\Desktop\food2.PNG')
snake_img=pygame.image.load(r'C:\Users\jagat\Desktop\snakeBody.PNG')
#snake_head=pygame.image.load(r'C:\Users\jagat\Desktop\snakehead.PNG')
#snake_head=pygame.transform.rotate(snake_head,180)
#colors
width=500
height=400
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
#Width and height of the game window
game_width=500
game_height=400
#Initializing game window
GameDisplay=pygame.display.set_mode((game_width,game_height))
#Game variables
font=pygame.font.SysFont(None,55)
def screen_score(text,color,x,y):
    screen_text=font.render(text,True,color)
    GameDisplay.blit(screen_text,[x,y])
def plot_snake(snake):
    #GameDisplay.blit(snake_head,snake[-1])
    for val in snake:
        GameDisplay.blit(snake_img,val)
def GameLoop():
    global snake_head
    score=0
    Collision=False
    GameExit=False
    snake_lst=[]
    snake_length=1
    snake_x=45
    snake_y=55
    directions=dict.fromkeys(['up','down','right','left'],False)
    snake_speedx=0
    snake_speedy=0
    fps=20
    clock=pygame.time.Clock()
    food_x=random.randint(100,game_width/2)
    food_y=random.randint(100,game_height/2)
        
    while not GameExit:
        if Collision:
            screen_score(f'Game Over!',red,140,100)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    GameExit=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        GameLoop()
        else:
            for event in  pygame.event.get():
                if event.type==pygame.QUIT:
                    GameExit=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT and directions['right']==False:
                        snake_speedx= -10
                        snake_speedy=0
                        directions['left']=True
                        directions['up']=False
                        directions['down']=False
                    if event.key==pygame.K_RIGHT and directions['left']==False:
                        snake_speedx= 10
                        snake_speedy=0
                        directions['right']=True
                        directions['up']=False
                        directions['down']=False
                    if event.key==pygame.K_UP and directions['down']==False:
                        snake_speedy= -10
                        snake_speedx=0
                        directions['up']=True
                        directions['left']=False
                        directions['right']=False
                    if event.key==pygame.K_DOWN and directions['up']==False:
                        snake_speedy= 10
                        snake_speedx=0
                        directions['down']=True
                        directions['left']=False
                        directions['right']=False
            if abs(snake_x-food_x)<12 and abs(snake_y-food_y)<12:
                score+=1
                snake_length+=1
                while True:
                    food_x=random.randint(100,game_width/2)
                    food_y=random.randint(100,game_height/2)
                    if [food_x,food_y]  in snake_lst :
                       food_x=random.randint(100,game_width/2)
                       food_y=random.randint(100,game_height/2)
                    else:
                        break
                
            snake_x+=snake_speedx
            snake_y+=snake_speedy
            if [snake_x,snake_y] in snake_lst[:-1]:
                Collision=True
            snake_lst.append([snake_x,snake_y])
            if len(snake_lst)>snake_length:
                del snake_lst[0]
            GameDisplay.fill(black)
            screen_score(f'Score:{score*10}',red,5,5)
            if snake_x<5 or snake_x>game_width-25 or snake_y<5 or snake_y>game_height-25:
                Collision=True
            GameDisplay.blit(food_img,(food_x,food_y))
            plot_snake(snake_lst)
        pygame.display.update()
        clock.tick(fps)
        

    pygame.quit()

GameLoop()