import pygame
import os
from .enemy import Enemy

imgs = []

for x in range(16):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/enemies/titan", "0" + add_str + ".png")),
        (64, 64)))


class Titan(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "titan"
        self.money = 20
        self.imgs = imgs[:]
        self.max_health = 5
        self.health = self.max_health
