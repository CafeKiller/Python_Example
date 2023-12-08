import random

import pygame
import sys
from itertools import cycle

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


# 玩家对象
class Marie:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.jump_state = False
        self.jump_height = 130
        self.lowest_y = 140
        self.jump_value = 0
        self.marie_index = 0
        self.marie_index_gen = cycle([0, 1, 2])

        self.adventure_img = (
            pygame.image.load("image/adventure1.png").convert_alpha(),
            pygame.image.load("image/adventure2.png").convert_alpha(),
            pygame.image.load("image/adventure3.png").convert_alpha(),
        )
        # self.jump_audio = pygame.mixer.Sound()
        self.rect.size = self.adventure_img[0].get_size()
        self.x = 50
        self.y = self.lowest_y
        self.rect.top_left = (self.x, self.y)

    # 跳跃
    def jump(self):
        self.jump_state = True

    # 移动
    def move(self):
        if self.jump_state:
            if self.rect.y >= self.lowest_y:
                self.jump_value = -5
            if self.rect.y <= self.lowest_y - self.jump_height:
                self.jump_value = 5

            self.rect.y += self.jump_value
            if self.rect.y >= self.lowest_y:
                self.jump_state = False

    def draw_marie(self):
        marie_index = next(self.marie_index_gen)
        SCREEN.blit(self.adventure_img[marie_index], (self.x, self.rect.y))


# 障碍物类
class Obstacle:
    score = 1
    move = 5
    obstacle_y = 150

    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.missile = pygame.image.load("image/missile.png").convert_alpha()
        self.pipe = pygame.image.load("image/pipe.png").convert_alpha()
        self.numbers = (
            pygame.image.load("image/0.png").convert_alpha(),
            pygame.image.load("image/1.png").convert_alpha(),
            pygame.image.load("image/2.png").convert_alpha(),
            pygame.image.load("image/3.png").convert_alpha(),
            pygame.image.load("image/4.png").convert_alpha(),
            pygame.image.load("image/5.png").convert_alpha(),
            pygame.image.load("image/6.png").convert_alpha(),
            pygame.image.load("image/7.png").convert_alpha(),
            pygame.image.load("image/8.png").convert_alpha(),
            pygame.image.load("image/9.png").convert_alpha(),
        )
        # self.score_audio = pygame.mixer.Sound()
        r = random.randint(0, 1)
        if r == 0:
            self.image = self.missile
            self.move = 15
            self.obstacle_y = 100
        else:
            self.image = self.pipe
        self.rect.size = self.image.get_size()
        self.width, self.height = self.rect.size
        self.x = 800
        self.y = self.obstacle_y
        self.rect.center = (self.x, self.y)

    def obstacle_move(self):
        self.rect.x = self.move

    def draw_obstacle(self):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))


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
