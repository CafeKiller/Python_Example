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

    def get_score(self):
        self.score
        tmp = self.score
        if tmp == 1:
            pass
        self.score = 0
        return tmp

    def show_score(self, score):
        self.score_digits = [int(x) for x in list(str(score))]
        total_width = 0
        for digit in self.score_digits:
            total_width += self.numbers[digit].get_width()
        x_offset = (SCREEN_WIDTH - (total_width + 30))
        for digit in self.score_digits:
            SCREEN.blit(self.numbers[digit], (x_offset, SCREEN_HEIGHT * 0.1))
            x_offset += self.numbers[digit].get_width()


# 游戏主函数
def mainGame():
    score = 0
    over = False
    global SCREEN, FPS_CLOCK
    pygame.init()

    FPS_CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("玛丽大冒险")

    bg1 = GameMap(0, 0)
    bg2 = GameMap(800, 0)

    marie = Marie()

    add_obstacle_timer = 0
    list = []

    # music_button = MusicButton()
    # btn_img = music_button.open_img
    # music_button.bg_music.play(-1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                # if music_button.is_open:
                #     btn_img = music_button.close_img
                #     music_button.is_open = False
                #     music_button.bg_music.stop()
                # else:
                #     btn_img = music_button.open_img
                #     music_button.is_open = True
                #     music_button.bg_music.play(-1)
                pass
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if marie.rect.y >= marie.lowest_y:
                    marie.jump()
                if over:
                    mainGame()

        if not over:

            bg1.map_update()
            bg1.map_rolling()

            bg2.map_update()
            bg2.map_rolling()

            marie.move()
            marie.draw_marie()

            if add_obstacle_timer >= 1300:
                r = random.randint(0, 100)
                if r > 40:
                    obstacle = Obstacle()
                    list.append(obstacle)
                add_obstacle_timer = 0

            for i in range(len(list)):
                list[i].obstacle_move()
                list[i].draw_obstacle()

                if pygame.sprite.collide_rect(marie, list[i]):
                    over = True
                    gameOver()
                else:
                    if (list[i].rect.x + list[i].rect.width) < marie.rect.x:
                        score += list[i].get_score()
                list[i].show_score(score)

        add_obstacle_timer += 20
        # SCREEN.blit(btn_img, (20, 20))
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


# 游戏结束函数
def gameOver():
    # bump_audio = pygame.mixer.Sound
    # bump_audio.play()
    screen_w = pygame.display.Info().current_w
    screen_h = pygame.display.Info().current_h
    over_img = pygame.image.load("image/gameover.png").convert_alpha()
    SCREEN.blit(over_img, ((screen_w - over_img.get_size()) / 2, (screen_h - over_img.get_height()) / 2))


if __name__ == "__main__":
    mainGame()
