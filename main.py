import pygame
from pygame.locals import *

pygame.ini()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))
display = pygame.Surface((300, 300))

while True:
  display.fill((0, 0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
  pygame.transfor.scale(diplay,screen.get_size(), screen)
  pygame.display.update()

