import pygame
import pygame_gui
from random import randint

# Создаем окно
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
window_caption = 'Звездопад!'
pygame.display.set_caption(window_caption)
pygame.init()

gui_manager = pygame_gui.UIManager(window_size) #Захват всего экрана для gui-элементов

# Создаем кнопку
button_size = (100, 50)
button_pos = (350, 250)
button_caption = "Звездопад!"
button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(button_pos, button_size),
    text=button_caption,
    manager=gui_manager,
    visible=True
)

#Счетчик звезд
counter_font = pygame.font.SysFont('Consolas', 20)

stars = []
counter = 0

def create_stars():
    """Функция для создания звезд с рандомными параметрами"""
    global stars
    global counter
    stars = []
    for _ in range(50):
        star = {
            'color': (randint(0, 255), randint(0, 255), randint(0, 255)),
            'position': [randint(0, window_size[0]), randint(0, window_size[1])],
            'radius': randint(1, 3),
            'speed': (randint(1, 7), randint(1, 7))
        }
        stars.append(star)

# Основной цикл программы
while True:
    time_delta = pygame.Clock().tick(60) / 1000.0  #Выставляем значение фпс

    #Обрабатываем разные события (выход и нажатие кнопки)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button:
                button.visible = False
                create_stars()

        gui_manager.process_events(event)  #Запускаем обновление и обработку для всех gui-элементов

    gui_manager.update(time_delta)
    window.fill(pygame.Color('black'))

    # Обновляем и рисуем звезды
    for star in stars:
        star['position'][0] += star['speed'][0]
        star['position'][1] += star['speed'][1]
        if star['position'][1] > window_size[1]:
            star['position'] = [randint(0, window_size[0]), -20]
            counter += 1
        if star['position'][0] > window_size[0]:
            star['position'] = [-20, randint(0, window_size[1])]
            counter += 1
        pygame.draw.circle(window, star['color'], star['position'], star['radius'])  #Рисуем звезды
    #Делаем счетчик звезд
    star_score = counter_font.render(text=f'Упало звезд: {counter}',
                                antialias=True,
                                color='white')

    window.blit(star_score, (10, 10))  #Выводим счетчик

    gui_manager.draw_ui(window)
    pygame.display.update()

