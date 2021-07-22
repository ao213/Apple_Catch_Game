from setting import *
from entities.player import Player
from entities.apple import Apple
from view.screen import Screen

class GameController:
    def __init__(self):
        self.main_screen = Screen()
        self.player = Player()
        self.apples = Apple.create_apples()

    def apple_process(self):
        updated_apples = []
        for apple in self.apples:
            apple.fall()
            # プレイヤーと衝突した時、ポイントを加算する
            if apple.check_collision(self.player):
                self.player.add_point(apple.get_point())
                apple = Apple.create_apple()
            # 底に達した時のみ、ダメージ処理を行う
            if apple.check_reach_bottom():
                self.player.receive_damage(apple)
                apple = Apple.create_apple()
            updated_apples.append(apple)

        self.apples = updated_apples

    def set_player_postion(self, pos_x):
        self.player.set_player_position(pos_x)

    def check_game_over(self):
        hp = int(self.player.get_hp())
        if hp <= 0:
            self.display_game_over_screen()
            return True
        return False

    def display_objects(self):
        """画面に表示するオブジェクトを全て表示する
        """
        self.main_screen.draw_object(self.player)
        for apple in self.apples:
            self.main_screen.draw_object(apple)

    def display_base_screen(self):
        """ゲーム画面を表示する
        """
        self.main_screen.draw_base_screen()

    def display_hud(self):
        """HUDを表示する
        """
        self.main_screen.draw_hud(self.player)

    def display_game_over_screen(self):
        """ゲームオーバー画面を表示する
        """
        self.main_screen.draw_game_over_screen()
