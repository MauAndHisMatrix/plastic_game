# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 13:35:14 2023

@author: Lillemoen
"""
#menus.py

import pygame
import sys
import json

import quiz_questions
import utils

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 533
BUTTON_WIDTH, BUTTON_HEIGHT = 0.1*WINDOW_WIDTH, 0.046*WINDOW_HEIGHT
BUTTON_SPACING = 0.01*WINDOW_WIDTH
WHITE = (255, 255, 255)
GREY = (0,0,255)
BLACK = (0, 0, 0)
FPS = 60

class Quiz:
    def __init__(self, beach_map):
        self.beach_map = beach_map
        self.background_image = pygame.image.load(utils.image_selector("beach_background.png"))
        self.background_image = utils.resize_image(
            self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.questions_bank = quiz_questions.get_random_questions(
            quiz_questions.questions_dict)
        self.question_data = {'current_question_number': 1,
        'Correct Answers': 0, 'Incorrect Answers': 0}
        self.screen = self.beach_map.screen
        
        pygame.display.set_caption("Quiz")
        
        # open a file for writing
        with open('question_data.json', 'w') as f:
            # write the dictionary to the file in JSON format
            json.dump(self.question_data, f)
        

    def get_question_tuple(self):
        data = dict()
        with open('question_data.json', 'r') as file:
            data = json.load(file)
        return data

    def write_question_tuple(self, question_data):
        with open('question_data.json', 'w') as f:
            # write the dictionary to the file in JSON format
            json.dump(question_data, f)

    def create_buttons(self, current_question_number):
        if current_question_number < 6:
            self.question_buttons = [
                utils.Button(0.23*WINDOW_WIDTH, 0.66*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                       "A", lambda: self.check_answer(1, current_question_number), False),
                utils.Button(0.38*WINDOW_WIDTH, 0.66*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                       "B", lambda: self.check_answer(2, current_question_number), False),
                utils.Button(0.54*WINDOW_WIDTH, 0.66*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                       "C", lambda: self.check_answer(3, current_question_number), False),
                utils.Button(0.70*WINDOW_WIDTH, 0.66*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT,
                       WHITE, "D", lambda: self.check_answer(4, current_question_number), False),
                utils.Button(0.83*WINDOW_WIDTH, 0.93*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                       "Back", self.open_beach_map)
            ]
        else:
            self.question_buttons = [utils.Button(0.46*WINDOW_WIDTH, 0.56*WINDOW_HEIGHT, 
                    BUTTON_WIDTH, BUTTON_HEIGHT, WHITE, "Back", self.open_beach_map)]

        return self.question_buttons

    def check_answer(self, answer, current_question_number):
        mark = self.questions_bank[current_question_number][-1] == answer
        data = self.get_question_tuple()

        data["current_question_number"] += 1

        if mark:
            data["Correct Answers"] += 1
        elif not mark:
            data["Incorrect Answers"] += 1

        self.write_question_tuple(data)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            try:
                for button in self.buttons:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            pos = pygame.mouse.get_pos()
                            if button.is_clicked(pos):
                                button.perform_action()
            except AttributeError:
                pass

    def draw(self, surface):
        surface.fill((0, 0, 0)) #have to create new surface to remove previous one
        surface.blit(self.background_image, (0, 0))

        data = self.get_question_tuple()
        current_question_number, correct_answers, incorrect_answers = data[
            "current_question_number"], data["Correct Answers"], data["Incorrect Answers"]

        try:
            quiz_text = self.questions_bank[current_question_number][0]
            quiz_font = pygame.font.Font(None, 30)
            max_text_width = WINDOW_WIDTH - 100  # Allow 100 pixels margin on each side
            quiz_lines = []
            words = quiz_text.split()

            current_line = ""
            for word in words:
                test_line = current_line + word + " "
                test_line_surface = quiz_font.render(test_line, True, GREY)

                if test_line_surface.get_width() <= max_text_width:
                    current_line = test_line
                else:
                    quiz_lines.append(current_line)
                    current_line = word + " "

            # Add the last line
            if current_line:
                quiz_lines.append(current_line)

            # Set the y_offset for the quiz text to position it at the top of the screen
            y_offset = 50

            utils.display_text(self, quiz_lines, quiz_font, (0,0,255),
                               (WINDOW_WIDTH // 2, y_offset))
            
            y_offset += 30 * len(quiz_lines) + 30 #ensure quiz answers below question

            # Display the answers under each other
            question_answers = [self.questions_bank[current_question_number][1],
                                self.questions_bank[current_question_number][2],
                                self.questions_bank[current_question_number][3],
                                self.questions_bank[current_question_number][4]]

            question_font = pygame.font.Font(None, 30)
            
            utils.display_text(self, question_answers, question_font, (0,0,255),
                               (WINDOW_WIDTH // 2, y_offset), line_spacing=35)

            answers_text = f"Correct Answers: {correct_answers}    Incorrect Answers: {incorrect_answers}"
            utils.display_text(self, [answers_text], pygame.font.Font(None, 30),
                               (0,0,255), (250, WINDOW_HEIGHT * 9//10))

            self.buttons = self.create_buttons(current_question_number)
            for button in self.buttons:
                button.draw(surface)
        
        except KeyError:

            utils.display_text(self, ["End of Quiz"], pygame.font.Font(None, 50),
                               (0,0,255), (0.5*WINDOW_WIDTH, WINDOW_HEIGHT * 0.4))          
            
            answers_text = f"Correct Answers: {correct_answers}    Incorrect Answers: {incorrect_answers}"
            utils.display_text(self, [answers_text], pygame.font.Font(None, 30),
                               (0,0,255), (250, WINDOW_HEIGHT * 9//10))

            self.buttons = self.create_buttons(current_question_number)
            for button in self.buttons:
                button.draw(surface)

    def open_beach_map(self):
        self.beach_map.multiplier = pow(2, self.get_question_tuple()["Correct Answers"]-1)#1 + self.get_question_tuple()["Correct Answers"] * 0.1
        if self.get_question_tuple()["current_question_number"] > 5:
            self.beach_map.quiz_completed = True
        clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            self.beach_map.handle_events(events)

            self.beach_map.draw()

            pygame.display.flip()
            clock.tick(FPS)

class HarvesterMenu:
    def __init__(self, beach_map):
        self.beach_map = beach_map
        self.screen = self.beach_map.screen
        
        self.background_image = pygame.image.load(utils.image_selector("beach_background.png"))
        self.background_image = utils.resize_image(
            self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.file_paths = ['seabin_info.txt', 'WasteShark_info.txt', 'trashwheel_info.txt',
                           'HO_wrack_info.txt', 'litter_picker_info.txt', 'litterboon_info.txt']
        self.harvester_info = [self.load_text_from_file(utils.info_selector(file_path)) for file_path in self.file_paths]
        
        self.harvester_buttons = []
        for i in range(0, 6):
            self.harvester_buttons.append(self.Harvester_button(self.beach_map, 0.1*WINDOW_WIDTH, (0.16*(i+1)-0.14)*WINDOW_HEIGHT,
                self.beach_map.harvesters[i], self.harvester_info[i]))
        
        self.buttons = [utils.Button(0.83*WINDOW_WIDTH, 0.93*WINDOW_HEIGHT, BUTTON_WIDTH,
                               BUTTON_HEIGHT, WHITE, "Back", self.open_beach_map)]
        
        pygame.display.set_caption("Harvester Menu")
        
    def load_text_from_file(self, file_path):
            with open(file_path, 'r') as file:
                text = file.read()
            return text
    
    class Harvester_button:
        def __init__(self, beach_map, x, y, harvester, info):
            self.beach_map = beach_map
            self.screen = self.beach_map.screen
            self.rect = pygame.Rect(x, y, 0.4*WINDOW_WIDTH, 0.1*WINDOW_HEIGHT)
            self.harvester = harvester
            self.info = info
      
            self.display_timers =[[False, None]] # first element refers to not
            # enough money, second is the timer
            
            self.buy_button = utils.Button(x, y + 0.1*WINDOW_HEIGHT, 0.075*WINDOW_WIDTH, 
                                     0.056*WINDOW_HEIGHT, (255, 0, 0), "Buy", self.update_harvesters)
            self.info_button = utils.Button(x + 0.075*WINDOW_WIDTH, y + 0.1*WINDOW_HEIGHT, 0.075*WINDOW_WIDTH, 
                                      0.056*WINDOW_HEIGHT, (0, 0, 255), "Info", self.toggle_info)
            
            self.show_info = False
        
        def wrap_text(self, text, max_width):
            font = pygame.font.Font(None, 24)
            words = text.split()
            lines = []
            current_line = words[0]
            
            for word in words[1:]:
                test_line = current_line + ' ' + word
                test_width, _ = font.size(test_line)
                
                if test_width <= max_width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word
            
            if current_line:
                lines.append(current_line)
    
            return lines
        
        def render_wrapped_text(self, surface, text, rect):
            lines = self.wrap_text(text, rect.width)
            
            font = pygame.font.Font(None, 24)
            y = rect.top
            for line in lines:
                text_surface = font.render(line, True, (0, 0, 0))
                text_rect = text_surface.get_rect(topleft=(rect.left, y))
                surface.blit(text_surface, text_rect)
                y += font.get_linesize()
    
        
        def draw(self, surface):
            ## Custom draw method for a Harvester button from scratch
            pygame.draw.rect(surface, (0, 255, 0), self.rect)
            font = pygame.font.Font(None, 20)
            title_font = pygame.font.Font(None, int(20 * 1.5))  # Increase font size by 1.5 times
            
            text_y = self.rect.top + 5
            text_spacing = 5
            
            # Draw the name with a bigger and more titular font
            title_text_surface = title_font.render(self.harvester.name, True, (0, 0, 0))
            title_text_rect = title_text_surface.get_rect(topleft=(self.rect.left + 20, text_y))
            surface.blit(title_text_surface, title_text_rect)
            
            # Draw the current amount next to the name
            current_amount_text = f"Current Amount: {self.harvester.amount}"
            current_amount_text_surface = font.render(current_amount_text, True, (0, 0, 0))
            current_amount_text_rect = current_amount_text_surface.get_rect(topleft=(title_text_rect.right + 10, text_y))
            surface.blit(current_amount_text_surface, current_amount_text_rect)
            
            text_y += title_text_surface.get_height() + text_spacing
            
            # Draw Price and Recovery Rate texts next to each other
            price_text = f"Price: ${self.harvester.price}"
            recovery_rate_text = f"Recovery Rate: {self.harvester.recovery_rate} ton/year"
            price_text_surface = font.render(price_text, True, (0, 0, 0))
            recovery_rate_text_surface = font.render(recovery_rate_text, True, (0, 0, 0))
            
            price_text_rect = price_text_surface.get_rect(topleft=(self.rect.left + 20, text_y))
            recovery_rate_text_rect = recovery_rate_text_surface.get_rect(topright=(self.rect.right - 20, text_y))
            
            surface.blit(price_text_surface, price_text_rect)
            surface.blit(recovery_rate_text_surface, recovery_rate_text_rect)
            
            # Draw buttons
            self.buy_button.draw(surface)
            self.info_button.draw(surface)
    
            # Draw info box if needed
            if self.show_info:
                self.draw_info_box(surface)
   
            # Temporary message if not enough money
            if self.display_timers[0][0]:
                utils.display_text(self, ["Not enough money!"], pygame.font.Font(None, 30),
                                   (255, 0, 0), (0.84*WINDOW_WIDTH, WINDOW_HEIGHT * 0.14),
                                   temporary=True, time=800)
                
        def toggle_info(self):
            self.show_info = not self.show_info

        def draw_info_box(self, surface):
            text_box_rect = pygame.Rect(self.rect.left+0.4*WINDOW_WIDTH+10, 0.1*WINDOW_HEIGHT, self.rect.width, 0.8*WINDOW_HEIGHT)
            self.render_wrapped_text(surface, self.info, text_box_rect)
            
        def update_harvesters(self):
            if self.harvester.price <= self.beach_map.bank:
                self.harvester.amount += 1 #need this to be connected to beach_map
                self.beach_map.bank -= self.harvester.price
            else:
                self.display_timers[0][0] = True #not enough money
    
        def handle_events(self, events):
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                try:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if self.buy_button.rect.collidepoint(pos):
                            self.buy_button.perform_action()
                        if self.info_button.rect.collidepoint(pos):
                            self.info_button.perform_action()
                except AttributeError:
                    pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            try:
                for button in self.buttons:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            pos = pygame.mouse.get_pos()
                            if button.is_clicked(pos):
                                button.perform_action()
            except AttributeError:
                pass
            
        for harvester_button in self.harvester_buttons:
            harvester_button.handle_events(events)

    def draw(self, surface):
        surface.fill((0, 0, 0))
        surface.blit(self.background_image, (0, 0))

        for button in self.buttons:
            button.draw(surface)
            
        for harvester_button in self.harvester_buttons:
            harvester_button.draw(surface)
            
        formatted_bank = "${:.2f}".format(self.beach_map.bank)  # Format the bank amount with two decimal places
        utils.display_text(self, [formatted_bank], pygame.font.Font(None, 36),
                           (0,100,0), (WINDOW_WIDTH - 100, 20), top_right=True)

    def open_beach_map(self):
        clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            self.beach_map.handle_events(events)

            self.beach_map.draw()

            pygame.display.flip()
            clock.tick(FPS)
            
class MainMenu:
    def __init__(self, beach_map):
        self.beach_map = beach_map
        self.screen = self.beach_map.screen
        self.background_image = pygame.image.load(utils.image_selector("beach_background.png"))
        self.background_image = utils.resize_image(
            self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.buttons = [utils.Button(0.84*WINDOW_WIDTH, 0.9*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                               "Back", self.open_beach_map),
                        utils.Button(0.6*WINDOW_WIDTH, 0.6*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                               "Load Game"),
                        utils.Button(0.7*WINDOW_WIDTH, 0.7*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                               "Save Game"),
                        utils.Button(0.5*WINDOW_WIDTH, 0.5*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                               "Exit Game", self.exit_game)]
        
        pygame.display.set_caption("Main Menu")
        
        #self.sliders = [Slider("Sound Control")] # to be made

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            try:
                for button in self.buttons:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            pos = pygame.mouse.get_pos()
                            if button.is_clicked(pos):
                                button.perform_action()
            except AttributeError:
                pass

    def draw(self, surface):

        surface.fill((0, 0, 0))
        surface.blit(self.background_image, (0, 0))
        font = pygame.font.Font(None, 40)
        text_spacing = 30

        for button in self.buttons:
            button.draw(surface)
            
        variable_names = [
            ("Total Recovery Rate (ton/year)", self.beach_map.calculate_total_recovery_rate()/self.beach_map.multiplier),
            ("Total Plastic (ton)", self.beach_map.total_plastic),
            ("Multiplier", self.beach_map.multiplier),
            ("Exchange Rate ($/ton)", self.beach_map.exchange_rate),#"${:.2f}".format(self.bank)
            ("Waste Rate (ton/year)", self.beach_map.waste_rate)
        ]
        
        for idx, (name, value) in enumerate(variable_names):
            text = f"{name}: {value:.1f}"
            text_surface = font.render(text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(topleft=(10, 50 + idx * text_spacing))
            surface.blit(text_surface, text_rect)
        
        utils.display_text(self, ["${:.2f}".format(self.beach_map.bank)], pygame.font.Font(None, 36),
                            (0, 100, 0), (WINDOW_WIDTH - 100, 20), top_right=True)
        
        utils.display_text(self, [self.beach_map.date.strftime("%B %Y")], pygame.font.Font(None, 36),
                            (10, 10, 150), (10, 10), top_left=True)

    def open_beach_map(self):
        clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            self.beach_map.handle_events(events)

            self.beach_map.draw()

            pygame.display.flip()
            clock.tick(FPS)
