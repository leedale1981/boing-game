import pgzero
import pgzrun
import pygame
import math
import sys
import random
from enum import Enum
from impact import Impact

if sys.version_info < (3, 5):
    print("This game requires at least version 3.5 of Python.")
    sys.exit()

pgzero_version = [int(s) if s.isnumeric() else s
                  for s in pgzero.__version__.split('.')]

if pgzero_version < [1, 2]:
    print(
        "this game requires at least version 1.2 of Pygame. You are using version {pgzero.__version__}.")
    sys.exit()

WIDTH = 800
HEIGHT = 480
TITLE = "Boing!"

HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PLAYER_SPEED = 6
MAX_AI_SPEED = 6


def normalised(x, y):
    length = math.hypot(x, y)
    return (x / length, y / length)


def sign(x):
    return -1 if x < 0 else 1
