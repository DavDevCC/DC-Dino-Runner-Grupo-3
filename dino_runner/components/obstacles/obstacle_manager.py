import random, pygame



from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import COIN_TYPE, CRASH_SOUND, DEFAULT_CRUSH, DISAPEAR_SOUND, HAMMER_TYPE, SHIELD_TYPE



class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
      
    def update(self, game):
        if len(self.obstacles) == 0:
             self.obstacle_type_list = [Bird(), Cactus()]
             self.obstacles.append(random.choice(self.obstacle_type_list))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type == SHIELD_TYPE:
                    obstacle.do_sound(DISAPEAR_SOUND)
                    self.obstacles.remove(obstacle)

                elif game.player.type == COIN_TYPE:
                    game.score += 20 
                    
                elif game.player.type == HAMMER_TYPE:
                    if not obstacle.was_crushed:
                        obstacle.do_sound(CRASH_SOUND)
                        obstacle.was_crushed = True
                        game.game_speed -= 1
                    obstacle.obstacle_to_draw = obstacle.crushed_image[obstacle.crushed_type]
                    obstacle.rect.y += 90 if obstacle.crushed_image == DEFAULT_CRUSH else 50
                    
                    
                else:
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
            