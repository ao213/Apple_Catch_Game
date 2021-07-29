from entities.entity import entity
from setting import MAX_HP

class Player(entity):

    def __init__(self):
        super().__init__(0, 500)
        #チェックポイント６
        #アンダースコアを２回先頭に使用することでサブクラスでの名前衝突を回避？？
        #アノテーションは。。。あれば分かりやすいのかな・・・？
        #知らんけど辞書型にハマってた俺が馬鹿みたくなってくるほど簡単なコンストラクタ
        self.__hp: int = MAX_HP
        self.__point: int = 0
        self.image: str = 'img/box.png'
        self.__hit_box_height: int = 30
        self.__hit_box_width: int = 90

    #チェックポイント７
    #タプルって定数のlistって考えて大丈夫かな？
    #普通に値を二つ返すのとタプルで返す違いとは？
    #関数アノテーションはあった方がいいのかな？
    def set_player_position(self, x: int) -> None:
        """
        Name: pos_x
        Explain: playerが画面外に出ないように値を制限
        -------
        Args:
        x (int): マウスのx座標
        """
        if x >= 800:
            self.set_pos_x(800)
        else:
            self.set_pos_x(x)

    def get_pos(self) -> int:
        """
        Name: get_pos
        Explain: 現在のplayer位置を返す
        -------
        Returns: 
        int: playerのx座標
        int: playerのy座標
        """
        x = self.get_pos_x()
        y = self.get_pos_y()
        return x, y

    def get_hp(self) -> int:
        """
        Name: get_hp
        Explain: playerのHPを返す
        -------
        Returns:
        int: playerのhp
        """
        return self.__hp

    def get_hit_box(self) -> int:
        """
        Name: get_hit_box
        Explain: playerの左右のヒットボックスを返す
        -------
        Returns:
        int: ヒットボックスの左座標
        int: ヒットボックスの右座標
        """
        x = self.get_pos_x()
        return x, x + self.__hit_box_width

    def get_point(self) -> int:
        """
        Name: get_point
        Explain: playerのポイントを返す
        -------
        Returns:
        int: playerのポイント
        """
        return self.__point

    def add_point(self, point: int) -> None:
        """
        Name: add_point
        Explain: 取得したポイントを加算する
        -------
        Args:
        point (int): 取得したポイント
        """
        self.__point += point

    def receive_damage(self, apple) -> None:
        """
        Name: receive_damage
        Explain: 受けたダメージを取得しplayerのHPを更新
        -------
        Args: 
        apple (Apple): Apple型のオブジェクト
        """
        self.__hp = self.__hp - apple.get_damage_point()
