import pygame
import os

pygame.init()
pygame.mixer.init()
# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper2.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Shield.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer1.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Shield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]
SMALL_CACTUS_CRUSHED = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1Crushed.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2Crushed.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3Crushed.png")),
]
LARGE_CACTUS_CRUSHED = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1Crushed.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2Crushed.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3Crushed.png")),
]
BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]
DEFAULT_CRUSH = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/BirdCrushed.png")),
]
CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
STARS = pygame.image.load(os.path.join(IMG_DIR, 'Other/stars.png'))
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
COIN = pygame.image.load(os.path.join(IMG_DIR, 'Other/coin.png'))

CRASH_SOUND = pygame.mixer.Sound((os.path.join(IMG_DIR, 'Other/tomb.wav')))
DISAPEAR_SOUND = pygame.mixer.Sound((os.path.join(IMG_DIR, 'Other/Shiel_Action.wav')))
THEME_SONG = pygame.mixer.Sound((os.path.join(IMG_DIR, 'Other/ThemeSong.wav')))
FONT_STYLE = "freesansbold.ttf"

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
COIN_TYPE = "coin"