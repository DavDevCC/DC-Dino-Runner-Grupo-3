import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, LARGE_CACTUS_CRUSHED, SMALL_CACTUS, SMALL_CACTUS_CRUSHED

class Cactus (Obstacle):
    def __init__(self):
        self.cactuses_types = [LARGE_CACTUS, SMALL_CACTUS]
        self.cactus_size = random.choice(self.cactuses_types)
        self.type = random.randint(0, 2)
        
        
        super().__init__ (self.cactus_size, self.type)
        self.crushed_type = self.type
        self.crushed_image = LARGE_CACTUS_CRUSHED if self.cactus_size == LARGE_CACTUS else SMALL_CACTUS_CRUSHED

        
        if self.cactus_size == SMALL_CACTUS: 
            self.rect.y = 325 
        elif self.cactus_size == LARGE_CACTUS:
            self.rect.y = 310 
      
            