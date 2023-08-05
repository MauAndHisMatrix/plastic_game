# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 23:05:46 2023

@author: Lillemoen
"""

import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
BUTTON_SPACING = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

class Harvester:
    def __init__(self, images, recovery_rate, price, location, name):
        self.images = [pygame.image.load(image_path) for image_path in images]
        self.rect = self.images[0].get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        self.recovery_rate = recovery_rate
        self.price = price
        self.amount = 1
        self.current_image_index = 0
        self.animation_interval = 0.25  # 0.25 seconds
        self.last_image_update_time = time.time()

    def animate(self):
        current_time = time.time()
        if current_time - self.last_image_update_time >= self.animation_interval:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.last_image_update_time = current_time

    @property
    def image(self):
        return self.images[self.current_image_index]
    
class BeachMap:
    def __init__(self, screen):
        self.background_image = pygame.image.load("beach_background.png")
        self.background_image = self.resize_image(self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.harvesters = [
            Harvester(["seabin.png"], 100, 10000, [30, 30], "seabin"),
            Harvester(["WasteShark.png"], 100, 10000, [80, 30], "waste_shark"),
            Harvester(["trashwheel_1.png", "trashwheel_2.png", 
                          "trashwheel_3.png", "trashwheel_4.png"], 
                      100, 10000, [130,30], "trash_wheel"),
            Harvester(["HO_wrack_1.png", "HO_wrack_2.png",
                       "HO_wrack_3.png", "HO_wrack_1.png"], 
                      100, 10000, [300,200], "ho_wrack"),
            Harvester(["litter_picker_1.png", "litter_picker_2.png",
                       "litter_picker_3.png", "litter_picker_2.png"], 
                      100, 10000, [300,150], "litter_picker"),
            Harvester(["litterboon_wide.png", "litterboon_middle.png",
                       "litterboon_narrow.png", "litterboon_middle.png"], 
                      100, 10000, [50,50], "litter_boon")
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

    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def draw(self):
        surface = self.screen
        # Draw the background image
        surface.blit(self.background_image, (0, 0))

        #Draw the harvesters on top of the background
        for harvester in self.harvesters:
            surface.blit(harvester.image, harvester.rect)

            
def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Beach Map")

    beach_map = BeachMap(screen)

    clock = pygame.time.Clock()

    while True:
        events = pygame.event.get()
        beach_map.handle_events(events)
        
        for harvester in beach_map.harvesters:
            harvester.animate()  # Call the animate method to update

        beach_map.draw()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
