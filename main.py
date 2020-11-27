import pygame

#set up display

pygame.init()
WIDTH, HEIGHT = 800,500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangboy Game!")

# the button variables 
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH-(RADIUS*2+GAP)*13)/2)
starty = 400
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i%13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x,y])





#loading images 
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

#game variables
hangman_status = 0

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)






#setting up gameloop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)

    #draw buttons

    for letter in letters:
        x,y = letter
        pygame.draw.circle(win,BLACK, (x,y),RADIUS,3)


    win.blit(images[hangman_status],(150,100))
    pygame.display.update()



while run:
    clock.tick(FPS)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

            
pygame.quit()

