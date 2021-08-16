from maineed.utils import *

# 初始化
pygame.init()
# 創建視窗
screen = pygame.display.set_mode((WIDTH, HIGH))
# 標題
pygame.display.set_caption('First Game By York')
# 時間管理
clock = pygame.time.Clock()
# 字體載入
font_name = pygame.font.match_font('arial')
# 遊戲狀態
running = True

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
        reborn_rocks()

    # 畫面顯示
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.update()

# 遊戲結束
pygame.quit()
