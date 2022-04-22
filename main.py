import pygame
import numpy as np


class Game:
    def __init__(self):
        pygame.init()
        width, height = 800, 600
        self.screen = pygame.display.set_mode([width, height])
        pygame.display.set_caption('Snake.py')
        self.fps = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        # start position Snake
        self.snake_pos = [400, 200]
        self.snake_body = [[400, 200], 
                            [390, 200], 
                            [380, 200], 
                            [370, 200]
                            ]

        self.direction = 'LEFT'
        self.newDirection = self.direction
        self.game_loop()

    def game_loop(self):
        # Loop mit While True: Schleife
        run = True

        while run:
            print("neue Runde, direction: "+ str(self.direction)+ " ,newdirection: "+ str(self.newDirection))
            self.direction = self.newDirection
            self.fps.tick(15)
            BG_COLOR = pygame.Color(73, 241, 202)
            self.screen.fill(BG_COLOR)
            # Standard für Games sind 3 Methoden:
            self.input()    # player eingabe
            self.update()   # screen Update mit Ereignissen
            self.draw()     # screen zeichnen

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


    def update(self):
        # Snake berührt sich = GameOver
        for block in self.snake_body[1:]:
            if self.snake_pos[0] == block[0] and self.snake_pos[1] == block[1]:
                pass
                #self.reset()
        # Snake berührt Fenster:
        if self.snake_pos[1] < 0:
            self.reset()
            print("kaputt1")
        if self.snake_pos[0] < 0:
            self.reset()
            print("kaputt2")


    def draw(self):
        # SnakeBody Zeichnen in voller Länge mit for-Schleife
        for self.snake_pos in self.snake_body:
            pygame.draw.rect(self.screen, pygame.Color(242, 135, 73), pygame.Rect(self.snake_pos[0], self.snake_pos[1], 10, 10))

    def reset(self):
        self.snake_pos = [400, 200]
        self.snake_body = [[400, 200], [390, 200], [380, 200], [370, 200]]


Game()
