import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
BUTTON_SPACING = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

class Button:
    def __init__(self, x, y, width, height, color, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 32)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def perform_action(self):
        if self.action is not None:
            self.action()


class Harvester:
    def __init__(self, image_path, x, y):
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (self.original_image.get_width() // 4, self.original_image.get_height() // 4))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class HarvesterMenu:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        self.value3 = 0

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self, surface):
        surface.fill(BLACK)
        font = pygame.font.Font(None, 40)
        value_text = f"Value 1: {self.value1}, Value 2: {self.value2}, Value 3: {self.value3}"
        text_surface = font.render(value_text, True, WHITE)
        text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        surface.blit(text_surface, text_rect)


class MainMenu:
    def __init__(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self, surface):
        surface.fill(BLACK)
        font = pygame.font.Font(None, 40)
        text_surface = font.render("Main Menu", True, WHITE)
        text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        surface.blit(text_surface, text_rect)


class Quiz:
    def __init__(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self, surface):
        surface.fill(BLACK)
        font = pygame.font.Font(None, 40)
        text_surface = font.render("Quiz", True, WHITE)
        text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        surface.blit(text_surface, text_rect)


class BeachMap:
    def __init__(self, screen):
        self.background_image = pygame.image.load("beach_background.png")
        self.background_image = self.resize_image(self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.harvesters = [
            Harvester("litterboon_narrow.png", 100, 200),
            Harvester("litterboon_wide.png", 300, 400)
        ]

        self.buttons = [
            Button(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE, "Harvester Menu", self.open_harvester_menu),
            Button(50, 110, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE, "Main Menu", self.open_main_menu),
            Button(50, 170, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE, "Quiz", self.open_quiz)
        ]
        self.screen = screen

    def resize_image(self, image, size):
        aspect_ratio = image.get_width() / image.get_height()
        new_width = size[0]
        new_height = int(new_width / aspect_ratio)
        if new_height > size[1]:
            new_height = size[1]
            new_width = int(new_height * aspect_ratio)
        return pygame.transform.scale(image, (new_width, new_height))

    def open_harvester_menu(self):
        harvester_menu = HarvesterMenu()
        self.run_sub_menu(harvester_menu)

    def open_main_menu(self):
        main_menu = MainMenu()
        self.run_sub_menu(main_menu)

    def open_quiz(self):
        quiz = Quiz()
        self.run_sub_menu(quiz)

    def run_sub_menu(self, sub_menu):
        clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            sub_menu.handle_events(events)

            sub_menu.draw(self.screen)

            pygame.display.flip()
            clock.tick(FPS)
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            for button in self.buttons:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        if button.is_clicked(pos):
                            button.perform_action()

    def draw(self):
        surface = self.screen
        # Draw the background image
        surface.blit(self.background_image, (0, 0))

        # Draw the harvesters on top of the background
        for harvester in self.harvesters:
            surface.blit(harvester.image, harvester.rect)

        # Draw the buttons on top of the background and harvesters
        for button in self.buttons:
            button.draw(surface)


def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Beach Map")

    beach_map = BeachMap(screen)

    clock = pygame.time.Clock()

    while True:
        events = pygame.event.get()
        beach_map.handle_events(events)

        beach_map.draw()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
