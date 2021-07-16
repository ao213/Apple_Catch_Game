from numpy.lib.function_base import select
import pygame
import pygame.font
import pygame.display
import pygame.draw
import apple
import setting
import numpy

class HUD:
    def __init__(self):
        self.hp = setting.hp
        self.point = setting.point
        self.font = pygame.font.Font(None,100)
        self.text_color = (127,195,156)
        self.line_x = setting.line_x
        

    def select_x(x):
        if x < 10:
            return 170
        elif x < 100:
            return 150
        elif x < 1000:
            return 130
        else:
            return 140

        
    def dmg_calc(obj):
        hud = HUD()
        setting.hp = setting.hp - obj.dmg_point
        hp_par = numpy.round(setting.hp / setting.HP,2)
        setting.line_x = int(setting.line * hp_par)
        
    
    def draw_hud(screen):
        hud = HUD()
        font = hud.font
        text_x = 0

        start_lien_x = 27
        line_y = 636
        end_line_x = hud.line_x
        if end_line_x <= start_lien_x:
            end_line_x = 28
        else:
            end_line_x = hud.line_x
        text_x = HUD.select_x(hud.point)

        text = font.render(str(hud.point), True, hud.text_color)    
        screen.blit(text,(text_x,700))
        pygame.draw.line(screen,hud.text_color,(start_lien_x,line_y),(end_line_x,line_y),20)
        



