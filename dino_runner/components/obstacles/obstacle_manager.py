import random, pygame


from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus


class ObstacleManager:
    def __init__(self):
        self.obstacles = []   
      
    def update(self, game):
        if len (self.obstacles) == 0:
             self.obstacle_type_list = [Bird(), Cactus()]
             self.obstacles.append(random.choice(self.obstacle_type_list))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                game.death_count += 1
                game.player_scores.append(game.score) 
                game.player_high_score = max(game.player_scores)
                pygame.time.delay(1000)  
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
                obstacle.draw(screen) 
    
    def reset_obstacles(self):
        self.obstacles = []
            