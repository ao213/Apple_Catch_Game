import setting
import apple
import random
import pygame
import box


class move:
    def move_apple(obj):
        if obj.pos_x == 0:
            obj.pos_x = random.randint(0,800)
        obj.pos_y += obj.down_speed

    def move_box(x,y):
        box = setting.boxs[0]
        if x >= 800:
            x = 800
            box["pos_x"] = x
        else:
            box["pos_x"] = x
        box["pos_y"] = 500
        
    def apple_hit_box(obj):
        box = setting.boxs[0]
        hit_box_left = box["pos_x"]
        hit_box_rigth = box["pos_x"] + box["hit_box_width"]

        hit_apple_x = obj.pos_x + 50
        hit_apple_y = obj.pos_y + obj.bottom_top

        if hit_box_left <= hit_apple_x <= hit_box_rigth and 580 > hit_apple_y >= 550:
            setting.point += obj.point
            return True


