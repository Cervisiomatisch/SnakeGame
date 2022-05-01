import pygame
import random

class Game:
    def __init__(self):
        pygame.init()
        self.width = 500
        self.height = 400
        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption('Snake.py')
        self.fps = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        self.score = 0
        # start position Snake
        self.snake_pos = [50, 100]
        self.snake_body = [
                            [50, 100], 
                            [40, 100], 
                            [30, 100], 
                            [20, 100]
                            ]
        # start fruit position
        self.fruit_pos = [random.randrange(1, (self.width//10)) * 10,
                  random.randrange(1, (self.height//10)) * 10]
        self.fruit_spawn = True


        self.direction = 'RIGHT'
        self.newDirection = self.direction
        self.game_loop()

    def game_loop(self):
        # Loop mit While True: Schleife
        run = True

        while run:
            print("neue Runde, direction: "+ str(self.direction)+ " ,newdirection: "+ str(self.newDirection))
            self.fps.tick(15)
            self.direction = self.newDirection
            
            BG_COLOR = pygame.Color(73, 241, 202)
            self.screen.fill(BG_COLOR)
            # Score geschichte
            self.score_font = pygame.font.SysFont('times new roman', 20)
            self.score_surface = self.score_font.render('Score : ' + str(self.score), True, pygame.Color(255, 255, 255))
            self.score_rect = self.score_surface.get_rect()
            self.screen.blit(self.score_surface, self.score_rect)
            # Standard für Games sind 3 Methoden (*):
            self.input()        # *player eingabe
            self.update()       # *screen Update mit Ereignissen
            self.draw()         # *screen zeichnen

            pygame.display.flip()

    def input(self):
        # Programm läuft nicht weiter, wenn Display geschlossen wird
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        # Playerinput
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.newDirection = 'UP'
                    print("Oben gedrückt")
                if event.key == pygame.K_DOWN:
                    self.newDirection = 'DOWN'
                    print("Runter gedrückt")
                if event.key == pygame.K_LEFT:
                    self.newDirection = 'LEFT'
                    print("Links gedrückt")
                if event.key == pygame.K_RIGHT:
                    self.newDirection = 'RIGHT'
                    print("Rechts gedrückt")
        
        # Playerinput korrigieren, dass Snake nicht sofort in die gegengesetzte Richtung kann
        if self.newDirection == 'UP' and self.direction != 'DOWN':
            self.direction == 'UP'
        if self.newDirection == 'DOWN' and self.direction != 'UP':
            self.direction == 'DOWN'
        if self.newDirection == 'RIGHT' and self.direction != 'LEFT':
            self.direction == 'RIGHT'
        if self.newDirection == 'LEFT' and self.direction != 'RIGHT':
            self.direction == 'LEFT'

        # Snake bewegen 
        if self.direction == 'UP':
                self.snake_pos[1] -= 10
                print("geht hoch")
        if self.direction == 'DOWN':
                self.snake_pos[1] += 10
                print("geht runter")
        if self.direction == 'RIGHT':
                self.snake_pos[0] += 10
                print("geht rechts")
        if self.direction == 'LEFT':
                self.snake_pos[0] -= 10
                print("geht links1")
        # Snake wächst
        self.snake_body.insert(0, list(self.snake_pos))
        if self.snake_pos[0] == self.fruit_pos[0] and self.snake_pos[1] == self.fruit_pos[1]:
            self.score += 1
            self.fruit_spawn = False
        else:
            self.snake_body.pop()

        if not self.fruit_spawn:
            self.fruit_pos = [random.randrange(1, (self.width//10)) * 10,
                              random.randrange(1, (self.height/10)) * 10]
        self.fruit_spawn = True
    
    def update(self):
        # Snake berührt sich = GameOver
        for block in self.snake_body[1:]:
            if self.snake_pos[0] == block[0] and self.snake_pos[1] == block[1]:
                self.reset()
        # Snake berührt Fenster:
        if self.snake_pos[1] < 0:
            self.reset()
        if self.snake_pos[0] < 0:
            self.reset()


    def draw(self):
        # SnakeBody Zeichnen in voller Länge mit for-Schleife
        for self.pos in self.snake_body:
            pygame.draw.rect(self.screen, pygame.Color(242, 135, 73), pygame.Rect(self.pos[0], self.pos[1], 10, 10))
        
        pygame.draw.rect(self.screen, pygame.Color(255, 0, 0), pygame.Rect(
        self.fruit_pos[0], self.fruit_pos[1], 10, 10))

    def reset(self):
        self.direction = 'RIGHT'
        self.score = 0
        self.snake_pos = [50, 100]
        self.snake_body = [
                            [50, 100], 
                            [40, 100], 
                            [30, 100], 
                            [20, 100]
                            ]

Game()
