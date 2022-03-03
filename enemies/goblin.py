import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(12):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/enemies/goblin", "0" + add_str + ".png")),
        (48, 48)))


class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "goblin"
        self.money = 12
        self.imgs = imgs[:]
        self.max_health = 3
        self.health = self.max_health


