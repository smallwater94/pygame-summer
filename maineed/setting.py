import os
import pygame
import random
# 螢幕大小
WIDTH = 1000
HIGH = 1000

# 遊戲幀數
FPS = 60

# 各類顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 97, 0)
GREEN = (0, 255, 255)
GREY = (190, 190, 190)
BLUE = (0, 0, 205)

# 射擊間隔
player_shot_interval = 30
space_pirate_ship_shot_interval = 80

# 初始化
pygame.init()
# 創建視窗
screen = pygame.display.set_mode((WIDTH, HIGH))
# 標題
pygame.display.set_caption('星際大冒險')
# 時間管理
clock = pygame.time.Clock()
# 字體載入
font_name = pygame.font.match_font('arial')