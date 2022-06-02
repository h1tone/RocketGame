"""
Класс для разных бустов
"""

import pygame, hero, const, score, time
from random import randint

class Bonus:
    def __init__(self, display, kosmolet, time):
        self.coin_widht = const.coin_widht
        self.coin_height = const.coin_height
        self.coin_x = randint(10, const.width_display - 10)
        self.coin_y = randint(10, const.height_display - 10)
        self.coin_image = pygame.image.load(const.coin_image)
        self.display = display
        self.time = time
        self.kosmolet = kosmolet
        self.coin_position = (self.coin_x, self.coin_y)
        self.coin_rect = self.coin_image.get_rect(center = self.coin_position)

    # менять положение монеты 
    def update(self): 
        self.display.blit(self.coin_image, (self.coin_x, self.coin_y))
        if self.check():
            self.coin_x = randint(10, const.width_display - 10)
            self.coin_y = randint(10, const.height_display - 10)
            self.coin_position = (self.coin_x, self.coin_y)
            self.coin_rect = self.coin_image.get_rect(center = self.coin_position)


    # проверка на совпадение rect-ов космолета и монеты
    def check(self): 
        if (self.coin_rect.right > self.kosmolet.rocketa_rect.left) and (self.coin_rect.left < self.kosmolet.rocketa_rect.right) and (self.coin_rect.bottom > self.kosmolet.rocketa_rect.top) and (self.coin_rect.top < self.kosmolet.rocketa_rect.bottom):
            return True
        else:
            return False




