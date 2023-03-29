import pygame


class Wall(object):

    def __init__(self, rect: pygame.Rect or tuple[int, int, int, int], texture: str = None):
        if type(rect) == tuple:
            self.rect = pygame.Rect(rect)
        else:
            self.rect = rect

        try:
            self.texture = pygame.image.load(f"source/images/wall/{texture}").convert()
        except FileNotFoundError:
            self.texture = pygame.image.load("source/images/error.png").convert()
        self.texture = pygame.transform.scale(self.texture, (self.rect.width, self.rect.height))

    def draw(self, surface: pygame.Surface, color: tuple = (0, 0, 0)):
        pygame.draw.rect(surface, color, self.rect)

    def blit(self, screen: pygame.Surface):
        screen.blit(self.texture, self.rect)
