import random

import pygame.mixer

from maineed.utils import *

# 遊戲狀態
running = True

# 分數
score = 0
pygame.mixer.music.play(-1)

while running:
    clock.tick(FPS)  # 遊戲FPS
    # 取得輸入
    for event in pygame.event.get():  # 如果點擊右上角的叉叉則結束遊戲
        if event.type == pygame.QUIT:
            running = False

    # 更新遊戲
    all_sprites.update()
    player.shoot()
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True)
    for hit in hits:
        random.choice(expl_sounds).play()
        score += 100
        reborn_rocks()

    hits = pygame.sprite.groupcollide(players, rocks, False, True)
    for hit in hits:
        reborn_rocks()
        player.helf -= 10
        if player.helf <= 0:
            running = False
    hits = pygame.sprite.groupcollide(space_pirate_ships, bullets, False, True)
    for hit in hits:
        space_pirate_ship.helf -= 50
        if space_pirate_ship.helf == 0:
            destruction_song.play()
            score += 1000
            space_pirate_ship.helf = 100
            space_pirate_ship.rect.x = random.randrange(200, 800)
            space_pirate_ship.rect.y = random.randrange(-500, -100)
    hits = pygame.sprite.groupcollide(players, enemybullets, False, True)
    for hit in hits:
        player.helf -= 10
        if player.helf <= 0:
            running = False


    # 畫面顯示
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text(screen, f"Score: {score}", 26, 50, 900)
    draw_health(screen, player.helf, 5, 950)
    pygame.display.update()


# 遊戲結束
pygame.quit()
