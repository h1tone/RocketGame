"""
Это модуль нашего основоного героя
"""
import pygame, const, main
from math import pi, sin, cos
from main import display 

class Hero:
    def __init__(self):
        self.x_last = 0
        self.y_last = 0
        self.x = const.start_pos_x
        self.y = const.start_pos_y
        self.speed = 4
        self.x_dir = 0
        self.y_dir = -1
        self.phi = -pi/2
        self.omega = 1/18
        self.rocketa = pygame.image.load(const.rocketa_image)
        self.rocketa_rect = self.rocketa.get_rect(center = const.start_pos)
        self.rot = None
        self.i = 0
        self.last_rect = None
        self.a = 0

    def go_left(self):
        self.phi -= self.omega
        self.y_dir = sin(self.phi)
        self.x_dir = cos(self.phi)

    def go_right(self):
        self.phi += self.omega
        self.y_dir = sin(self.phi)
        self.x_dir = cos(self.phi)

    def rect(self):
        self.rot = pygame.transform.rotate(self.rocketa, self.i)
        self.rot_new = self.rot.get_rect(center = (self.x, self.y))
        display.blit(self.rot, self.rot_new)

    def clear_callback(self):
        display.fill(const.BLACK, (self.x_last, self.y_last, const.hero_wight, const.hero_height))

    def rotate_left(self):
        self.i += self.omega * 180/pi
        self.rot = pygame.transform.rotate(self.rocketa, self.i)
        self.rot_new = self.rot.get_rect(center = (self.x, self.y))
        display.blit(self.rot, self.rot_new)


    def rotate_right(self):
        self.i -= self.omega * 180/pi
        self.rot = pygame.transform.rotate(self.rocketa, self.i)
        self.rot_new = self.rot.get_rect(center = (self.x, self.y))
        display.blit(self.rot, self.rot_new)

    def change_xy(self):
        self.phi = self.phi % (2*pi)
        self.x_last = self.x
        self.x += self.x_dir * self.speed
        self.y_last = self.y
        self.y += self.y_dir * self.speed
        self.last_rect = self.rocketa_rect
        self.rocketa_rect = self.rocketa.get_rect(center = (self.x, self.y))
        #print(self.phi)