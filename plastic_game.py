import json
from typing import Union



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
        pass



class Harvester:
    def __init__(self, image, recovery_rate, price):
        self.image = image
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
        





def main():

    beach = BeachMap(POLLUTION_LEVEL)




    

