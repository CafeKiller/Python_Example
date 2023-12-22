import pygame


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
