# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 13:37:07 2023

@author: Lillemoen
"""
#harvester.py

import pygame
import time

import utils

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 533

images = [
    ["seabin_big.png", "seabin_middle.png", "seabin_small.png", "seabin_middle.png"],
    ["WasteShark.png"],
    ["trashwheel_1.png", "trashwheel_2.png", "trashwheel_3.png", "trashwheel_4.png"],
    ["HO_wrack_1.png", "HO_wrack_2.png", "HO_wrack_3.png", "HO_wrack_2.png"],
    ["litter_pickers_1.png", "litter_pickers_2.png", "litter_pickers_3.png", "litter_pickers_2.png"],
    ["litterboon_wide.png", "litterboon_middle.png", "litterboon_narrow.png", "litterboon_middle.png"]
]
# Apply image_selector to each element in the images array
images = list(map(lambda lst: list(map(utils.image_selector, lst)), images))

harvester_params = [
    (images[0], 1.17, 4100, (int(0.15*WINDOW_WIDTH), int(0.3*WINDOW_HEIGHT)), "Seabin", (int(0.11*WINDOW_WIDTH), int(0.11*WINDOW_WIDTH)), 0),
    (images[1], 150, 24600, (int(0.0125*WINDOW_WIDTH), 0), "WasteShark", (int(0.11*WINDOW_WIDTH), int(0.225*WINDOW_WIDTH)), 2.5),
    (images[2], 6205, 800000, (int(0.27*WINDOW_WIDTH), 0), "Trash Wheel", (int(0.15*WINDOW_WIDTH), int(0.3*WINDOW_WIDTH)), 1.5),
    (images[3], 2, 10000, (int(0.81*WINDOW_WIDTH), int(0.375*WINDOW_HEIGHT)), "HO Wrack", (int(0.19*WINDOW_WIDTH), int(0.28*WINDOW_WIDTH)), 2),
    (images[4], 0.1, 1000, (int(0.71*WINDOW_WIDTH), int(0.028*WINDOW_HEIGHT)), "Litter Picker", (int(0.125*WINDOW_WIDTH), int(0.15*WINDOW_WIDTH)), 1),
    (images[5], 18, 100000, (int(0.425*WINDOW_WIDTH), 0), "LitterBoom", (int(0.22*WINDOW_WIDTH), WINDOW_HEIGHT), 0)
]


class Harvester:
    def __init__(self, images, recovery_rate, price, location, name, size, speed):
        self.images = [pygame.image.load(image_path) for image_path in images]
        self.rect = self.images[0].get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        self.recovery_rate = recovery_rate
        self.price = price
        self.size = size
        self.amount = 0
        self.current_image_index = 0
        self.animation_interval = 0.25  # 0.25 seconds
        self.last_image_update_time = time.time()
        self.speed = speed
        self.name = name
        
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