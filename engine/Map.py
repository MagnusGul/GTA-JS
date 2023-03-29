from .Character import *


def calc_angle(v1: pygame.Vector2, v2: pygame.Vector2):
    v2_new = pygame.Vector2(v2.x - v1.x, v2.y - v1.y)
    v1_new = pygame.Vector2(0, 0)
    angle = v1_new.angle_to(v2_new)

    return angle


class Map(object):

    def __init__(self, walls: list, surfaces: list, roofs: list, map_start_point: list[int, int]):
        self.surfaces = surfaces
        self.walls = walls
        self.roofs = roofs
        self.map_start_point = map_start_point
        self.all = self.surfaces + self.walls + self.roofs

    def map_move(self, direction: dict[str: int, str: int, str: int, str: int]):
        for target in self.all:
            if direction["up"]:
                target.rect.y -= 1
            if direction["down"]:
                target.rect.y += 1
            if direction["left"]:
                target.rect.x -= 1
            if direction["right"]:
                target.rect.x += 1

    def update(self, screen: pygame.Surface, player: Character, mouse_vector2: pygame.Vector2,
               surface_blit: bool = False, wall_blit: bool = False,
               surface_draw: bool = False, wall_draw: bool = False):

        for surface in self.surfaces:
            if surface.rect.colliderect(player.rect):
                player.material = surface.type
            else:
                player.material = "stone"
            if surface_draw:
                surface.draw_rect(screen, (255, 255, 255))
            if surface_blit:
                surface.blit(screen)
            surface.rect.x -= self.map_start_point[0]
            surface.rect.y -= self.map_start_point[1]

        for wall in self.walls:
            if wall_draw:
                wall.draw(screen, (0, 0, 0))
            if wall_blit:
                wall.blit(screen)
            wall.rect.x -= self.map_start_point[0]
            wall.rect.y -= self.map_start_point[1]
        for roof in self.roofs:
            if not player.rect.colliderect(roof.rect):
                roof.alpha += 10
                if roof.alpha > 255:
                    roof.alpha = 255
            else:
                if roof.alpha < 0:
                    roof.alpha = 0
                roof.alpha -= 10
            roof.rect.x -= self.map_start_point[0]
            roof.rect.y -= self.map_start_point[1]
            roof.texture.set_alpha(roof.alpha)
            roof.blit(screen)

        player.move()
        player.body_rotate(calc_angle(player.vector2, mouse_vector2))
        player.blit()
