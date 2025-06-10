import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Mario Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player settings
player_speed = 5
jump_force = 15
gravity = 0.8
player_x = 400  # Initialize player position
player_y = 540  # Start near the bottom of the screen
player_velocity_y = 0  # Player's vertical velocity

# Platform settings
platforms = [
    pygame.Rect(100, 500, 150, 20),  # Platform 1
    pygame.Rect(300, 400, 200, 20),  # Platform 2
    pygame.Rect(600, 300, 150, 20),  # Platform 3
    pygame.Rect(200, 200, 100, 20)   # Platform 4
]

# Font for score display
font = pygame.font.SysFont(None, 50)

# Initialize score
score = 0

# Function to handle jumping
def jump():
    global player_velocity_y
    if player_y == 540:  # Can jump only if on the ground
        player_velocity_y = -jump_force

# Function to handle movement
def move(left, right):
    global player_x
    if left:
        player_x -= player_speed
    if right:
        player_x += player_speed

# Function to draw everything on the screen
def draw():
    global screen, player_x, player_y, score
    # Clear the screen
    screen.fill(WHITE)
    
    # Draw platforms
    for plat in platforms:
        pygame.draw.rect(screen, GREEN, plat)
    
    # Draw player
    pygame.draw.circle(screen, BLUE, (player_x, player_y), 20)
    
    # Draw score
    text = font.render(f'Score: {score}', True, RED)
    screen.blit(text, (10, 30))

# Update game state, including gravity and score
def update():
    global player_y, player_velocity_y, score
    
    # Apply gravity
    player_velocity_y += gravity
    player_y += player_velocity_y
    
    # Prevent the player from falling below the ground
    if player_y >= 540:
        player_y = 540
        player_velocity_y = 0  # Reset the vertical velocity when on the ground
    
    # Check for collisions with platforms
    for plat in platforms:
        if player_y + 20 >= plat.top and player_y + 20 <= plat.bottom and player_x + 20 > plat.left and player_x - 20 < plat.right:
            if player_velocity_y > 0:
                player_y = plat.top - 20  # Place player on top of the platform
                player_velocity_y = 0  # Stop downward movement
                break  # Stop checking further platforms
    
    # Update score
    score += 1

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move(left=True, right=False)
            elif event.key == pygame.K_RIGHT:
                move(left=False, right=True)
            elif event.key == pygame.K_SPACE:
                jump()
    
    # Update game state
    update()
    
    # Draw everything
    draw()
    
    # Update the display
    pygame.display.update()

    # Set the frames per second (FPS)
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
