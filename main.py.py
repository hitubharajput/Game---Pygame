import pygame
import random
import os


#--------------------------------------------------------------------------------------------------------
# for initialize all function of pygame : 
pygame.init()
# for initialize music function :
pygame.mixer.init() 
# for initialize text function :
pygame.font.init()


# RGB(red,green,blue) color code :
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0,255,0)
yellow=(255,255,0)

# function  : helps to write text on game window                          
def text_screen(text, color, x, y):
    screen_text = font.render(text,True, color) 
     # Most important function to blit the text on the screen
    gameWindow.blit(screen_text, [x,y])

# width and hight of game window
screen_width = 600
screen_height = 600
# crate a game window
gameWindow = pygame.display.set_mode((screen_width, screen_height))


# tab Title
pygame.display.set_caption("SnakeAndSnacks")
# most important : after do all necessary thing for display must update display
pygame.display.update()

# FPS : frame per second (smoothness of game)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30) 

# plot snake on the game window
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

        
def welcome():
    
    pygame.mixer.music.load('ws.mp3.mp3')
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:
        # add image on window
        bgimg = pygame.image.load("main.jpg")
        bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
        gameWindow.blit(bgimg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('move.mp3.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)

# Main body  : All Game control
def gameloop():
# Game specific variables
    exit_game = False
    game_over = False
    # snake intial postion in window :
    snake_x = 70
    snake_y = 70
    #snake velocity in x and y direction(intial velocity) :
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    # intial snake length
    snk_length = 1
    # food intial in game window correspond to screen width and hight :
    food_x = random.randint(50,500)
    food_y = random.randint(50,500)
    # intial score of player :
    score = 0
    # initial velocity :
    snake_velocity = 5
    # initial snake size
    snake_size = 10
    fps = 30
    temp = 0 
  # existancy of hiscore file :
    if(not os.path.exists("hiscore.txt")) :
           with open("hiscore.txt","w") as f :
               f.write("0")

    # for display hiscore : 
    with open("hiscore.txt","r") as f :
        hiscore = f.read()
    while not exit_game:
        if game_over:
     # for display hiscore : 
            with open("hiscore.txt","w") as f :
                    f.write(str(hiscore))
            gameWindow.fill(white)
            # for add image on window
            bgimg = pygame.image.load("second.jpg")
            bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score : "+ str(score) +"            Hiscore : "   +str(hiscore), yellow, 300, 535)
     # game exit 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
     # restart game or replay after quit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                  # if gamer press any keys 
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.music.load('m2.mp3.mp3')
                    pygame.mixer.music.play()
                  # if gamer press right arrow  key
                    if event.key == pygame.K_RIGHT:
                        
                        velocity_x = snake_velocity
                        velocity_y = 0
                        
                        
                  # if gamer press left arrow  key
                    if event.key == pygame.K_LEFT:
                        velocity_x = - snake_velocity
                        velocity_y = 0
                        
                  # if gamer press up arrow  key
                    if event.key == pygame.K_UP:
                        velocity_y = - snake_velocity
                        velocity_x = 0
                       
                  # if gamer press down arrow  key
                    if event.key == pygame.K_DOWN:
                        velocity_y = snake_velocity
                        velocity_x = 0
                      
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y


            # increase score when snake ate food
               # here most important is abs function
            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10 :
                pygame.mixer.music.load('score.mp3.mp3')
                pygame.mixer.music.play()
                score +=200
                food_x = random.randint(80,500)
                food_y = random.randint(80,500)
                snk_length +=2
              # for store hiscore in file : 
                if score>int(hiscore) :
                   hiscore = score
                   pygame.mixer.music.load('ah.mp3.wav')
                   pygame.mixer.music.play() 
                   
            bgimg = pygame.image.load("third.jpg")
            bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score : "+ str(score) +"            Hiscore : "   +str(hiscore), green, 150, 15)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            # snake head :
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            # delete firts element of the game 

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('death.mp3.mp3')
                pygame.mixer.music.play()
            # game over 
            if snake_x<50 or snake_x>550 or snake_y<50 or snake_y>550:
                game_over = True
                pygame.mixer.music.load('death.mp3.mp3')
                pygame.mixer.music.play()
              
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
# game end point
    pygame.quit()
    quit()
# game start point
welcome()
