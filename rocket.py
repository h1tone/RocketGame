import pygame, const, sys, main, menu
from math import acos, asin, sqrt, pi, sin, cos, fmod


def quarter(x, y):
    if y < 0 and x > 0:
        return 1
    elif y < 0 and x < 0:
        return 2
    elif y >= 0 and x <= 0:
        return 3
    elif y >= 0 and x >= 0:
        return 4


def find_phi_lim(rocket):
    if rocket.q_dir_lim == 1:
        return -acos(rocket.y_dir_lim / sqrt(rocket.y_dir_lim ** 2 + rocket.x_dir_lim ** 2))
    elif rocket.q_dir_lim == 2:
        return -asin(rocket.y_dir_lim / sqrt(rocket.y_dir_lim ** 2 + rocket.x_dir_lim ** 2)) + pi / 2
    elif rocket.q_dir_lim == 3:
        return acos(rocket.y_dir_lim / sqrt(rocket.y_dir_lim ** 2 + rocket.x_dir_lim ** 2))
    elif rocket.q_dir_lim == 4:
        return asin(rocket.y_dir_lim / sqrt(rocket.y_dir_lim ** 2 + rocket.x_dir_lim ** 2)) + 3 / 2 * pi


class Rocket:
    def __init__(self, r, dis, x, y):
        self.kosmolet = r
        self.x_last = 0
        self.rocketa = pygame.image.load(const.low_enemy)
        self.rocketa_rect = self.rocketa.get_rect(center=(700, 200))
        self.y_last = 0
        self.x = x  # random.randint(0, const.width_display + 100)
        self.y = y  # random.randint(-const.height_display - 100,-const.height_display - 150)
        self.speed = 5
        self.x_dir = 0  # r.x - self.x
        self.y_dir = 1  # r.y - self.y
        self.x_dir_lim = r.x - self.x  # _lim координаты направляющего вектора, к которому стремится направляющий вектор противника
        self.y_dir_lim = r.y - self.y
        self.q = quarter(self.x, self.y)
        self.q_dir = quarter(self.x_dir, self.y_dir)
        self.q_dir_lim = quarter(self.x_dir_lim, self.y_dir_lim)
        self.phi = 0
        self.phi_lim = 0
        self.omega = 1 / 35
        self.lifetime = 100
        self.i = 0
        self.rot = None
        self.direction = 0
        self.direction_last = 0
        self.dis = dis
        self.q = quarter(self.x, self.y)
        self.q_dir = quarter(self.x_dir, self.y_dir)
        self.q_dir_lim = quarter(self.x_dir_lim, self.y_dir_lim)

    def time_death(self):
        pass

    def enemy_go_left(self):
        self.phi -= self.omega
        self.y_dir = sin(self.phi + pi / 2)
        self.x_dir = cos(self.phi + pi / 2)

    def enemy_go_right(self):
        self.phi += self.omega
        self.y_dir = sin(self.phi + pi / 2)
        self.x_dir = cos(self.phi + pi / 2)

    def enemy_clear_callback(self):
        self.dis.fill(const.BLACK, (self.x_last - 30, self.y_last - 30, const.hero_wight + 50, const.hero_height + 50))

    def enemy_rotate_left(self):
        self.i += self.omega * 180 / pi
        self.rot = pygame.transform.rotate(self.rocketa, self.i)
        self.rot_new = self.rot.get_rect(center=(self.x, self.y))
        self.dis.blit(self.rot, self.rot_new)

    def rect(self):
        self.rot = pygame.transform.rotate(self.rocketa, self.i)
        self.rot_new = self.rot.get_rect(center=(self.x, self.y))
        self.dis.blit(self.rot, self.rot_new)

    def enemy_rotate_right(self):
        self.i -= self.omega * 180 / pi
        self.rot = pygame.transform.rotate(self.rocketa, self.i)
        self.rot_new = self.rot.get_rect(center=(self.x, self.y))
        self.dis.blit(self.rot, self.rot_new)

    def enemy_change_xy(self):
        self.q = quarter(self.x, self.y)
        self.q_dir = quarter(self.x_dir, self.y_dir)
        self.q_dir_lim = quarter(self.x_dir_lim, self.y_dir_lim)
        self.x_dir_lim = self.kosmolet.x - self.x  # _lim координаты направляющего вектора, к которому стремится направляющий вектор противника
        self.y_dir_lim = self.kosmolet.y - self.y
        self.phi_lim = find_phi_lim(self)
        self.phi_lim, self.phi = self.phi_lim % (2 * pi), self.phi % (2 * pi)
        self.direction = (self.phi - self.phi_lim) % (2 * pi)
        if self.direction <= pi:
            self.enemy_go_left()
            self.enemy_rotate_left()
        elif self.direction > pi:
            self.enemy_go_right()
            self.enemy_rotate_right()
        else:
            self.rect()
        self.direction_last = self.direction
        self.x_last = self.x
        self.x += self.x_dir * self.speed
        self.y_last = self.y
        self.y += self.y_dir * self.speed
        self.last_rect = self.rocketa_rect
        self.rocketa_rect = self.rocketa.get_rect(center=(self.x, self.y))

    def is_collision(self):
        if (self.rocketa_rect.left > self.kosmolet.rocketa_rect.left) and (
                self.rocketa_rect.right < self.kosmolet.rocketa_rect.right) and (
                self.rocketa_rect.top > self.kosmolet.rocketa_rect.top) and (
                self.rocketa_rect.bottom < self.kosmolet.rocketa_rect.bottom):
            menu.Pause()
