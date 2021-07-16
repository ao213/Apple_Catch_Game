from hud import HUD
from move import move
import random
import pygame
import setting

class apple_list:

    def load_apple():
        #ふじ
        setting.apples.append(
            {
                "name" : 'fuji_apple',
                "down_speed":1,
                "point":1,
                "spawn_rate":10,
                "dir":'img/fuji.png',
                "pos_x":0,
                "pos_y":0,
                "bottom_top":100,
                "dmg_point":1,
            }
        )

        #王林
        setting.apples.append(
            {
                "name" : 'ourin_apple',
                "down_speed":0.6,
                "point":2,
                "spawn_rate":10,
                "dir":'img/ourin.png',
                "pos_x":0,
                "pos_y":0,
                "bottom_top":100,
                "dmg_point":5,
                
            }
        )

        #青り４号
        setting.apples.append(
            {
                "name" : 'aori4gou_apple',
                "down_speed":3,
                "point":5,
                "spawn_rate":10,
                "dir":'img/aori4gou.png',
                "pos_x":0,
                "pos_y":0,
                "bottom_top":100,
                "dmg_point":10,

            }
        )

    def choice_apple():
        down_apple =  random.choice(setting.apples)
        return down_apple
    
    def create_apple_list():
        if len(setting.screen_apple_list) <= setting.max_apple:
            
            if setting.screen_apple_list[0] == 0:
                for i in range(setting.max_apple):
                    setting.screen_apple_list[i] = apple(apple_list.choice_apple())
            elif len(setting.screen_apple_list) < setting.max_apple:
                setting.screen_apple_list.append(apple(apple_list.choice_apple()))

        return setting.screen_apple_list

    def draw_apple(screen):
        screen_in_apple = apple_list.create_apple_list()

        for obj in screen_in_apple:
            apple_img = pygame.image.load(obj.dir)
            move.move_apple(obj)
            if obj.pos_y + obj.bottom_top >= 600 or move.apple_hit_box(obj):
                setting.screen_apple_list.remove(obj)
                if obj.pos_y + obj.bottom_top >= 600:
                    HUD.dmg_calc(obj)
            screen.blit(apple_img,(obj.pos_x,obj.pos_y))




class apple:
    def __init__(self,stats):
        self.name = stats['name']
        self.point = stats['point']
        self.dir = stats['dir']
        self.pos_x = stats['pos_x']
        self.pos_y = stats['pos_y']
        self.down_speed = stats['down_speed']
        self.bottom_top = stats['bottom_top']
        self.dmg_point = stats['dmg_point']
    




