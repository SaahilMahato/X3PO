import pygame

pygame.init()
height, width = 600,800
white = (255,255,255)
black = (0,0,0)
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("X-3PO")

VA_img = pygame.image.load('Img/VA.png')
gameexit = False

string = ""
text = "Hello, " + string
reply = "I am listening.."


def message(msg,color,x,y,font):
    font = pygame.font.SysFont(None, font)
    screen_text = font.render(msg, True, color)
    display.blit(screen_text, [x,y])


while not gameexit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameexit =True
    display.fill(white)
    display.blit(VA_img,((width//2)-170, (height//2)-300))
    message("X-3PO", black, 330,350, 70)
    message(text, black, 300,420, 50)
    message(reply, black, 300,480, 60)
    pygame.display.update()

pygame.display.update()
pygame.quit()
quit()
