import pygame
from player import Player
from enemy import EnemyRed, EnemyBlue, EnemyBrown, EnemyGreen
import pygame_gui

screen_size = [800, 600]
screen = pygame.display.set_mode(screen_size)
player = Player(screen_size)
pygame.init()
gui_manager = pygame_gui.UIManager(screen_size)


class Game:
    best_records = list()  # Список с результами

    def __init__(self, screen_size):
        pygame.init()
        self.time = 0
        self.screen_size = screen_size
        self.screen_caption = 'Игра'
        pygame.display.set_caption(self.screen_caption)
        self.timer = pygame.time.Clock()
        self.font_size = 20
        self.font_name = 'Consolas'
        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.data_red = list()
        self.data_blue = list()
        self.data_brown = list()
        self.data_green = list()
        self.events = list()
        self.running = True
        self.game_over = False
        self.level = [(1500, 6000, 10000, 19000),  # Начальный уровень сложности
                      (1200, 5000, 9000, 29000),  # 20 секунд
                      (1000, 4000, 8000, 39000),  # 50 секунд
                      (800, 3000, 7000, 49000),  # 90 секунд
                      (600, 2000, 6000, 50000)]  # 140 секунд
        self.level_time = [20, 50, 90, 140]
        self.current_level = 0
        self.start = True

    def start_game(self):
        """Делает экран старта игры с объяснением, что делает каждый враг"""
        screen.fill('black')
        text_red = self.font.render(
            text='КРАСНЫЙ',
            antialias=True,
            color='Red'
        )
        text_after_red = self.font.render(
            text=' - СНИМАЕТ ТВОЮ ЖИЗНЬ, ЕСЛИ ПОПАДЕШЬ ПОД НЕГО',
            antialias=True,
            color='white'
        )

        text_after_blue = self.font.render(
            text=' - СНИМАЕТ ТВОЮ ЖИЗНЬ И САМ НЕСЕТСЯ НА ТЕБЯ',
            antialias=True,
            color='white'
        )

        text_after_brown = self.font.render(
            text=' - НЕ СНИМАЕТ ТВОЮ ЖИЗНЬ, ЕСЛИ ПОПАДЕШЬ ПОД НЕГО ИНВЕРТИРУЕТСЯ ',
            antialias=True,
            color='white'
        )
        text_after_brown_2 = self.font.render(
            text='УПРАВЛЕНИЕ',
            antialias=True,
            color='white'
        )
        text_after_green = self.font.render(
            text=' - ВОССТАНАВЛИВАЕТ ОДНО ЗДОРОВЬЕ',
            antialias=True,
            color='white'
        )
        text_blue = self.font.render(
            text='СИНИЙ',
            antialias=True,
            color='blue'
        )
        text_brown = self.font.render(
            text='КОРИЧНЕВЫЙ',
            antialias=True,
            color='brown'
        )
        text_green = self.font.render(
            text='ЗЕЛЕНЫЙ',
            antialias=True,
            color='green'
        )
        text_start = self.font.render(
            text='НАЖМИ ЛЮБУЮ КНОПКУ ЧТОБЫ НАЧАТЬ',
            antialias=True,
            color='white'
        )
        screen.blit(text_red, (10, 10))
        screen.blit(text_after_red, (text_red.get_width() + 10, 10))
        screen.blit(text_blue, (10, 30))
        screen.blit(text_after_blue, (text_blue.get_width() + 10, 30))
        screen.blit(text_brown, (10, 50))
        screen.blit(text_after_brown, (text_brown.get_width() + 10, 50))
        screen.blit(text_after_brown_2, (10, 70))
        screen.blit(text_green, (10, 90))
        screen.blit(text_after_green, (text_green.get_width() + 10, 90))
        screen.blit(text_start, (230, 250))
        freeze = True
        while freeze:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    print(111111)
                    freeze = False
                    self.start = False
            pygame.display.update()
        screen.fill('black')

    def end(self):
        """Делает экран конца игры и показывает результаты"""
        self.game_over = True  # флаг окончания игры
        screen.fill('black')
        end_font = pygame.font.SysFont('Consolas', 50)
        end = end_font.render(
            text="GAME OVER",
            antialias=True,
            color='white'
        )
        score = self.font.render(
            text=f'Вы продержались: {round(self.time, 2)}!',
            antialias=True,
            color='white'
        )
        best_score = self.font.render(
            text=f'Лучший рекорд: {max(self.best_records)}',
            antialias=True,
            color='white'
        )
        continue_text = self.font.render(
            text=f'Нажмите любую кнопку чтобы сыграть еще раз',
            antialias=True,
            color='white'
        )

        screen.blit(best_score, (280, 330))
        screen.blit(score, (280, 300))
        screen.blit(end, (280, 200))
        screen.blit(continue_text, (200, 400))
        pygame.display.update()

        freeze = True
        pygame.time.delay(5000)
        while freeze:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    freeze = False
                    self.reset_game()
            pygame.display.update()

    def reset_game(self):
        """Начинает игру с начала"""
        self.time = 0
        self.timer = pygame.time.Clock()
        self.data_red.clear()
        self.data_blue.clear()
        self.data_brown.clear()
        self.data_green.clear()
        player.pos_x = screen_size[0] // 2
        player.pos_y = screen_size[1] // 2
        player.center = [player.pos_x, player.pos_y]
        player.life = 3
        player.has_immunity = False
        player.immunity_start_time = 0
        self.game_over = False
        self.run_game()
        self.start = False

    def is_alive(self, enemy):
        """Проверяет, столкнулся ли игрок с врагом, жив ли еще игрок, и смотрит, если эффект иммунитета или инверсии управления"""
        cur_time = pygame.time.get_ticks()

        if player.has_immunity:
            player.reverse_controls = False
            if cur_time - player.immunity_start_time > player.immunity_time:
                player.has_immunity = False

        if player.reverse_controls and cur_time - player.reverse_controls_start > 2000:
            player.reverse_controls = False

        if player.check_collision(enemy):
            if type(enemy) != EnemyBrown and type(enemy) != EnemyGreen:
                if player.life == 0:
                    self.best_records.append(round(self.time, 2))
                    self.end()
                elif not player.has_immunity:
                    player.life -= 1
                    player.has_immunity = True
                    player.immunity_start_time = cur_time
            elif type(enemy) == EnemyBrown:
                self.data_brown.remove(enemy)
                player.reverse_controls = True
                player.reverse_controls_start = cur_time
            elif type(enemy) == EnemyGreen:
                self.data_green.remove(enemy)
                player.life += 1

    def create_captions(self):
        """Создает показатели здоровья, времени и уровня сложности сверху слева"""
        time_score = self.font.render(
            text=f'Прошло времени: {round(self.time, 2)}',
            antialias=True,
            color='white'
        )

        life_last = self.font.render(
            text=f'Осталось жизней: {player.life}',
            antialias=True,
            color='white'
        )

        level = self.font.render(
            text=f'Сложность: {self.current_level + 1}',
            antialias=True,
            color='white'
        )

        screen.blit(time_score, [10, 10])
        screen.blit(life_last, [10, 30])
        screen.blit(level, [10, 50])

    def increase_difficulty(self):
        """Повышает сложность каждые 20, 30, 40, 50 секунд."""
        if self.current_level < len(self.level) - 1:
            if self.time >= self.level_time[self.current_level]:
                self.current_level += 1
                red_spawn, blue_spawn, brown_spawn, green_spawn = self.level[self.current_level]
                pygame.time.set_timer(self.events[0], red_spawn)
                pygame.time.set_timer(self.events[1], blue_spawn)
                pygame.time.set_timer(self.events[2], brown_spawn)
                pygame.time.set_timer(self.events[3], green_spawn)

    def run_game(self):
        """Основная функция игры, запускает и отрисовывает все все все"""
        event_red = pygame.USEREVENT + 1
        event_blue = pygame.USEREVENT + 2
        event_brown = pygame.USEREVENT + 3
        event_green = pygame.USEREVENT + 4
        red_spawn, blue_spawn, brown_spawn, green_spawn = self.level[self.current_level]
        pygame.time.set_timer(event_red, red_spawn)
        pygame.time.set_timer(event_blue, blue_spawn)
        pygame.time.set_timer(event_brown, brown_spawn)
        pygame.time.set_timer(event_green, green_spawn)
        self.events.append(event_red)
        self.events.append(event_blue)
        self.events.append(event_brown)
        self.events.append(event_green)
        if self.start:
            self.start_game()
        while self.running:
            if not self.game_over and not self.start:
                time_delta = self.timer.tick(60) / 1000.0

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        pygame.quit()
                        quit()
                    elif event.type == self.events[0]:
                        enemy_red = EnemyRed()
                        self.data_red.append(enemy_red)
                    elif event.type == self.events[1]:
                        enemy_blue = EnemyBlue()
                        self.data_blue.append(enemy_blue)
                    elif event.type == self.events[2]:
                        enemy_brown = EnemyBrown()
                        self.data_brown.append(enemy_brown)
                    elif event.type == self.events[3]:
                        for _ in range(self.current_level + 1):
                            enemy_green = EnemyGreen()
                            self.data_green.append(enemy_green)

                self.time += time_delta

                self.increase_difficulty()

                keys = pygame.key.get_pressed()
                if not player.reverse_controls:
                    player.move_player(keys)
                else:
                    player.reverse_move_player(keys)

                screen.fill('black')

                for enemy in self.data_red[:]:
                    enemy.move_enemy()
                    if enemy.is_enemy_off_screen():
                        self.data_red.remove(enemy)
                    else:
                        enemy.draw_enemy()
                    self.is_alive(enemy)

                for enemy in self.data_blue[:]:
                    enemy.move_enemy(player.center)
                    if enemy.is_enemy_off_screen():
                        self.data_blue.remove(enemy)
                    else:
                        enemy.draw_enemy()
                    self.is_alive(enemy)

                for enemy in self.data_brown[:]:
                    enemy.move_enemy(player.center)
                    if enemy.is_enemy_off_screen():
                        self.data_brown.remove(enemy)
                    else:
                        enemy.draw_enemy()
                    self.is_alive(enemy)

                for enemy in self.data_green[:]:
                    enemy.move_enemy()
                    if enemy.is_enemy_off_screen():
                        self.data_green.remove(enemy)
                    else:
                        enemy.draw_enemy()
                    self.is_alive(enemy)

                player.draw_player()

                self.create_captions()

            pygame.display.update()


game = Game(screen_size)
game.run_game()

game = Game(screen_size)
game.run_game()
