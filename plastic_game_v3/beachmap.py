# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 13:29:49 2023

@author: Lillemoen
"""

#beachmap.py

import pygame
import datetime
import sys
import os

import harvester
import utils
import menus

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 533
BUTTON_WIDTH, BUTTON_HEIGHT = 0.1*WINDOW_WIDTH, 0.046*WINDOW_HEIGHT
BUTTON_SPACING = 0.01*WINDOW_WIDTH
WHITE = (255, 255, 255)
GREY = (0,0,255)
BLACK = (0, 0, 0)
FPS = 60

class BeachMap:
    def __init__(self, screen):
        self.background_image = pygame.image.load(utils.image_selector("beach_background.png"))
        self.background_image = utils.resize_image(self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.harvesters = [harvester.Harvester(images, recovery_rate, price, location, name, size, speed)
                           for images, recovery_rate, price, location, name, size, speed in harvester.harvester_params]

        self.buttons = [
            utils.Button(0.0625*WINDOW_WIDTH, 0.1*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                   "Harvester Menu", self.open_harvester_menu),
            utils.Button(0.0625*WINDOW_WIDTH,  0.21*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT,
                   WHITE, "Main Menu", self.open_main_menu),
            utils.Button(0.0625*WINDOW_WIDTH,  0.32*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT,
                   WHITE, "Quiz", self.open_quiz),
            utils.Button(0.85*WINDOW_WIDTH, 0.9*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                   "Next", self.next_term)]
        
        self.screen = screen
        self.multiplier = 1.
        self.bank = 10000
        self.harvesters[4].amount += 1 #start off with a litter picker
        
        self.exchange_rate = 100 #1 ton of plastic is worth $100
        self.total_recovery_rate = self.calculate_total_recovery_rate()
        self.waste_rate = 8.e6 #tons of plastic released into ocean per year
        self.total_plastic = 1.5e8
        self.date = datetime.datetime(2023, 8, 1)
        
        self.quiz_completed = False
        self.display_timers =[[False, None], [False, None]] 
        # Designed for temporary displaying. First array is for quiz already being
        # completed and second is for quiz being unopened before pressing next.
        # The inner array refers to a boolean for it being pressed or not folllowed
        # by a timer to ensure the message closes after a certain time

    def calculate_total_recovery_rate(self):
        total_recovery_rate = 0
        for harvester in self.harvesters:
            total_recovery_rate += harvester.recovery_rate * harvester.amount
        return total_recovery_rate * self.multiplier
    
    def next_term(self):
        if self.quiz_completed:
            self.total_recovery_rate = self.calculate_total_recovery_rate()
            self.total_plastic += (self.waste_rate - self.total_recovery_rate) / 12
            self.bank += self.total_recovery_rate * self.exchange_rate
            self.multiplier = 1.
            self.quiz_completed = False
            if self.date.month == 12:  # If it's December, increment the year and set month to January
                self.date = self.date.replace(year=self.date.year + 1, month=1)
            else:
                self.date = self.date.replace(month=self.date.month + 1)
        else:
            self.display_timers[1][0] = True#display_quiz_unopened = True

    def open_harvester_menu(self):
        harvester_menu = menus.HarvesterMenu(self)
        self.run_sub_menu(harvester_menu)

    def open_main_menu(self):
        main_menu = menus.MainMenu(self)
        self.run_sub_menu(main_menu)

    def open_quiz(self):
        if not self.quiz_completed:
            quiz = menus.Quiz(self)
            self.run_sub_menu(quiz)
        else:
            self.display_timers[0][0] = True

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

    def move_harvesters(self):
        for harvester in self.harvesters:
            harvester.mover()

    def draw(self):
        surface = self.screen
        # Draw the background image
        surface.blit(self.background_image, (0, 0))

        # Draw the harvesters on top of the background
        for harvester in self.harvesters:
            if harvester.amount > 0:
                resized_image = utils.resize_image(harvester.image, harvester.size)
                surface.blit(resized_image, harvester.rect)

        # Draw the buttons on top of the background and harvesters
        for button in self.buttons:
            button.draw(surface)
            
        for harvester in self.harvesters:
            harvester.animate()  # Call the animate method to update

        self.move_harvesters()
        
        utils.display_text(self, ["${:.2f}".format(self.bank)], pygame.font.Font(None, 36),
                            (0, 100, 0), (WINDOW_WIDTH - 100, 20), top_right=True)
        
        utils.display_text(self, [self.date.strftime("%B %Y")], pygame.font.Font(None, 36),
                            (10, 10, 150), (10, 10), top_left=True)
        
        if self.display_timers[0][0]:
            utils.display_text(self, ["Quiz already completed!", "Proceed to next term."],
                                pygame.font.Font(None, 30), (255, 0, 0),
                                (0.84*WINDOW_WIDTH, WINDOW_HEIGHT * 0.14), 
                                temporary=True, index=0)
        
        if self.display_timers[1][0]:
            utils.display_text(self, ["Complete quiz before the next term!"],
                                pygame.font.Font(None, 30), (255, 0, 0),
                                (0.74*WINDOW_WIDTH, WINDOW_HEIGHT * 0.14), 
                                temporary=True, index=1)
        
                        
    
        
        