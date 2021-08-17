import pygame.transform

from maineed.setting import *

# 載入圖片
player_img = pygame.image.load(os.path.join("img", "player.png")).convert()
screen_img = pygame.image.load(os.path.join("img", "d.png")).convert()
eneship_img = pygame.image.load(os.path.join("img", "eneship.png")).convert()
rock_png = pygame.image.load(os.path.join("img", "rock.png")).convert()
bullet_png = pygame.image.load(os.path.join("img", "bullet.png")).convert()
# 載入音效
shood_soung = pygame.mixer.Sound(os.path.join("sound", "shoot.wav"))
shood_soung.set_volume(0.8)
expl_sounds = [
    pygame.mixer.Sound(os.path.join("sound", "expl0.wav")),
    pygame.mixer.Sound(os.path.join("sound", "expl1.wav"))
]
destruction_song = pygame.mixer.Sound(os.path.join("sound", "destruction1.wav"))
destruction_song.set_volume(0.5)
pygame.mixer.music.load(os.path.join("sound", "background.ogg"))
pygame.mixer.music.set_volume(1)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
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
        if self.shoot_count == player_shot_interval:
            shood_soung.play()
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            self.shoot_count = 0


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.n = 0
        self.image_ori = rock_png
        self.image_ori.set_colorkey(BLACK)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-2000, -100)
        self.speedy = random.randrange(2, 10)
        self.speedx = random.randrange(-2, 2)
        self.total_dgree = 0
        self.rot_degree = random.randrange(-3, 3)

    def rotate(self):
        self.total_dgree += self.rot_degree
        self.total_dgree = self.total_dgree % 360
        self.image = pygame.transform.rotate(self.image_ori, self.total_dgree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HIGH:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-2, 2)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_png
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.n = 0
        self.width = 10
        self.high = 30
        self.image = pygame.Surface((self.width, self.high))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.n = 0
        self.width = random.randrange(2, 10)
        self.high = self.width + 5
        self.image = pygame.Surface((self.width, self.high))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(10, 20)
        self.speedx = random.randrange(-1, 1)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HIGH:
            self.rect.x = random.randrange(0, WIDTH - self.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(10, 20)
            self.speedx = random.randrange(-1, 1)


class SpacePirateShip(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.n = 0
        self.width = 30
        self.high = 100
        self.image = pygame.transform.scale(eneship_img, (50, 125))
        self.image.set_colorkey(BLACK)
        self.helf = 100
        self.shoot_count = 0
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(200, 800)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = 1
        self.speedx = 0

    def update(self):
        self.shoot_count += 1
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HIGH:
            self.rect.x = random.randrange(200, 800)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = 1
            self.speedx = 0
        if self.shoot_count == space_pirate_ship_shot_interval:
            enemybullet = EnemyBullet(self.rect.centerx, self.rect.top)
            all_sprites.add(enemybullet)
            enemybullets.add(enemybullet)
            self.shoot_count = 0


class Screen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = screen_img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -10000
        self.speedy = 10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HIGH:
            self.rect.x = 0
            self.rect.y = -10000
            self.speedy = 10


# 創群
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemybullets = pygame.sprite.Group()
space_pirate_ships = pygame.sprite.Group()

# 實體化
player = Player()
space_pirate_ship = SpacePirateShip()
screens = Screen()
# 加群
players.add(player)
space_pirate_ships.add(space_pirate_ship)
# 顯示順序
all_sprites.add(screens)
for i in range(5):
    meteor = Meteor()
    all_sprites.add(meteor)
for i in range(20):
    rock = Rock()
    all_sprites.add(rock)
    rocks.add(rock)
all_sprites.add(space_pirate_ship)
all_sprites.add(player)
