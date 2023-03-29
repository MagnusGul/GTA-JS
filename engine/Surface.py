import pygame
import os


class Surface(object):

    def __init__(self, rect: pygame.Rect or tuple[int, int, int, int], material: str = "stone", texture: str = None):
        for i in os.listdir("source/audio/steps/"):
            if material == i:
                self.type = i
                break
        if type(rect) == tuple:
            self.rect = pygame.Rect(rect)
        else:
            self.rect = rect
        try:
            self.texture = pygame.image.load(f"source/images/surface/{texture}").convert()
        except FileNotFoundError:
            self.texture = pygame.image.load("source/images/error.png").convert()
        self.texture = pygame.transform.scale(self.texture, (self.rect.width, self.rect.height))

    def draw_rect(self, display: pygame.Surface, color: tuple = (0, 0, 0)):
        pygame.draw.rect(display, color, self.rect)

    def blit(self, screen: pygame.Surface):
        screen.blit(self.texture, self.rect)
