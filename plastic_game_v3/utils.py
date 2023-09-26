# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 13:42:35 2023

@author: Lillemoen
"""
#utils.py
import pygame
import os

class Button:
    def __init__(self, x, y, width, height, color, text, action=None, responsive=True):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.action = action
        
        # Calculate the width based on the text length and add some padding
        if responsive:
            font = pygame.font.Font(None, 32)
            text_surface = font.render(self.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect()
            padding = 10  # adjust this for additional padding
            self.width = text_rect.width + 2 * padding
            self.height = text_rect.height + 0.2 * padding
            
        else:
            self.width = width
            self.height = height
        
        # Create the button rect based on the calculated width and height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 32)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def perform_action(self):
        if self.action is not None:
            self.action()

            
def image_selector(image):
    return os.path.join('images', image)

def info_selector(text_file):
    return os.path.join('infos', text_file)

def resize_image(image, size):
    new_width, new_height = size
    return pygame.transform.scale(image, (new_width, new_height))

def display_text(pygame_object, text, font, colour, position, temporary=False,
                 index=0, time=1500, top_right=False, top_left=False, line_spacing=30):
    """
    Multi-purpose function to display text on pygame screens

    Parameters
    ----------
    pygame_object
        The object we will be drawing on
    text : array of strings
        Each element will be on a new line
    font : pygame font
    colour : 3d tuple
        Colour of text
    position : 2d tuple
        x and y coordinates of where the text will be centred
    temporary : Boolean, optional
        DESCRIPTION. True if text only wants to be displayed for a set
        amount of time. The default is False.
    index : int, optional
        The index for the array of display timers. The default is 0.
    time : int, optional
        milliseconds the text is temporarily displayed for. The default is 1500.
    top_right : Boolean, optional
        True indicates position is set from top-right. The default is False.
    top_left : Boolean, optional
        True indicates position is set from top-left. The default is False.
    line_spacing : int, optional
        The default is 30.

    """
    for sentence in text:
        text_surface = font.render(sentence, True, colour)
        if top_right: 
            text_rect = text_surface.get_rect(topright=position)
        if top_left: 
            text_rect = text_surface.get_rect(topleft=position)
        else: 
            text_rect = text_surface.get_rect(center=position)
        
        pygame_object.screen.blit(text_surface, text_rect)
        position = (position[0], position[1] + line_spacing)
    
    if temporary:
        current_time = pygame.time.get_ticks()
        timer = pygame_object.display_timers[index][1]
        
        if timer is None:
            pygame_object.display_timers[index][1] = current_time
            
        else:
            elapsed_time = current_time - timer
            
            if elapsed_time > time:  # Display for 1.5 seconds by default
                pygame_object.display_timers[index][0] = False
                pygame_object.display_timers[index][1] = None
                
    