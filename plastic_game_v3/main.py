# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 13:27:05 2023

@author: Lillemoen
"""
# main.py
import pygame
import beachmap
import traceback

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 533
FPS = 60

def main():

    pygame.init()

    try:
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Plastic Harvesting Game")
    
        beach_map = beachmap.BeachMap(screen)
    
        clock = pygame.time.Clock()
    
        while True:
            events = pygame.event.get()
            beach_map.handle_events(events)
    
            beach_map.draw()
    
            pygame.display.flip()
            clock.tick(FPS)
            
    except Exception as e:
        traceback.print_exc()  # Print the stack trace
        pygame.quit()


if __name__ == "__main__":
    main()