import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
FPS = 90  # Increased the frame rate
WHITE = (255, 255, 255)
FONT_SIZE = 36

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Initialize paddles and ball
player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Initial spawn locations for the ball
player_ball_spawn = (WIDTH // 4, HEIGHT // 2 - BALL_RADIUS // 2)
opponent_ball_spawn = (3 * WIDTH // 4, HEIGHT // 2 - BALL_RADIUS // 2)

ball = pygame.Rect(player_ball_spawn[0], player_ball_spawn[1], BALL_RADIUS, BALL_RADIUS)

# Increased ball speed
ball_speed = [4, 4]

# Scores
player_score = 0
opponent_score = 0

# Font for scoring
font = pygame.font.Font(None, FONT_SIZE)

# Paddle speeds
player_paddle_speed = 5  # Increased player paddle speed
opponent_paddle_speed = 4  # Slightly increased opponent paddle speed

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= player_paddle_speed
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += player_paddle_speed

    # Ball movement
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collisions with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Ball collisions with paddles
    if ball.colliderect(player_paddle):
        ball_speed[0] = abs(ball_speed[0])  # Change the sign of the x-direction
    elif ball.colliderect(opponent_paddle):
        ball_speed[0] = -abs(ball_speed[0])  # Change the sign of the x-direction

    # Score points
    if ball.left <= 0:
        opponent_score += 1
        ball = pygame.Rect(opponent_ball_spawn[0], opponent_ball_spawn[1], BALL_RADIUS, BALL_RADIUS)
    elif ball.right >= WIDTH:
        player_score += 1
        ball = pygame.Rect(player_ball_spawn[0], player_ball_spawn[1], BALL_RADIUS, BALL_RADIUS)

    # Opponent AI with increased speed
    if opponent_paddle.centery < ball.centery and opponent_paddle.bottom < HEIGHT:
        opponent_paddle.y += opponent_paddle_speed
    elif opponent_paddle.centery > ball.centery and opponent_paddle.top > 0:
        opponent_paddle.y -= opponent_paddle_speed

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw scores
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (WIDTH // 4, 20))
    screen.blit(opponent_text, (3 * WIDTH // 4 - FONT_SIZE // 2, 20))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()