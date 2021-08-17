from maineed.objects import *


def reborn_rocks():
    r = Rock()
    all_sprites.add(r)
    rocks.add(r)

def reborn_space_pirate_ship():
    s = SpacePirateShip()
    all_sprites.add(s)
    space_pirate_ships.add(s)


def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 200
    BAR_HIGHT = 15
    fill = (hp / 100) * BAR_LENGTH
    outline_recy = pygame.Rect(x, y, BAR_LENGTH, BAR_HIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, GREEN, outline_recy, 2)

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)