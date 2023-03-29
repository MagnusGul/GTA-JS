from .Console import *
from .Wall import *
from math import ceil
from random import randint
from os import listdir


class Character(object):
    """
    Players and NPCs
    """

    def __init__(self, console: Console,
                 material: str,
                 screen: pygame.Surface,
                 map_start_point: list[int, int],
                 texture: str = None,
                 wall_list: list[Wall] = None,
                 rect: pygame.Rect = pygame.Rect(0, 0, 70, 70),
                 step_distance: int = 100, speed: int = 5):
        """

        :param speed: movement speed in pix(5)
        :param console: main game console
        """
        self.wall_list = wall_list
        self.screen = screen
        self.material = material
        self.map_start_point = map_start_point
        self.rect = rect
        try:
            self.texture = pygame.image.load(f"source/images/player/{texture}").convert()
        except FileNotFoundError:
            self.texture = pygame.image.load("source/images/error.png").convert()
        self.texture = pygame.transform.scale(self.texture, (self.rect.width, self.rect.height))
        self.original_texture = self.texture.copy()

        self.speed = speed
        self.step_distance = step_distance
        self.step_counter = 0
        self.step_sounds = {"source": "source/audio/steps/"}
        self.move_direction = {"up": False, "down": False, "left": False, "right": False}
        self.hitbox = {
            "up": pygame.Rect(self.rect.x + 1, self.rect.y, self.rect.width - 2, 1),
            "down": pygame.Rect(self.rect.x + 1, self.rect.y + self.rect.height, self.rect.width - 2, 1),
            "left": pygame.Rect(self.rect.x, self.rect.y + 1, 1, self.rect.height - 2),
            "right": pygame.Rect(self.rect.x + self.rect.width, self.rect.y + 1, 1, self.rect.height - 2)
        }

        self.vector2 = pygame.math.Vector2(self.rect.center)

        for i in listdir("source/audio/steps"):
            self.step_sounds[i] = []
        for i in listdir("source/audio/steps"):
            try:
                for j in listdir("source/audio/steps/" + i):
                    self.step_sounds[i].append(pygame.mixer.Sound(self.step_sounds["source"] + i + "/" + j))
            except FileNotFoundError:
                console.log(f"FileNotFoundError: Can't find: {i}")

    def move(self):

        speed = self.speed

        direction = self.move_direction.copy()

        if (direction["up"] or direction["down"]) and (direction["left"] or direction["right"]):
            speed = ceil(self.speed / 2)
        if direction["up"] and direction["down"]:
            direction["up"] = False
            direction["down"] = False
            speed = self.speed
        if direction["left"] and direction["right"]:
            direction["left"] = False
            direction["right"] = False
            speed = self.speed

        for i in range(speed):

            if self.wall_list is not None:
                for wall in self.wall_list:
                    for side in self.hitbox:
                        if wall.rect.colliderect(self.hitbox[side]):
                            direction[side] = False

            if direction["up"]:
                self.rect.y -= 1
                self.step_counter += 1
                self.move_hitbox("up")
            if direction["down"]:
                self.rect.y += 1
                self.step_counter += 1
                self.move_hitbox("down")
            if direction["left"]:
                self.rect.x -= 1
                self.step_counter += 1
                self.move_hitbox("left")
            if direction["right"]:
                if self.rect.x >= self.screen.get_width() * 0.75:
                    self.rect.x -= 1
                else:
                    self.rect.x += 1
                self.move_hitbox("right")
                self.step_counter += 1

        if self.step_counter >= self.step_distance:
            self.play_step()

        self.vector2 = pygame.math.Vector2(self.rect.center)

    def play_step(self):
        self.step_sounds[self.material][
            randint(0, len(listdir(self.step_sounds["source"] + self.material)) - 1)
        ].play()
        self.step_counter = 0

    def draw_rect(self, color: tuple = (0, 0, 0)):
        """

        :param color: draw color
        :return:
        """
        pygame.draw.rect(self.screen, color, self.rect)

    def draw_hitbox(self, color: tuple = (255, 0, 0)):
        for i in self.hitbox:
            pygame.draw.rect(self.screen, color, self.hitbox[i])

    def blit(self):
        self.screen.blit(self.texture, self.rect)

    def body_rotate(self, angle):
        self.texture = pygame.transform.rotate(self.original_texture, -angle)

    def move_hitbox(self, direction: str):
        if direction == "up":
            for i in self.hitbox:
                self.hitbox[i].y -= 1
        elif direction == "down":
            for i in self.hitbox:
                self.hitbox[i].y += 1
        elif direction == "left":
            for i in self.hitbox:
                self.hitbox[i].x -= 1
        elif direction == "right":
            for i in self.hitbox:
                self.hitbox[i].x += 1
