import codecs

import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800


# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.mid_bottom = init_pos
        self.speed = 10

    def move(self):
        self.rect.top -= self.speed


class Player(pygame.sprite.Sprite):
    def __init__(self, player_rect, init_pos):
        pygame.sprite.Sprite.__init__(self)
        for i in range(len(player_rect)):
            self.image.append(player_rect[i].convert_alpha())

        self.rect = player_rect[0].get_rect()
        self.rect.top_left = init_pos
        self.speed = 8
        self.bullets = pygame.sprite.Group()
        self.img_index = 0
        self.is_hit = False

    # 发射子弹
    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)

    # 向上移动(需要判定边界)
    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    # 向下移动(需要判定边界)
    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    # 向左移动
    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    # 向右移动
    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_down_imgs, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 2
        self.down_index = 0

    def move(self):
        self.rect.top += self.speed


# 写入文件
def write_txt(content, strim, path):
    f = codecs.open(path, strim, 'utf8')
    f.write(str(content))
    f.close()


# 初始化
pygame.init()
screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.set_caption("简易版飞机大战")
ic_launcher = pygame.image.load("image/ic_launcher.png").convert_alpha()
pygame.display.set_icon(ic_launcher)
background = pygame.image.load("image/background.png").convert_alpha()
game_over = pygame.image.load("image/gameover.png").convert_alpha()
plane_bullet = pygame.image.load("image/bullet.png").convert_alpha()

player_img1 = pygame.image.load('image/player1.png')
player_img2 = pygame.image.load('image/player2.png')
player_img3 = pygame.image.load('image/player_off1.png')
player_img4 = pygame.image.load('image/player_off2.png')
player_img5 = pygame.image.load('image/player_off3.png')

enemy_img1 = pygame.image.load('image/enemy1.png')
enemy_img2 = pygame.image.load('image/enemy2.png')
enemy_img3 = pygame.image.load('image/enemy3.png')
enemy_img4 = pygame.image.load('image/enemy4.png')
