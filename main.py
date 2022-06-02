import pygame, const, hero, random, bonus, rocket, sys, pygame_menu, menu
from camera import Camera, camera_func
from math import cos, sin, pi, acos, sqrt, fmod
from score import Score

pygame.font.init()

pygame.init()

display = pygame.display.set_mode(const.DISPLAY_SIZE)
pygame.display.set_caption("Kosmo")

time = pygame.time.Clock()


def start_the_game():
    clock = pygame.time.Clock()
    score = Score(display)
    rocketa = hero.Hero()
    # enemy = rocket.Rocket(rocketa, display, 1000, 700)
    # enemy2 = rocket.Rocket(rocketa, display, 100, 100)
    coin = bonus.Bonus(display, rocketa, 10)
    coin_list = []
    enemy_list = []
    coin_counter = 0
    time_start = pygame.time.get_ticks()
    run = True
    while run:

        if pygame.time.get_ticks() % 1500 == 0:
            enemy_list.append(rocket.Rocket(rocketa, display, random.randint(-200, const.width_display + 50),
                                            random.randint(-200, const.height_display + 50)))
        clock.tick(const.FPS)

        rocketa.change_xy()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()

        display.blit(const.bg, (0, 0))

        if keys[pygame.K_LEFT]:
            rocketa.go_left()
            rocketa.rotate_left()
        elif keys[pygame.K_RIGHT]:
            rocketa.go_right()
            rocketa.rotate_right()
        else:
            rocketa.rect()

        if keys[pygame.K_ESCAPE]:
            menu.Pause()

        if coin.check():
            coin_counter += 1

        # enemy.is_collision()
        # enemy2.is_collision()
        for i in enemy_list:
            i.enemy_change_xy()
            i.is_collision()

        coin.update()

        score.score_update(coin_counter)

        # enemy.enemy_change_xy()
        # enemy2.enemy_change_xy()

        pygame.display.flip()


if __name__ == "__main__":
    menu.Menu()
