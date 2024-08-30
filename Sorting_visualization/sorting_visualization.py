import pygame
from random import randint
import pygame_gui

'''Инициализация разных переменных, названий, кнопок и тд'''
pygame.init()
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Визуализация сортировок')

gui_manager = pygame_gui.UIManager(window_size)

cell_size = 4

height = window_size[1] // cell_size
width = window_size[0] // cell_size

clock = pygame.time.Clock()

button_size = (100, 50)
button_pos_1 = (150, 250)
button_pos_2 = (350, 250)
button_pos_3 = (550, 250)

button_caption_1 = "Пузырьком"
button_caption_2 = "Пирамидой"
button_caption_3 = "Выбором"

button_1 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(button_pos_1, button_size),
    text=button_caption_1,
    manager=gui_manager,
    visible=True
)

button_2 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(button_pos_2, button_size),
    text=button_caption_2,
    manager=gui_manager,
    visible=True
)

button_3 = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(button_pos_3, button_size),
    text=button_caption_3,
    manager=gui_manager,
    visible=True
)

percent_counter = pygame.font.SysFont('Consolas', 20)


def bubble_sort(lst):
    '''Выполняет сортировку пузырьком, визуалилурет ее и показывает сколько осталось до полной сортировки в процентах'''
    for percent in range(len(lst)):
        percent_ = percent_counter.render(text=f'Выполнено: {(round(percent / width, 3) * 100) + 0.5} %',
                                          antialias=True,
                                          color='white')
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
            window.fill(pygame.Color('black'))
            for j in range(len(lst)):
                if i + 1 != j:
                    pygame.draw.rect(window, 'white',
                                     [j * cell_size, (height - lst[j]) * cell_size, cell_size, lst[j] * cell_size])
                else:
                    pygame.draw.rect(window, 'red',
                                     [j * cell_size, (height - lst[j]) * cell_size, cell_size, lst[j] * cell_size])
            window.blit(percent_, (10, 10))
            pygame.display.flip()
            clock.tick(500)
    frozen = True
    while frozen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                frozen = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                frozen = False


def heapify(lst, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and lst[left_child] > lst[largest]:
        largest = left_child
    if right_child < heap_size and lst[right_child] > lst[largest]:
        largest = right_child
    if largest != root_index:
        lst[root_index], lst[largest] = lst[largest], lst[root_index]
        heapify(lst, heap_size, largest)


def heap_sort(lst):
    '''Выполняет пирамидальную сортировку, визуалилурет ее и показывает сколько осталось до полной сортировки в процентах'''
    n = len(lst)
    for i in range(n, -1, -1):
        heapify(lst, n, i)
    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
        window.fill(pygame.Color('black'))
        for j in range(len(lst)):
            percent_ = percent_counter.render(text=f'Выполнено: {round((width / (j + 1)), 3)} %',
                                              antialias=True,
                                              color='white')

            if i != j:
                pygame.draw.rect(window, 'white',
                                 [j * cell_size, (height - lst[j]) * cell_size, cell_size, lst[j] * cell_size])
            else:
                pygame.draw.rect(window, 'red',
                                 [j * cell_size, (height - lst[j]) * cell_size, cell_size, lst[j] * cell_size])

                window.blit(percent_, (10, 10))
        pygame.display.flip()
        clock.tick(15)

    frozen = True

    while frozen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                frozen = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                frozen = False


def selection_sort(lst):
    '''Выполняет сортировку выбором, визуалилурет ее и показывает сколько осталось до полной сортировки в процентах'''
    for i in range(len(lst)):
        percent_ = percent_counter.render(text=f'Выполнено: {round((i / width), 3) * 100 +0.5} %',
                                          antialias=True,
                                          color='white')
        minimum = i
        window.fill(pygame.Color('black'))
        for j in range(len(lst)):
            color = 'red' if j == minimum else 'white'
            pygame.draw.rect(window, color,
                             [j * cell_size, (height - lst[j]) * cell_size, cell_size, lst[j] * cell_size])
        pygame.display.flip()
        clock.tick(30)

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[minimum]:
                minimum = j
                window.fill(pygame.Color('black'))
                for k in range(len(lst)):
                    color = 'red' if k == minimum else 'white'
                    pygame.draw.rect(window, color,
                                     [k * cell_size, (height - lst[k]) * cell_size, cell_size, lst[k] * cell_size])
                window.blit(percent_, (10, 10))
                pygame.display.flip()
                clock.tick(30)

        lst[minimum], lst[i] = lst[i], lst[minimum]

        window.fill(pygame.Color('black'))
        for j in range(len(lst)):
            pygame.draw.rect(window, 'white',
                             [j * cell_size, (height - lst[j]) * cell_size, cell_size, lst[j] * cell_size])
        window.blit(percent_, (10, 10))
        pygame.display.flip()
        clock.tick(30)

    frozen = True

    while frozen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                frozen = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                frozen = False


running = True
while running:
    '''основной цикл, при нажатии на кнопу запускается визуализация выбранной сортировки'''
    lst = [randint(0, window_size[1] // cell_size) for _ in range(window_size[0] // cell_size)]
    time_delta = pygame.Clock().tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == button_1:
                button_1.visible = False
                button_2.visible = False
                button_3.visible = False
                bubble_sort(lst)

            if event.ui_element == button_2:
                button_1.visible = False
                button_2.visible = False
                button_3.visible = False
                heap_sort(lst)
            if event.ui_element == button_3:
                button_1.visible = False
                button_2.visible = False
                button_3.visible = False
                selection_sort(lst)

        gui_manager.process_events(event)

    gui_manager.update(time_delta)
    window.fill('black')

    button_1.visible = True
    button_2.visible = True
    button_3.visible = True

    gui_manager.draw_ui(window)
    pygame.display.update()

pygame.quit()
