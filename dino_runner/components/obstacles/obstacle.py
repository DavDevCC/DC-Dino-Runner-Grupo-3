import pygame

from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH, DEFAULT_CRUSH

class Obstacle(Sprite):
    def __init__(self, image, obstacle_type):
        self.was_crushed = False
        self.crushed_image = DEFAULT_CRUSH
        self.crushed_type = 0
        self.image = image
        self.obstacle_type = obstacle_type
        self.obstacle_to_draw = self.image[self.obstacle_type]
        self.rect = self.obstacle_to_draw.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = 325

    
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
            
    def draw(self, screen):
        screen.blit(self.obstacle_to_draw, (self.rect.x, self.rect.y))
        
    def do_sound(self, destroy_sound):
        action_sound = pygame.mixer.Sound(destroy_sound)
        pygame.mixer.Sound.play(action_sound)
   