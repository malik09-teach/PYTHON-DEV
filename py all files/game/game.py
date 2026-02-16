import pygame
import sys
import random

# --- 1. Initialization ---
pygame.init()

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100) # Color for the walls

# Define player object (red square)
player_size = 50
player_speed = 5

# Define target object (green square)
target_size = 30

# --- Game State Variables ---
score = 0
player_x, player_y = 0, 0
target_x, target_y = 0, 0
walls = []
game_over = False

# --- Font Setup ---
score_font = pygame.font.SysFont('arial', 32)
game_over_font = pygame.font.SysFont('arial', 72)
restart_font = pygame.font.SysFont('arial', 24)

clock = pygame.time.Clock()

# --- Functions to manage game state ---
def create_random_maze_walls():
    
    maze_layouts = [
    
    
        [
            pygame.Rect(0, 100, 500, 50),
            pygame.Rect(300, 250, 500, 50),
            pygame.Rect(0, 400, 500, 50),
            pygame.Rect(200, 500, 500, 50),
        ],
        # Layout 3: Vertical channels
        [
            pygame.Rect(100, 0, 50, 400),
            pygame.Rect(300, 200, 50, 600),
            pygame.Rect(500, 0, 50, 400),
            pygame.Rect(700, 200, 50, 600),
        ]
    ]
    return random.choice(maze_layouts)

def get_safe_position(size, walls):
    
    while True:
        pos_x = random.randint(0, SCREEN_WIDTH - size)
        pos_y = random.randint(0, SCREEN_HEIGHT - size)
        temp_rect = pygame.Rect(pos_x, pos_y, size, size)
        
        is_colliding = False
        for wall in walls:
            if temp_rect.colliderect(wall):
                is_colliding = True
                break
        
        if not is_colliding:
            return pos_x, pos_y

def reset_game():
    """Resets all game variables to their initial state."""
    global score, player_x, player_y, target_x, target_y, walls, game_over
    
    score = 0
    
    # Generate the walls first
    walls = create_random_maze_walls()
    
    # Then get safe positions for the player and target
    player_x, player_y = get_safe_position(player_size, walls)
    target_x, target_y = get_safe_position(target_size, walls)
    
    game_over = False

# --- 2. The Main Game Loop ---
reset_game() # Start the game for the first time

running = True
while running:
    # 2a. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_game()
    
    if not game_over:
        keys = pygame.key.get_pressed()
        
        new_x = player_x
        new_y = player_y

        if keys[pygame.K_LEFT]:
            new_x -= player_speed
        if keys[pygame.K_RIGHT]:
            new_x += player_speed
        if keys[pygame.K_UP]:
            new_y -= player_speed
        if keys[pygame.K_DOWN]:
            new_y += player_speed
            
        potential_rect = pygame.Rect(new_x, new_y, player_size, player_size)
        
        collision_with_wall = False
        for wall in walls:
            if potential_rect.colliderect(wall):
                collision_with_wall = True
                break
        
        if not collision_with_wall:
            player_x = new_x
            player_y = new_y

        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        target_rect = pygame.Rect(target_x, target_y, target_size, target_size)

        if player_x < 0 or player_x > SCREEN_WIDTH - player_size or \
           player_y < 0 or player_y > SCREEN_HEIGHT - player_size or \
           collision_with_wall:
            game_over = True
        
        if player_rect.colliderect(target_rect):
            score += 1
            # Move the target to a new safe position
            target_x, target_y = get_safe_position(target_size, walls)
    
    # 2c. Rendering (Draw the updated screen)
    screen.fill(WHITE)
    
    if not game_over:
        for wall in walls:
            pygame.draw.rect(screen, GRAY, wall)
            
        pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))
        pygame.draw.rect(screen, GREEN, target_rect)
        
        score_text = score_font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
    else:
        game_over_text = game_over_font.render("Out!", True, RED)
        final_score_text = score_font.render(f"Final Score: {score}", True, BLACK)
        restart_text = restart_font.render("Press 'R' to restart", True, BLACK)
        
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
        
        screen.blit(game_over_text, game_over_rect)
        screen.blit(final_score_text, final_score_rect)
        screen.blit(restart_text, restart_rect)
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
sys.exit()