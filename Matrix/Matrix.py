import pygame
import pygame_gui
import random

# Создаем окно, даем название окна
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Матрица Lite')
pygame.init()
# Чтобы мы могли управлять обновление и обработку событий для всех GUI-элементов,
# добавленных в него
gui_manager = pygame_gui.UIManager(window_size)

# Создаем цифры 1 и 0
font = pygame.font.SysFont('Consolas', 20)
text_color = pygame.Color('green')
text_symbols = ['0', '1']

# Рандомно выбираем позицию и скорость полета объектов
text_pos = [(random.randint(0, window_size[0]), 0) for i in range(100)]
text_speed = [random.uniform(3, 10) for i in range(100)]
text_surface_list = []

# Параметры для кнопки
button_size = (100, 50)
button_pos = (350, 250)
button_text = 'Матрица!'

# Создаем саму кнопку
button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(button_pos, button_size),
    text=button_text,
    manager=gui_manager,
    visible=True
)

while True:
    '''Основной цикл'''
    time_delta = pygame.time.Clock().tick(60)
    # Ловим все события которые происходят на экране
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Если наша кнопка нажата, то создаем 100 разных элементов матрицы (0 или 1), рандомно задаем их первоначальную позицию и скорость
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            text_surface_list = []
            button.visible = False
            for i in range(100):
                text_symbol = random.choice(text_symbols)
                text_surface = font.render(text_symbol, True, text_color)
                text_surface_list.append(text_surface)

        gui_manager.process_events(event)

    gui_manager.update(time_delta)

    window.fill(pygame.Color('black'))
    # Изменяем позицию каждого элемента матрицы, изменяя ее позицию по y
    for i in range(100):
        text_pos[i] = (text_pos[i][0], text_pos[i][1] + text_speed[i])
        if text_pos[i][1] > window_size[1]:
            text_pos[i] = (random.randint(0, window_size[0]), -20)
        if len(text_surface_list) > i:
            window.blit(text_surface_list[i], text_pos[i])

    gui_manager.draw_ui(window)
    pygame.display.update()
