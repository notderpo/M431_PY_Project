import pygame
import sys
import random

# Initialisierung von Pygame
pygame.init()

# Konstanten
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
SNAKE_SIZE = 20
SNAKE_SPEED = 15

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Richtungen
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = WHITE

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * SNAKE_SIZE)) % WIDTH), (cur[1] + (y * SNAKE_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], SNAKE_SIZE, SNAKE_SIZE))

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                         random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE))

# Erstelle ein Fenster
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake = Snake()
food = Food()

# Spiel-Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.direction = UP
            if event.key == pygame.K_DOWN and snake.direction != UP:
                snake.direction = DOWN
            if event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.direction = LEFT
            if event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.direction = RIGHT

    snake.update()

    # Kollision mit der Nahrung
    if snake.get_head_position() == food.position:
        snake.length += 1
        food.randomize_position()

    # Zeichne den Hintergrund
    screen.fill(BLACK)

    # Zeichne die Schlange und die Nahrung
    snake.render(screen)
    food.render(screen)

    # Aktualisiere den Bildschirm
    pygame.display.flip()

    # Begrenze die Aktualisierungsrate
    clock.tick(SNAKE_SPEED)
    
