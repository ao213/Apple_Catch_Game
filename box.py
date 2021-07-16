import pygame
import move
import setting

class Box:

    def __init__(self,stats):
        self.name = stats['name']
        self.pos_x = stats['pos_x']
        self.pos_y = stats['pos_y']
        self.dir = stats['dir']
        self.hit_box_heigth = stats['hit_box_heigth']
        self.hit_box_width = stats['hit_box_width']

class box_play:

    def load_box():
        setting.boxs.append(
            {
                "name":"No.1",
                "pos_x":0,
                "pos_y":0,
                "dir":"img/box.png",
                "hit_box_heigth": 30,
                "hit_box_width":90,
            }
        )

    def create_box():
        box = Box(setting.boxs[0])
        return box

    def draw_box(screen):
        box = box_play.create_box()
        box_img = pygame.image.load(box.dir)
        screen.blit(box_img,(box.pos_x,box.pos_y))



    