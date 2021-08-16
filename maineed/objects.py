import pygame
import random
from maineed.setting import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HIGH - 10
        self.shoot_count = 0
        self.speed = 10
        self.helf = 100

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            self.rect.x += self.speed
        if key_pressed[pygame.K_a]:
            self.rect.x -= self.speed
        if key_pressed[pygame.K_w]:
            self.rect.y -= self.speed
        if key_pressed[pygame.K_s]:
            self.rect.y += self.speed

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HIGH:
            self.rect.bottom = HIGH

    def shoot(self):
        self.shoot_count += 1
        if self.shoot_count == shot_interval:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            self.shoot_count = 0


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.n = 0
        self.width = 30
        self.high = 30
        self.image = pygame.Surface((self.width, self.high))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(2, 10)
        self.speedx = random.randrange(-2, 2)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HIGH:
            self.rect.x = random.randrange(0, WIDTH - self.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-2, 2)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.n = 0
        self.width = 10
        self.high = 30
        self.image = pygame.Surface((self.width, self.high))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()


# 創群
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# 實體化
player = Player()

# 加群
all_sprites.add(player)
players.add(player)
for i in range(20):
    rock = Rock()
    all_sprites.add(rock)
    rocks.add(rock)
