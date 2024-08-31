import pygame
import random
from random import randint
import pymunk.pygame_util

pymunk.pygame_util.positive_y_is_up = False


class Galton_board:
    def __init__(self):
        pygame.init()
        self.widht = 800
        self.hight = 1000
        self.screen_size = (self.widht, self.hight)
        self.fps = 60
        self.screen = pygame.display.set_mode(self.screen_size)
        self.clock = pygame.time.Clock()
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.space = pymunk.Space()
        self.space.gravity = 0, 8000
        self.step_line = 57.114
        self.running = True
        self.step_x = 80
        self.step_y = 31
        self.start_x = [0, 40]

    def create_circle(self, space):
        pos = (randint(0, 800), randint(0, 100))
        mass, size = 100, 7
        circle_moment = pymunk.moment_for_circle(mass, 0, size)
        circle_body = pymunk.Body(mass, circle_moment)
        circle_body.position = pos
        circle_shape = pymunk.Circle(circle_body, size)
        circle_shape.elasticity = 0.4
        circle_shape.friction = 1.0
        circle_shape.color = (randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))
        space.add(circle_body, circle_shape)
        return pos, size

    def create_static_circle(self, x, y):
        static_circle_body = self.space.static_body
        static_circle_body.position = (self.start_x[y % 2] + x * self.step_x, 350 + y * self.step_y)
        static_circle_shape = pymunk.Circle(static_circle_body, 10)
        static_circle_shape.elasticity = 0.4
        static_circle_shape.friction = 1.0
        self.space.add(static_circle_shape)

    def create_segments(self, space, start, end, thickness):
        segment = pymunk.Segment(space.static_body, start, end, thickness)
        segment.elasticity = 0.8
        segment.friction = 1.0
        space.add(segment)

    def run(self):

        self.create_segments(self.space, (1, self.hight), (self.widht, self.hight), 30)
        self.create_segments(self.space, (0, 100), (350, 250), 5)
        self.create_segments(self.space, (450, 250), (800, 100), 5)
        self.create_segments(self.space, (350, 290), (350, 250), 5)
        self.create_segments(self.space, (450, 290), (450, 250), 5)
        for i in range(15):
            self.create_segments(self.space, (i * self.step_line, 1000), (i * self.step_line, 600), 5)

        [([random.randrange(256) for _ in range(3)], self.create_circle(self.space)) for _ in range(700)]

        for y in range(8):
            for x in range(12 - y % 2):
                self.create_static_circle(x, y)

        while self.running:
            self.screen.fill('black')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()

            self.space.step(1 / self.fps)
            self.space.debug_draw(self.draw_options)

            pygame.display.flip()
            self.clock.tick(self.fps)


galton_board = Galton_board()
galton_board.run()
