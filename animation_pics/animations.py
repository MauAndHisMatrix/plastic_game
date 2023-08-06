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
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 533
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
BUTTON_SPACING = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

class Harvester:
    def __init__(self, images, recovery_rate, price, location, name, size, speed):
        self.images = [pygame.image.load(image_path) for image_path in images]
        self.rect = self.images[0].get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        self.recovery_rate = recovery_rate
        self.price = price
        self.size = size
        self.amount = 1
        self.current_image_index = 0
        self.animation_interval = 0.25  # 0.25 seconds
        self.last_image_update_time = time.time()
        self.speed = speed

    def animate(self):
        current_time = time.time()
        if current_time - self.last_image_update_time >= self.animation_interval:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.last_image_update_time = current_time

    @property
    def image(self):
        return self.images[self.current_image_index]
    
    def mover(self):
       # Implement the mover method to move the harvester up and down the screen
        self.rect.y += self.speed  # Adjust the speed of movement as per your requirements
        if self.rect.y > WINDOW_HEIGHT:
            self.rect.y = -self.rect.height
    
class BeachMap:
    def __init__(self, screen):
        self.background_image = pygame.image.load("beach_background.png")
        self.background_image = self.resize_image(self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.harvesters = [
            Harvester(["seabin_big.png", "seabin_middle.png", "seabin_small.png",
                       "seabin_middle.png"], 100, 10000, (int(0.15*WINDOW_WIDTH), 
                    int(0.3*WINDOW_HEIGHT)), "seabin", (int(0.11*WINDOW_WIDTH),int(0.11*WINDOW_WIDTH)), 0),
            Harvester(["WasteShark.png"], 100, 10000, (int(0.0125*WINDOW_WIDTH), 0), "waste_shark",
                      (int(0.11*WINDOW_WIDTH),int(0.225*WINDOW_WIDTH)), 2.5),
            Harvester(["trashwheel_1.png", "trashwheel_2.png", 
                          "trashwheel_3.png", "trashwheel_4.png"], 
                      100, 10000, (int(0.27*WINDOW_WIDTH),0), "trash_wheel", 
                      (int(0.15*WINDOW_WIDTH), int(0.3*WINDOW_WIDTH)), 1.5),
            Harvester(["HO_wrack_1.png", "HO_wrack_2.png",
                       "HO_wrack_3.png", "HO_wrack_2.png"], 
                      100, 10000, (int(0.81*WINDOW_WIDTH),int(0.375*WINDOW_HEIGHT)),
                      "ho_wrack", (int(0.19*WINDOW_WIDTH),int(0.28*WINDOW_WIDTH)), 2),
            Harvester(["litter_pickers_1.png", "litter_pickers_2.png",
                       "litter_pickers_3.png", "litter_pickers_2.png"], 
                      100, 10000, (int(0.71*WINDOW_WIDTH),int(0.028*WINDOW_HEIGHT)),
                      "litter_picker", (int(0.125*WINDOW_WIDTH), int(0.15*WINDOW_WIDTH)), 1),
            Harvester(["litterboon_wide_.png", "litterboon_middle_.png",
                       "litterboon_narrow_.png", "litterboon_middle_.png"], 
                      100, 10000, (int(0.425*WINDOW_WIDTH),0), "litter_boon",
                      (int(0.22*WINDOW_WIDTH), WINDOW_WIDTH), 0)]
            
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

    def move_harvesters(self):
        for harvester in self.harvesters:
            harvester.mover()

    def draw(self):
        surface = self.screen
        # Draw the background image
        surface.blit(self.background_image, (0, 0))

        #Draw the harvesters on top of the background
        for harvester in self.harvesters:
            resized_image = self.resize_image(harvester.image, harvester.size)  # Adjust the size as per your requirements
            surface.blit(resized_image, harvester.rect)

            
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

        beach_map.move_harvesters()
        beach_map.draw()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
