import pygame
import random

class GameObject:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self, surface):
        raise NotImplementedError

class Snake(GameObject):
    def __init__(self):
        super().__init__(400, 300, 20)
        self.direction = pygame.K_RIGHT

    def update(self):
        if self.direction == pygame.K_UP:
            self.y -= self.size
        elif self.direction == pygame.K_DOWN:
            self.y += self.size
        elif self.direction == pygame.K_LEFT:
            self.x -= self.size
        elif self.direction == pygame.K_RIGHT:
            self.x += self.size

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.size, self.size))

class Food(GameObject):
    def __init__(self):
        super().__init__(random.randint(0, 800), random.randint(0, 600), 20)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.size, self.size))