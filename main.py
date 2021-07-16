import pygame
import pygame.image
import pygame.display
import numpy
import setting
import apple
import box
import move
import hud

fps_clock = pygame.time.Clock()



def main():
    pygame.init()
    apple.apple_list.load_apple()
    box.box_play.load_box()
    logo = pygame.image.load("img/fruit_apple.png")
    bg = pygame.image.load("img/apple_bg.jpg")
    hud_bg = pygame.image.load("img/hud.png")
    game_over_bg = pygame.image.load("img/GAME OVER.png")
    game_over_flag = False
    run = True 
    
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    screen_1 = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Apple_catch_game")



    while run:
        if game_over_flag:
            pygame.display.update()
            screen_1.fill((100,100,100))
            screen.blit(game_over_bg,(0,0))
        else:
            pygame.display.update()
            screen.fill((100,100,100))
            screen.blit(bg,(0,-300))
            screen.blit(hud_bg,(0,600))
            box.box_play.draw_box(screen)
            apple.apple_list.draw_apple(screen)
            hud.HUD.draw_hud(screen)
            print(setting.hp)
            if setting.hp <= 0:
                game_over_flag = True




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEMOTION:
                x,y = event.pos
                move.move.move_box(x,y)




if __name__ == '__main__':
    main()