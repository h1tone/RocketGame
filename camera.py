"""
Camera module
"""
import pygame, const

class Camera:
    def __init__(self, display, camera_func, widht, height):
        self.display = display
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, widht, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)


    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_func(camera, target_rect):
    l = -target_rect.x + const.width_display/2
    t = -target_rect.y + const.height_display/2
    w, h = camera.widht, camera.height

    l = min(0, l)
    l = max(-(camera.widht - const.level_x), l)
    t = max(-(camera.height - const.level_y), t)
    t = min(0,t)

    return pygame.Rect(l,t,w,h)