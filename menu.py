import pygame, pygame_menu, main

def save():
    pass

def set_difficulty(value, difficulty):
    pass


def Menu():
    menu = pygame_menu.Menu(400, 400, 'Kosmo', theme=pygame_menu.themes.THEME_DARK)

    menu.add_button('Играть',main.start_the_game) 
    menu.add_text_input('Введите имя :', default='Марченко')
    menu.add_selector('Сложность :', [('Medium', 1), ('Hard', 2),("Easy", 3) ], onchange=set_difficulty)
    menu.add_button('Выход', pygame_menu.events.EXIT)

    menu.mainloop(main.display)

def Pause():
    pause = pygame_menu.Menu(300, 400, 'Kosmo', theme=pygame_menu.themes.THEME_DARK)

    pause.add_button('Продолжить',main.start_the_game) 
    pause.add_button("Сохранить", save)
    pause.add_button('Выход', pygame_menu.events.EXIT)

    pause.mainloop(main.display)