import random
import json
from setting import *


class Apple():
    #チェックポイント5
    #辞書型の方がvscodeで読み込みするときに補完されて楽だった
    #先頭のアンダースコアはカプセル化をする為のものだった？
    #アンダースコア一つの場合はクラス内部でしたか使用できなくなるが
    #インスタンス化したときアクセスできてしまう？
    #二つだとカプセル化の役目を果たせている?
    def __init__(self, json):
        self.__point: int = int(json['point'])
        self.image: str = 'img/{}'.format(json['image'])
        self.__down_speed: int = int(json['down_speed'])
        self.__spawn_rate: int = int(json['spawn_rate'])
        self.__damage_point: int = int(json['damage_point'])

        self.__pos_x:int = random.randint(0, 800)
        self.__pos_y:int = 0

    def fall(self) -> None:
        self.__pos_y += self.__down_speed

    def get_pos_y(self) -> int:
        """
        Name: get_pos_y
        Explain: リンゴのy座標を返す
        -------
        Returns:
        int: リンゴのy座標
        """
        return self.__pos_y

    def get_pos(self) -> int:
        """
        Name: get_pos
        Explain: リンゴのx座標とy座標を返す
        -------
        Returns:
        int: リンゴのx座標
        int: リンゴのy座標
        """
        return self.__pos_x, self.__pos_y

    def get_hit_box(self) -> int:
        """
        Name: get_hit_box
        Explain: リンゴのヒットボックスを返す
        -------
        Returns:
        int: リンゴのx座標のヒットボックス
        int: リンゴのy座標のヒットボックス
        """
        return self.__pos_x + 50, self.__pos_y

    def get_point(self) -> int:
        """
        Name: get_point
        Explain: リンゴのポイントを返す
        -------
        Returns:
        int: リンゴのポイント
        
        """
        return self.__point

    def get_damage_point(self) -> int:
        """
        Name: get_damage_point
        Explain: リンゴのダメージを返す
        -------
        Returns:
        int: リンゴのダメージ
        
        """
        return self.__damage_point

    def check_collision(self, player) -> bool:
        player_hit_box_left, player_hit_box_right = player.get_hit_box()
        apple_hit_box_x, apple_hit_box_y = self.get_hit_box()
        
        if (player_hit_box_left <= apple_hit_box_x <= player_hit_box_right
            and 480 > apple_hit_box_y >= 450):
            return True
        return False

    def check_reach_bottom(self) -> bool:
        pos_y = self.__pos_y
        if pos_y >= 500:
            return True
        return False

    #TODO クラスメソッドに関して勉強
    @classmethod
    def create_apple(cls):
        json_list_for_apple = cls.create_list_from_json(APPLE_JSON)
        return Apple(random.choice(json_list_for_apple))
        

    @classmethod
    #TODO open関数に関して勉強する
    def create_list_from_json(cls, json_file) -> list:
        with open(json_file) as file:
            jsn = json.load(file)
            return [jsn_val for jsn_val in jsn.values()]

    @classmethod
    def create_apples(cls):
        json_list_for_apple = cls.create_list_from_json(APPLE_JSON)
        return cls.create_random_apples_to_limit(json_list_for_apple)
    
    @classmethod
    def create_random_apples_to_limit(cls, json_list) -> list:
        return [Apple(random.choice(json_list)) for _ in range(MAX_APPLE_NUM)]





