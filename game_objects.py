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
        self.body = [(self.x, self.y)]  # Body is a list of positions
        self.grow = False

    def update(self):
        # Calculate new position
        if self.direction == pygame.K_UP:
            new_pos = (self.x, self.y - self.size)
        elif self.direction == pygame.K_DOWN:
            new_pos = (self.x, self.y + self.size)
        elif self.direction == pygame.K_LEFT:
            new_pos = (self.x - self.size, self.y)
        elif self.direction == pygame.K_RIGHT:
            new_pos = (self.x + self.size, self.y)
        # Add new position to start of body
        self.body.insert(0, new_pos)
        # Update head position
        self.x, self.y = new_pos
        # If not growing, remove last position from body
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False  # Reset grow flag

        # Check if snake has crossed the border
        if self.x >= 800:
            self.x = 0
        elif self.x < 0:
            self.x = 800 - self.size
        if self.y >= 600:
            self.y = 0
        elif self.y < 0:
            self.y = 600 - self.size

    def draw(self, surface):
        # Draw the head
        pygame.draw.rect(surface, (255, 0, 0), (*self.body[0], self.size, self.size))
        # Draw the rest of the body
        for pos in self.body[1:]:
            pygame.draw.rect(surface, (255, 255, 255), (*pos, self.size, self.size))

    # Removed grow method

class Food(GameObject):
    def __init__(self):
        super().__init__(random.randint(0, 800), random.randint(0, 600), 20)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.size, self.size))

class BigFood(GameObject):
    def __init__(self):
        super().__init__(random.randint(0, 800), random.randint(0, 600), 40)
        self.timer = pygame.time.get_ticks()

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y, self.size, self.size))
