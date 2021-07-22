from typing import Tuple


class entity:
    def __init__(self, x: int, y: int) -> None:
        self.__pos_x: int = x
        self.__pos_y: int = y

    def get_pos(self) -> Tuple:
        return self.__pos_x, self.__pos_y

    def get_pos_x(self) -> int:
        return self.__pos_x
    
    def get_pos_y(self) -> int:
        return self.__pos_y

    def get_hit_box(self) -> int:
        pass

    def set_pos_x(self, x):
        self.__pos_x = x
    
    def set_pos_y(self, y):
        self.__pos_y = y

    def print_test(self) -> None:
        print(self.__pos_x)