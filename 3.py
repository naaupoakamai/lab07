import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Ball")

BALL_RADIUS = 25
BALL_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
STEP = 20

ball_x = WIDTH // 2
ball_y = HEIGHT // 2

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - BALL_RADIUS - STEP >= 0:
                    ball_y -= STEP
            elif event.key == pygame.K_DOWN:
                if ball_y + BALL_RADIUS + STEP <= HEIGHT:
                    ball_y += STEP
            elif event.key == pygame.K_LEFT:
                if ball_x - BALL_RADIUS - STEP >= 0:
                    ball_x -= STEP
            elif event.key == pygame.K_RIGHT:
                if ball_x + BALL_RADIUS + STEP <= WIDTH:
                    ball_x += STEP

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
