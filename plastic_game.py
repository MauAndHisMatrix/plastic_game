# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 20:33:32 2023

@author: Lillemoen
"""

import json
from typing import Union
import numpy as np



POLLUTION_LEVEL = 2000
HARVESTERS = "seabin trash_wheel waste_shark litter_boon ho_wrack litter_picker".split()


class BeachMap:
    def __init__(self, current_plastic_level,
                       bank):
        self._plastic_level = current_plastic_level
        self._bank = bank

        self.harvesters = [Harvester(harv) for harv in HARVESTERS]

        self._turn_counter = 1
        self._panel_size = (100, 100)

        self.pollution_rate = 20
        self.recovery_rate = 0
        


    def add_harvester(self, harvester_name):
        pass # need to increase the harvester_numbers variable by 1 at the desired index



class Harvester:
    def __init__(self, images, recovery_rate, price, location):
        self.images = images
        self.image = images[0] #the image that is actually going to shown at a given time
        self.location = location
        self.recovery_rate = recovery_rate
        self.price = price
        self.amount = 1


    def animate(self):
        pass


    def move(self, new_coods):
        self.location = new_coods


    def upgrade(self):
        self.recovery_rate *= 1.5


    def add_harvesters(self):
        self.number += 1
        self.recovery_rate += self.recovery_rate
        
class Seabin(Harvester):
    def __init__(self, location):
        # Call the constructor of the base class (Harvester)
        super().__init__(["seabin.png"], 100, 10000, location)
        
    def animate(self):
        pass #doesn't need to do anything as not animated

class Trash_wheel(Harvester):
    def __init__(self, location):
        # Call the constructor of the base class (Harvester)
        super().__init__(["trashwheel_1.png", "trashwheel_2.png", 
                          "trashwheel_3.png", "trashwheel_4.png"], 100, 10000, location)
        
    def animate(self):
        pass #doesn't need to do anything as not animated
        



def main():

    beach = BeachMap(POLLUTION_LEVEL)
