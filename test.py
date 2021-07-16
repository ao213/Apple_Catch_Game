import pygame
import pygame.display
import pygame.event
import pygame.mouse
import pygame.draw
import numpy

def main():
    pygame.init()
    WIDTH = 300
    HEIGHT = 300
    CAPTION = "test"
    run = True
    HP = 50

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption(CAPTION)
    img = pygame.image.load("img/fuji.png")
    font = pygame.font.Font(None, 30)
    start_lien_x = 50
    start_line_y = 50

    end_line_x = 250
    end_line_y = 50


    while run:
        t_x,t_y = pygame.mouse.get_pos()
        hp_par =  numpy.round((t_x / 4) / HP,2)

        text_1 = font.render(str(int(t_x / 4)), True, (255,255,255))   
        text = font.render(str(hp_par), True, (255,255,255))

        line_x = end_line_x - int(end_line_x * hp_par)
        


        pygame.display.update()
        screen.fill((100,100,100))
        screen.blit(img,(0,0))
        screen.blit(text,(150,150))
        screen.blit(text_1,(270,270))

        pygame.draw.line(screen,(0,0,0),(start_lien_x,start_line_y),(line_x,end_line_y),10)
        

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEMOTION:
                x,y = event.pos


if __name__ == '__main__':
    main()