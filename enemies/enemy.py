import pygame
import math
import os


class Enemy:
    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.path = [(10, 245), (177, 245), (282, 297), (526, 297), (627, 217), (681, 105), (747, 77), (816, 83),
                     (883, 222), (973, 284), (1096, 366), (1042, 478), (894, 501), (740, 524), (580, 562), (148, 541),
                     (85, 522), (42, 415), (1, 365), (-5, 365), (-75, 360), (-100, 345)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = pygame.image.load(os.path.join("game_assets/enemies/spider", "000.png"))
        self.dis = 0
        self.path_pos = 0
        self.move_dis = 0
        self.imgs = []
        self.flipped = False
        self.max_health = 0
        self.speed_increased = 1.1

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        self.img = self.imgs[self.animation_count]

        win.blit(self.img, (self.x - self.img.get_width()/2, self.y - self.img.get_height()/2 - 18))
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        draw health bar above enemy
        :param win: surface
        :return: None
        """
        length = 50
        moveBy = round(length / self.max_health)
        health_bar = round(moveBy * self.health)

        pygame.draw.rect(win, (255,0,0), (self.x-30, self.y-75, length, 10), 0)
        pygame.draw.rect(win, (0,255,0), (self.x-30, self.y-75, health_bar, 10), 0)

    def collide(self, X, Y):
        """
        Returns if position has hit enemy
        :param x: int
        :param y: int
        :return: Bool
        """
        if self.x + self.width >= X >= self.x:
            if self.y + self.height >= Y >= self.y:
                return True
        return False

    def move(self):
        """
        Move enemy
        :return: None
        """
        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        x1, y1 = self.path[self.path_pos]
        x1 = x1 + 70
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-100, 345)
        else:
            x2, y2 = self.path[self.path_pos + 1]
        x2 = x2 + 70

        dirn = ((x2 - x1), (y2 - y1))
        length = math.sqrt((dirn[0]) ** 2 + (dirn[1]) ** 2)
        dirn = (dirn[0]/length * self.speed_increased, dirn[1]/length * self.speed_increased)

        # Flip enemies
        if dirn[0] < 0 and not (self.flipped):
            self.flipped = True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)

        move_x, move_y = (self.x + dirn[0]), (self.y + dirn[1])

        self.x = move_x
        self.y = move_y

        # Go to next point
        if dirn[0] >= 0:  # moving right
            if dirn[1] >= 0:  # moving down
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1
        else:  # moving left
            if dirn[1] >= 0:  # moving down
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x <= x2 and self.y >= y2:
                    self.path_pos += 1

    def hit(self, damage):
        """
        Removes health and returns if enemy is alive.
        :return: Bool
        """
        self.health -= damage
        if self.health <= 0:
            return True
        return False

