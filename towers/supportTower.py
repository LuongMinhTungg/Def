import pygame
from .tower import Tower
import os
import math
import time
from menu.menu import Menu

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "menu.png")), (120, 60))
upgrade_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "upgrade.png")), (50, 50))

range_imgs = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "5.png")), (90,90)),
              pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "6.png")), (90,90))]


class RangeTower(Tower):
    """
    Add extra range to each surrounding tower
    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 100
        self.tower_imgs = range_imgs[:]
        self.effect = [0.2, 0.4]
        self.width = self.height = 90
        self.name = "range"
        self.menu = Menu(self, self.x, self.y, menu_bg, [1000, "MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade")

    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)

    def get_upgrade_cost(self):
        """
        gets the upgrade cost
        :return: int
        """
        return self.menu.get_item_cost()

    def support(self, towers):
        """
        will modify towers according to ability
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis <= self.range + tower.width/2:
                effected.append(tower)

        for tower in effected:
            tower.range = tower.original_range + round(tower.range * self.effect[self.level - 1])


damage_imgs = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "8.png")), (90,90)),
              pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "9.png")), (90,90))]


class DamageTower(RangeTower):
    """
    Add damage to surrounding towers
    """
    def __init__(self, x, y):
        super().__init__(x,y)
        self.range = 100
        self.tower_imgs = damage_imgs[:]
        self.effect = [0.5, 1]
        self.name = "damage"
        self.menu = Menu(self, self.x, self.y, menu_bg, [1000, "MAX"])
        self.menu.add_btn(upgrade_btn, "Upgrade")

    def draw(self, win):
        super().draw(win)

    def support(self, towers):
        """
        will modify towers according to ability
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis <= self.range + tower.width/2:
                effected.append(tower)

        for tower in effected:
            tower.damage = tower.original_damage + round(tower.original_damage * self.effect[self.level - 1])
