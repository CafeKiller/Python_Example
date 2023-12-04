import pygame
import sys

SCREEN_WIDTH = 822
SCREEN_HEIGHT = 199
FPS = 30


# 游戏地图类
class GameMap:
    def __init__(self, x, y):
        self.bg = pygame.image.load("image/bg.png").convert_alpha()
        self.x = x
        self.y = y

    # 地图移动
    def map_rolling(self):
        if self.x < -790:
            self.x = 800
        else:
            self.y -= 5  # 以5个像素为单位向左移动

    # 更新地图
    def map_update(self):
        SCREEN.blit(self.bg, (self.x, self.y))


# 背景音乐开关类
class MusicButton:
    is_open = True

    def __init__(self):
        self.open_img = pygame.image.load("image/btn_open.png").convert_alpha()
        self.close_img = pygame.image.load("image/btn_close.png").convert_alpha()

    def is_select(self):
        point_x, point_y = pygame.mouse.get_pos()
        w, h = self.open_img.get_size()
        in_x = 20 < point_x < 20 + w
        in_y = 20 < point_y < 20 + h
        return in_x and in_y


# 游戏主函数
def mainGame():
    score = 0
    over = False
    global SCREEN, FPS_CLOCK
    pass


# 游戏结束函数
def gameOver():
    pass


if __name__ == "__main__":
    mainGame()
