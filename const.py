"""
Модуль всех необходимых констант 
"""
import pygame
from random import randint

FPS = 120


""" Размеры уровня """
level_x = 3000
level_y = 3000
""" Размеры уровня """


"""Размеры экрана"""
width_display = 1366
height_display = 768
DISPLAY_SIZE = [width_display, height_display]
"""Размеры экрана"""


"""Все картинки"""
backgroud = "images\Back2.jpg"
bg = pygame.image.load(backgroud)
rocketa_image = "images\Kosmolet.png"
low_enemy = "images\RocketaEnemy.png"
hight_enemy = "images\RocketaEnemy2.png"
coin_image = "images\Coin.png"
"""Все картинки"""


"""Характеристики персонажа"""
hero_height = 38
hero_wight = 28
hero_speed = 5
hero_omega = 0  # больше, чем в обычной ракеты, но меньше, чем у поворотливой ракеты 2
"""Характеристики персонажа"""


"""Начальное положение героя"""
start_pos_x = width_display/2 - hero_wight/2
start_pos_y = height_display/2 - hero_height/2 + 200

start_pos = (start_pos_x, start_pos_y)
"""Начальное положение героя"""

"""Цвета"""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
"""Цвета"""

# самый слабый - weak $$$ средний - medium $$$ boss - boss

"""Ракета 1 обычная""" 
rocket1_speed = 0
rocket1_omega = 0
rocket1_lifetime =0
"""Ракета 1""" 


"""Ракета 2 обычная скорость, быстрее поворачивает"""
rocket2_speed = 0
rocket2_omega = 0
rocket2_lifetime = 0
"""Ракета 2"""


"""Ракета 3 быстрая, но неповоротливая"""
rocket3_speed = 0
rocket3_omega = 0
rocket3_lifetime = 0
"""Ракета 3"""


"""Размеры монеты"""
coin_widht = 10
coin_height = 10
"""Размеры бонусов"""


"""Место расположения монет"""
coin_x = randint(10, width_display - 10)
coin_y = randint(10, height_display - 10)
"""Место расположения монет"""

