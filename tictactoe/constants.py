import pygame

WINDOW_WIDTH = 500
MARGIN = 100
PROFILE_SIZE = WINDOW_WIDTH // 10

P1_LOGO = pygame.image.load("assets/star.png")
P2_LOGO = pygame.image.load("assets/error.png")
P1_IMG = pygame.image.load("assets/happy.png")
P2_IMG = pygame.image.load("assets/batman.png")

P1_AVATAR = pygame.transform.scale(P1_IMG, (PROFILE_SIZE, PROFILE_SIZE))
P2_AVATAR = pygame.transform.scale(P2_IMG, (PROFILE_SIZE, PROFILE_SIZE))

GREEN = (39, 174, 96)
GREY = (44, 62, 80)
PURPLE = (142, 68, 173)
WHITE = (255, 255, 255)
