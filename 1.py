import pygame
import time
import math

pygame.init()

WIDTH, HEIGHT = 1400, 1050
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

clock_face = pygame.image.load("mickey_face.png")
minute_hand = pygame.image.load("right_hand.png")
second_hand = pygame.image.load("left_hand.png")

minute_hand = pygame.transform.scale(minute_hand, (1400,1050))
second_hand = pygame.transform.scale(second_hand, (63, 1050))

CENTER = (WIDTH // 2, HEIGHT // 2)

def rotate_and_blit(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=pivot)
    screen.blit(rotated_image, rotated_rect.topleft)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    min_angle = -(minutes * 6)
    sec_angle = -(seconds * 6)

    rotate_and_blit(minute_hand, min_angle, CENTER)
    rotate_and_blit(second_hand, sec_angle, CENTER)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    pygame.time.delay(1000)

pygame.quit()
