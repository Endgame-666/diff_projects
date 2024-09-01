import pygame
import random

pygame.init()

window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Матрица')

font = pygame.font.SysFont('MS Gothic', 20)
color = ['green', (30, 89, 69), (0, 69, 36), (0, 102, 51), 'green', 'green', ]

katakana_symbols = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ',
                    'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト',
                    'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
                    'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ',
                    'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン']

hiragana_symbols = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ',
                    'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と',
                    'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ',
                    'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り',
                    'る', 'れ', 'ろ', 'わ', 'を', 'ん']

japanese_symbols = katakana_symbols + hiragana_symbols

columns = 40
column_width = window_size[0] // columns

text_pos = [[(x * column_width, random.randint(-window_size[1], 0)) for y in range(20)] for x in range(columns)]
text_speed = [random.randint(2, 5) for _ in range(columns)]
change_frequency = [random.randint(5, 15) for _ in range(columns)]
frame_counters = [[0 for _ in range(20)] for _ in range(columns)]
text_color = [random.choice(color) for _ in range(columns)]

text_surface_list = [[font.render(random.choice(japanese_symbols), True, random.choice(color)) for _ in range(20)] for _
                     in range(columns)]

clock = pygame.time.Clock()
running = True

while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(pygame.Color('black'))

    for col in range(columns):
        for i in range(len(text_pos[col])):

            x, y = text_pos[col][i]
            y += text_speed[col]
            if y > window_size[1]:
                y = random.randint(-20, -5)

            frame_counters[col][i] += 1
            if frame_counters[col][i] >= change_frequency[col]:
                text_symbol = random.choice(japanese_symbols)
                text_surface_list[col][i] = font.render(text_symbol, True, text_color[col])
                frame_counters[col][i] = 0

            text_pos[col][i] = (x, y)
            window.blit(text_surface_list[col][i], (x, y))

    pygame.display.update()

pygame.quit()
