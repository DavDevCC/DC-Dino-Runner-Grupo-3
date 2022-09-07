import random

from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from dino_runner.components.obstacles.cactus import Cactus


class ObstacleManager:
    def __init__ (self) :
        self.obstacles = []

    def update(self, game ) :
        obstacle_options = [SMALL_CACTUS, LARGE_CACTUS]
        if len (self.obstacles ) == 0 :
             self.obstacles.append(Cactus(random.choice(obstacle_options)))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False

    def draw (self, screen) :
        for obstacle in self.obstacles :
            obstacle.draw(screen) 