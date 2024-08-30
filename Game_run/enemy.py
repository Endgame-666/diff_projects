import math
import pygame
from random import randint, uniform

screen_size = [800, 600]
screen = pygame.display.set_mode(screen_size)


class Enemy:

    def __init__(self, screen_size):
        self.enemy_pos = list()
        self.enemy_radius = 10
        self.enemy_color = 'Red'
        self.screen_size = screen_size
        self.id = randint(0, 3)
        if self.id == 0:  # Левая сторона
            self.enemy_pos = [0, randint(0, self.screen_size[1])]
        elif self.id == 1:  # Верхняя сторона
            self.enemy_pos = [randint(0, self.screen_size[0]), 0]
        elif self.id == 2:  # Нижняя сторона
            self.enemy_pos = [randint(0, self.screen_size[0]), self.screen_size[1]]
        elif self.id == 3:  # Правая сторона
            self.enemy_pos = [self.screen_size[0], randint(0, self.screen_size[1])]
        self.speed = round(uniform(0.5, 2), 4)

    def is_enemy_off_screen(self):
        return (self.enemy_pos[0] < -self.enemy_radius or
                self.enemy_pos[0] > self.screen_size[0] + self.enemy_radius or
                self.enemy_pos[1] < -self.enemy_radius or
                self.enemy_pos[1] > self.screen_size[1] + self.enemy_radius)

    def draw_enemy(self):
        pygame.draw.circle(screen, self.enemy_color, self.enemy_pos, self.enemy_radius)


class EnemyRed(Enemy):

    def __init__(self):
        super(EnemyRed, self).__init__(screen_size)
        self.enemy_radius = 10
        self.enemy_color = 'Red'
        self.speed = round(uniform(0.5, 2), 4)

    def move_enemy(self):
        if self.id == 0:
            self.enemy_pos[0] += self.speed
        elif self.id == 1:
            self.enemy_pos[1] += self.speed
        elif self.id == 2:
            self.enemy_pos[1] -= self.speed
        elif self.id == 3:
            self.enemy_pos[0] -= self.speed


class EnemyBlue(Enemy):

    def __init__(self):
        super(EnemyBlue, self).__init__(screen_size)
        self.time_created = pygame.time.get_ticks()
        self.enemy_radius = 8
        self.enemy_color = 'blue'
        self.speed = round(3, 5)

    def move_towards_player(self, player_pos):
        direction_x = player_pos[0] - self.enemy_pos[0]
        direction_y = player_pos[1] - self.enemy_pos[1]
        distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
        if distance != 0:
            direction_x /= distance
            direction_y /= distance

        self.enemy_pos[0] += direction_x * self.speed
        self.enemy_pos[1] += direction_y * self.speed

    def move_enemy(self, player_pos):
        current_time = pygame.time.get_ticks()
        if current_time - self.time_created <= 5000:
            self.move_towards_player(player_pos)
        else:
            if self.id == 0:
                self.enemy_pos[0] += self.speed
            elif self.id == 1:
                self.enemy_pos[1] += self.speed
            elif self.id == 2:
                self.enemy_pos[1] -= self.speed
            elif self.id == 3:
                self.enemy_pos[0] -= self.speed


class EnemyBrown(Enemy):

    def __init__(self):
        super(EnemyBrown, self).__init__(screen_size)
        self.time_created = pygame.time.get_ticks()
        self.enemy_radius = 8
        self.enemy_color = (128, 64, 48)
        self.speed = 10

    def move_towards_player(self, player_pos):
        direction_x = player_pos[0] - self.enemy_pos[0]
        direction_y = player_pos[1] - self.enemy_pos[1]
        distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
        if distance != 0:
            direction_x /= distance
            direction_y /= distance

        self.enemy_pos[0] += direction_x * self.speed
        self.enemy_pos[1] += direction_y * self.speed

    def move_enemy(self, player_pos):
        current_time = pygame.time.get_ticks()
        if current_time - self.time_created <= 2000:
            self.move_towards_player(player_pos)
        else:
            if self.id == 0:
                self.enemy_pos[0] += self.speed
            elif self.id == 1:
                self.enemy_pos[1] += self.speed
            elif self.id == 2:
                self.enemy_pos[1] -= self.speed
            elif self.id == 3:
                self.enemy_pos[0] -= self.speed


class EnemyGreen(Enemy):

    def __init__(self):
        super(EnemyGreen, self).__init__(screen_size)
        self.enemy_color = 'Green'
        self.speed = 1.5
        self.heal_amount = [1, 2, 3, 4, 5]

    def move_enemy(self):
        if self.id == 0:
            self.enemy_pos[0] += self.speed
        elif self.id == 1:
            self.enemy_pos[1] += self.speed
        elif self.id == 2:
            self.enemy_pos[1] -= self.speed
        elif self.id == 3:
            self.enemy_pos[0] -= self.speed
