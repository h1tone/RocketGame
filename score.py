"""
Модуль для подсчета очков и записывания их в файл
"""
import pygame, hero, const

class Score:
    def __init__(self, display):
        self.main_font = pygame.font.SysFont("comicsans", 50)
        self.score_label = None
        self.display = display

    # обновление количества собранных монет
    def score_update(self, sc):
        self.score_label = self.main_font.render(f"Coins: {sc}", 100, (255,255,0)) 
        self.display.blit(self.score_label, (const.width_display - self.score_label.get_width() - 10, 10)) # счет в углу экрана 

    def save_coins(self):
        pass