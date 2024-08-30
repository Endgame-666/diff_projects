import math
import pygame

screen_size = [800, 600]
screen = pygame.display.set_mode(screen_size)


class Player:

    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.color = "Yellow"
        self.radius = 30
        self.speed = 10
        self.pos_x = self.screen_size[0] // 2
        self.pos_y = self.screen_size[1] // 2
        self.center = [self.pos_x, self.pos_y]
        self.life = 5
        self.has_immunity = False
        self.immunity_time = 1000
        self.reverse_controls = False

    def is_lu_off_screen(self, pos):
        return pos > self.radius

    def is_rd_off_screen(self, pos, size):
        return pos + self.radius < size

    def move_player(self, keys):

        if keys[pygame.K_UP] and self.is_lu_off_screen(self.pos_y):  # Вверх
            self.pos_y -= self.speed
            self.center = [self.pos_x, self.pos_y]
        if keys[pygame.K_DOWN] and self.is_rd_off_screen(self.pos_y, screen_size[1]):  # Вниз
            self.pos_y += self.speed
            self.center = [self.pos_x, self.pos_y]
        if keys[pygame.K_LEFT] and self.is_lu_off_screen(self.pos_x):  # Влево
            self.pos_x -= self.speed
            self.center = [self.pos_x, self.pos_y]
        if keys[pygame.K_RIGHT] and self.is_rd_off_screen(self.pos_x, self.screen_size[0]):  # Вправо
            self.pos_x += self.speed
            self.center = [self.pos_x, self.pos_y]

    def reverse_move_player(self, keys):
        if keys[pygame.K_DOWN] and self.is_lu_off_screen(self.pos_y):  # Вверх
            self.pos_y -= self.speed
            self.center = [self.pos_x, self.pos_y]
        if keys[pygame.K_UP] and self.is_rd_off_screen(self.pos_y, screen_size[1]):  # Вниз
            self.pos_y += self.speed
            self.center = [self.pos_x, self.pos_y]
        if keys[pygame.K_RIGHT] and self.is_lu_off_screen(self.pos_x):  # Влево
            self.pos_x -= self.speed
            self.center = [self.pos_x, self.pos_y]
        if keys[pygame.K_LEFT] and self.is_rd_off_screen(self.pos_x, self.screen_size[0]):  # Вправо
            self.pos_x += self.speed
            self.center = [self.pos_x, self.pos_y]

    def check_collision(self, enemy):
        distance = math.sqrt((self.pos_x - enemy.enemy_pos[0]) ** 2 + (self.pos_y - enemy.enemy_pos[1]) ** 2)
        return distance < (self.radius + enemy.enemy_radius)

    def draw_player(self):
        if self.has_immunity:
            self.color = (244, 169, 0)
        elif self.reverse_controls:
            self.color = (128, 64, 48)
        else:
            self.color = 'Yellow'
        pygame.draw.circle(screen, self.color, self.center, self.radius)
