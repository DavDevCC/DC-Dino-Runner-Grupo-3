import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__ (self ):
        self.type = 0  
        self.flutter = 0  #aleteo/cambiar imagenes
        super().__init__ ( BIRD, self.type ) #sacar rect
        self.rect.y = random.randint (100, 250) 
        

    def update(self , game_speed , obstacles ) :
        self.rect.x -= game_speed
        self.obstale_to_draw = BIRD[0] if self.flutter < 10 else BIRD[1]
        self.flutter += 1
        if self.flutter >= 20:
            self.flutter = 0    
        if self.rect.x < -self.rect.width :
            obstacles.pop()
        
    