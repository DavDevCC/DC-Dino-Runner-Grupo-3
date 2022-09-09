import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, DEFAULT_CRUSH

class Bird(Obstacle):
    def __init__ (self):
        self.type = 0  
        self.flutter = 0  #aleteo/cambiar imagenes
        super().__init__ (BIRD, self.type) #sacar rect
        self.rect.y = random.randint(200, 320) 
        self.crushed_image = DEFAULT_CRUSH
        self.crushed_type = 0
        

    def update(self, game_speed, obstacles):
        if not self.was_crushed:
            self.obstacle_to_draw = BIRD[0] if self.flutter < 10 else BIRD[1]
            self.flutter += 1
            if self.flutter >= 20:
                self.flutter = 0    
        super().update(game_speed, obstacles)
        

    