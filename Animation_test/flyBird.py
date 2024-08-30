import pygame
import os

window_size = (650, 600)
window = pygame.display.set_mode(window_size)
window_caption = 'Полет птички'
pygame.display.set_caption(window_caption)
pygame.init()

window.fill('white')
pygame.display.flip()
clock = pygame.time.Clock()

frame_images = []
for i in range(1, 10):
    frame_images.append(pygame.image.load(f'frames/frm_{i}.png'))
   # os.system(f'frames/frm_{i}.png')

# параметры анимации
animation_length = len(frame_images)
animation_speed = 60  # кадры в секунду
current_frame_index = 0
animation_timer = 0
frame_position = [0, 0]

while True:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    animation_timer += time_delta

    if animation_timer >= 4.6 / animation_speed:
        current_frame_index = (current_frame_index + 1) % animation_length
        animation_timer -= 4.6 / animation_speed

    current_frame = frame_images[current_frame_index]
    window.blit(current_frame, frame_position)
    pygame.display.update()