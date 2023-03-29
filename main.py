# moduls
import pygame
import engine
import commands as cmd
import importlib

pygame.init()
pygame.mixer.pre_init(44100, -16, 1, 512)

# Constants, classes, functions
tick = 60
settings = cmd.load_settings("settings.json")
config = cmd.load_config("config.json")

# objects
screen = cmd.display_update(settings)
console = engine.Console(screen.get_width(), pygame.font.SysFont("arial", 22))
clock = pygame.time.Clock()

mouse_vector_2 = pygame.Vector2(0, 0)
player_vector_2 = None


player = None
scene = None

running = True
while running:
    screen.fill((100, 100, 100))
    # FPS locker
    clock.tick(tick)

    # events checking
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == config["console_activate"]:
                console.in_active = not console.in_active
            elif event.key == config["change_display_type"]:
                cmd.change_display_type(settings)
            if not console.in_active:
                if player is not None:
                    if event.key == config["up"]:
                        player.move_direction["up"] = True
                    elif event.key == config["down"]:
                        player.move_direction["down"] = True
                    elif event.key == config["left"]:
                        player.move_direction["left"] = True
                    elif event.key == config["right"]:
                        player.move_direction["right"] = True

        elif event.type == pygame.KEYUP:
            if not console.in_active:
                if player is not None:
                    if event.key == config["up"]:
                        player.move_direction["up"] = False
                    elif event.key == config["down"]:
                        player.move_direction["down"] = False
                    elif event.key == config["left"]:
                        player.move_direction["left"] = False
                    elif event.key == config["right"]:
                        player.move_direction["right"] = False

        elif event.type == pygame.MOUSEMOTION:
            mouse_vector_2 = pygame.math.Vector2(event.pos)

        elif event.type == pygame.QUIT:
            running = False

    # console
    if console.activate:
        if console.inner_parameter == "exit":
            running = False
            console.log("Exiting...")
        elif console.inner_parameter == 'map':
            try:
                scene = importlib.import_module("maps." + console.inner_value)
                player = engine.Character(
                    console, "stone", screen, scene.objects.map_start_point, "musa.jpg", scene.objects.walls
                )
            except ModuleNotFoundError:
                console.log("Incorrect map name")
        elif console.inner_parameter == "speed":
            try:
                player.speed = int(console.inner_value)
            except ValueError:
                console.log("value must to be integer")
        console.history_update()
        console.activate = False
        console.inner_parameter = ''
        console.inner_value = ''

    # map
    if scene is not None:
        scene.objects.update(screen, player, mouse_vector_2, True, True)

    # --------
    console.update(screen, events)

    # display update
    pygame.display.update()
