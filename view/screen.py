import numpy as np
import pygame
from entities.player import Player

from setting import *

class Screen:
    
    def __init__(self):
        #画像読み込み
        logo = pygame.image.load(LOGO_PATH)
        self.bg = pygame.image.load(BG_PATH)
        self.hud_bg = pygame.image.load(HUD_BG_PATH)
        self.gameover_bg = pygame.image.load(GAMEOVER_BG_PATH)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        #HUD設定
        self.font = pygame.font.Font(None, 100)
        self.text_color = HUD_TEXT_COLOR
        #チェックポイント_1
        #LINE_Xを定数としてsettingに持たせる必要はるのか？？
        #ただ、最大値を参照するメソッドがあるので必要だとは思うが...
        self.line_x = LINE_X 
        #self.line_x = 873
        
        pygame.display.set_icon(logo)
        pygame.display.set_caption(CAPTION)

    def draw_object(self, Object):
        """
        Name: draw_object
        Explain: 引数で渡されたオブジェクトの描画
        -------
        Args:

        Object (Object): 描画するためのオブジェクトクラス
        -------
        Returns:

        -------
        note:
        """
        #チャックポイント3,4
        #変数imageの名前の付け方はimgでも良いのでは？PEP8で略して書くのは大丈夫なはず
        #ただ、比較的分かりやすい、英語スペルの勉強になるから略さずに書くほうが良いのかな？
        #画像の読み込みで変数を直接参照してるがget_imageってメソッドを作って返すのはどうか？
        #メソッドを書く手間がかかるだけなのか？他にも直接参照する利点があるなら知りたい
        image = pygame.image.load(Object.image)
        #img = pygame.image.load(Object.image)
        self.screen.blit(image, Object.get_pos())


    def draw_base_screen(self):
        """
        Name: draw_base_screen
        Explain: 基本となるBG,HUDのBGを描画
        """
        self.screen.fill((100, 100, 100))
        self.screen.blit(self.bg,(0, -300))
        self.screen.blit(self.hud_bg, (0, 600))

    def draw_hud(self, player):
        """
        Name: draw_hud
        Explain: HUDの体力ゲージ、ポイント数の描画
        """
        #start_line_xやline_yを定数としてsettingに持たせるのはありか？
        #ただ、HUDの要素だから持たせる必要はないと思うけど。。。
        #チェックポイント_2
        start_lien_x = 27
        line_y = 636
        hp_par = np.round(player.get_hp() / MAX_HP, 2)
        end_lien_x = int(LINE_X * hp_par)
        if end_lien_x <= start_lien_x:
            end_lien_x = 28
        text_x = self.select_x(player.get_point())

        text = self.font.render(str(player.get_point()), True, self.text_color)
        self.screen.blit(text, (text_x, 700))
        pygame.draw.line(self.screen, self.text_color, 
                        (start_lien_x, line_y), (end_lien_x, line_y), 20)

    def draw_game_over_screen(self):
        """
        Name: draw_gameover_screen
        Explain: ゲーム終了後の画面を描画
        """
        self.screen.fill((100, 100, 100))
        self.screen.blit(self.gameover_bg, (0, 0))
        

    def select_x(self, x):
        """
        Name: draw_gameover_screen
        Explain: HUDのポイントの描画位置Xを桁数に応じて変更
        -------
        Args:
        x (int): 現在のポイント数

        -------
        Returns:
        int : ポイントのXの描画位置
        
        """

        if x < 10:
            return 170
        elif x < 100:
            return 150
        elif x < 1000:
            return 130
        else:
            return 140








