import pygame
import random

# Initialize Pygame
pygame.init()

# Game configuration
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PLAYER_SIZE = 50
BLOCK_SIZE = 40
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Game state
player_x = WINDOW_WIDTH // 2
player_y = WINDOW_HEIGHT - PLAYER_SIZE - 50
block_y = -BLOCK_SIZE
block_x = random.randint(0, WINDOW_WIDTH - BLOCK_SIZE)
block_speed = 5
score = 0

# Initialize the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Avoid the Blocks')

clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - PLAYER_SIZE:
        player_x += 5

    # Move the block
    block_y += block_speed
    if block_y > WINDOW_HEIGHT:
        block_y = -BLOCK_SIZE
        block_x = random.randint(0, WINDOW_WIDTH - BLOCK_SIZE)
        score += 1

    # Check for collision
    if player_x < block_x + BLOCK_SIZE and player_x + PLAYER_SIZE > block_x \
            and player_y < block_y + BLOCK_SIZE and player_y + PLAYER_SIZE > block_y:
        running = False

    # Draw player and block
    pygame.draw.rect(screen, RED, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.rect(screen, BLUE, (block_x, block_y, BLOCK_SIZE, BLOCK_SIZE))

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
