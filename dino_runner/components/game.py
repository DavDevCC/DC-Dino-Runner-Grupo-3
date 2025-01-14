import random
import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, CLOUD, DEFAULT_TYPE, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, STARS, THEME_SONG, TITLE, FPS



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.text_color = (0, 0, 0)

        self.x_pos_cloud = SCREEN_WIDTH
        self.y_pos_cloud = random.randint(50, 150)
        self.x_pos_stars = 0
        self.y_pos_stars = 50

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

        self.running = False
        self.score = 0
        self.death_count = 0
        self.player_scores = []
        self.player_high_score = 0

    def execute(self):
        theme_song = pygame.mixer.Sound(THEME_SONG)
        pygame.mixer.Sound.play(theme_song, -1)
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.score = 0
        self.game_speed = 20
        self.playing = True
        self.power_up_manager.reset_power_ups()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.update_score()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.score, self.game_speed, self.player)
    
    def update_score(self):
        self.score += 1
        if self.score % 200 == 0:
            self.game_speed += 3


    def draw(self):
        
        self.clock.tick(FPS)
        background_color = (255, 255, 255) if self.score // 500 != 1 else (50, 50, 50)
        self.text_color = (0, 0, 0) if self.score // 500 != 1 else (255, 255, 255)
        self.screen.fill(background_color)
        self.player.draw(self.screen)
        if background_color == (50, 50, 50):
            self.x_pos_stars = self.draw_bg_items(STARS, self.y_pos_stars, self.x_pos_stars, y_pos_restart = 50, movement_vel= 8)
        else:
            self.x_pos_cloud = self.draw_bg_items(CLOUD, self.y_pos_cloud, self.x_pos_cloud, x_pos_restart = SCREEN_WIDTH, y_pos_restart = random.randint(50, 100), movement_vel = self.game_speed // 3)

        self.x_pos_bg = self.draw_bg_items(BG, self.y_pos_bg, self.x_pos_bg, )
        self.draw_score()
        self.draw_power_up_time(self.text_color)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update() # actualiza pantalla = se puede pasar componentes
        
    def draw_bg_items(self, image, y_pos, x_pos, x_pos_restart = 0, y_pos_restart = 380, movement_vel = 20):
        x_pos = x_pos
        image_width = image.get_width()
        self.screen.blit(image, (x_pos, y_pos))
        self.screen.blit(image, (image_width + x_pos, y_pos))
        if x_pos <= -image_width:
            self.screen.blit(image, (image_width + x_pos, y_pos))
            x_pos = x_pos_restart #scr width
            y_pos = y_pos_restart
        x_pos -= movement_vel
        return x_pos
        


    def draw_score(self):
        blit_text(self.screen, f"Score: {self.score}", 70, x_pos = 1000, text_size_font = 22, color_text = self.text_color)
        blit_text(self.screen, f"Highscore: {self.player_high_score}", 40, x_pos = 1000, text_size_font = 22,  color_text = self.text_color)

   

    def draw_power_up_time(self, text_color):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks()) / 1000, 1)
            if time_to_show >= 0:
                blit_text(self.screen, f"{self.player.type.capitalize()} enabled for {time_to_show} seconds", 40, x_pos= 500, text_size_font = 22, color_text = text_color) 
            else :                                               
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE


    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False        
            if event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            blit_text(self.screen, "Press any key to start", half_screen_height)
        else:
            blit_text(self.screen, "Press any key to restart", half_screen_height, text_size_font = 40)
            blit_text(self.screen, f"Death count: {self.death_count}", half_screen_height + 50)
            blit_text(self.screen, f"Score: {self.score}", half_screen_height + 100)
            blit_text(self.screen, f"High Score: {self.player_high_score}", 100)
            self.screen.blit(ICON, (half_screen_width - 30, half_screen_height - 140))
         #   blit_text(self.screen, f"High Score: {self.player_high_score}", 100)
            
            
        self.screen.blit(ICON, (half_screen_width - 30, half_screen_height - 140))
        pygame.display.flip()
        self.handle_events_on_menu()
    
    
def blit_text(screen, text,  y_pos, x_pos = SCREEN_WIDTH // 2 , text_font = FONT_STYLE, text_size_font = 30, color_text = (0, 0, 0) ):
    font = pygame.font.Font(text_font, text_size_font)
    text = font.render(text, True, color_text)
    text_rect = text.get_rect()
    text_rect.center = (x_pos, y_pos)
    screen.blit(text, text_rect)


