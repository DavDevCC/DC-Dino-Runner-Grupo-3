import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


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

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

        self.running = False
        self.score = 0
        self.death_count = 0
        self.player_scores = []
        self.player_high_score = 0

    def execute(self):
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
    
    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.obstacle_manager.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.update() # actualiza pantalla = se puede pasar componentes
        

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        self.blit_text(self.screen, f"Score: {self.score}", 1000, 70, text_size_font = 22)
        self.blit_text(self.screen, f"Highscore: {self.player_high_score}", 1000, 40, text_size_font = 22)


    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False        
            if event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((180, 180, 180))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.blit_text(self.screen, "Press any key to start", half_screen_width, half_screen_height)
        else:
            self.blit_text(self.screen, "Press any key to restart", half_screen_width, half_screen_height, text_size_font = 40)
            self.blit_text(self.screen, f"Death count: {self.death_count}", half_screen_width, half_screen_height + 50)
            self.blit_text(self.screen, f"Score: {self.score}", half_screen_width, half_screen_height + 100)
            self.blit_text(self.screen, f"High Score: {self.player_high_score}", half_screen_width, 100)
        self.screen.blit(ICON, (half_screen_width - 30, half_screen_height - 140))
        pygame.display.flip()
        self.handle_events_on_menu()
    
    def blit_text(self, screen, text, x_pos, y_pos, text_font = FONT_STYLE, text_size_font = 30, color_text = (0, 0, 0) ):
        font = pygame.font.Font(text_font, text_size_font)
        text = font.render(text, True, color_text)
        text_rect = text.get_rect()
        text_rect.center = (x_pos, y_pos)
        screen.blit(text, text_rect)


