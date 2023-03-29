from pygame import FULLSCREEN
from pygame import display
from json import loads


def change_display_type(settings_dict):
    if settings_dict["window_full_screen"]:
        settings_dict["window_full_screen"] = 0
    else:
        settings_dict["window_full_screen"] = FULLSCREEN


def display_update(settings_dict):
    screen = display.set_mode((settings_dict["window_height"], settings_dict["window_width"]),
                              settings_dict["window_full_screen"], vsync=True)
    return screen


def load_settings(settings_file):
    settings_file = open(settings_file)
    settings_inner = str(settings_file.read())
    settings_dict = loads(settings_inner)

    settings_dict["window_full_screen"] = bool(settings_dict["window_full_screen"])

    if settings_dict["window_full_screen"]:
        settings_dict["window_full_screen"] = FULLSCREEN
    else:
        settings_dict["window_full_screen"] = 0

    return dict(settings_dict)


def load_config(config_file):
    config_file = open(config_file)
    config_inner = str(config_file.read())
    config_dict = loads(config_inner)

    return dict(config_dict)
