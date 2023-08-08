# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 19:32:51 2023

@author: Lillemoen
"""

import pygame
import sys
import json
import time
import random
import datetime
import textwrap

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 533
#WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
BUTTON_WIDTH, BUTTON_HEIGHT = 0.1*WINDOW_WIDTH, 0.046*WINDOW_HEIGHT
BUTTON_SPACING = 0.01*WINDOW_WIDTH
WHITE = (255, 255, 255)
GREY = (0,0,255)
BLACK = (0, 0, 0)
FPS = 60

questions_dict = {
    1: ("What is the primary source of plastic pollution in the oceans?",
        "a) Industrial waste",
        "b) Landfill runoff",
        "c) Single-use plastics and litter",
        "d) Oil spills",
        3),
    2: ("Which of the following plastics is most commonly found in marine litter?",
        "a) PET (Polyethylene terephthalate)",
        "b) PVC (Polyvinyl chloride)",
        "c) PP (Polypropylene)",
        "d) PS (Polystyrene)",
        3),
    3: ("How long does it take for a plastic bag to decompose in the environment?",
        "a) 1 year",
        "b) 10 years",
        "c) 100 years",
        "d) 1000 years",
        4),
    4: ("Which oceanic region is infamous for the 'Great Pacific Garbage Patch,' a large accumulation of marine debris?",
        "a) Atlantic Ocean",
        "b) Indian Ocean",
        "c) Pacific Ocean",
        "d) Southern Ocean",
        3),
    5: ("What are microplastics?",
        "a) Large plastic items floating on the ocean surface",
        "b) Plastic particles less than 1 millimeter in size",
        "c) A type of biodegradable plastic",
        "d) Plastic waste collected from beaches",
        2),
    6: ("How do plastic microbeads primarily enter water bodies?",
        "a) Released from industrial facilities",
        "b) Naturally occurring in the environment",
        "c) Found in seafood and consumed by marine animals",
        "d) Found in personal care products like exfoliating scrubs",
        4),
    7: ("What percentage of marine animals are estimated to have ingested plastic debris?",
        "a) Less than 10%",
        "b) About 25%",
        "c) Around 50%",
        "d) Over 80%",
        4),
    8: ("What is the main threat of plastic pollution to marine life?",
        "a) Habitat destruction",
        "b) Disruption of food chains",
        "c) Increase in ocean acidity",
        "d) Depletion of oxygen levels",
        2),
    9: ("Which international event aims to raise awareness and combat plastic pollution by encouraging people to reduce single-use plastics?",
        "a) World Environment Day",
        "b) Earth Hour",
        "c) International Plastic Bag Free Day",
        "d) Global Recycling Day",
        3),
    10: ("What is a possible solution to reduce plastic pollution?",
         "a) Incinerating plastic waste",
         "b) Promoting the use of single-use plastics",
         "c) Implementing better waste management and recycling systems",
         "d) Dumping plastic waste into oceans",
         3),
    11: ("Which country is the largest contributor to plastic pollution in the ocean?",
         "a) China",
         "b) United States",
         "c) India",
         "d) Indonesia",
         1),
    12: ("Which type of plastic is commonly used for single-use water bottles?",
         "a) HDPE (High-Density Polyethylene)",
         "b) LDPE (Low-Density Polyethylene)",
         "c) PVC (Polyvinyl chloride)",
         "d) PET (Polyethylene terephthalate)",
         4),
    13: ("What percentage of plastic waste is estimated to be recycled globally?",
         "a) Less than 10%",
         "b) Around 25%",
         "c) Approximately 50%",
         "d) Over 75%",
         1),
    14: ("Which sea animal is commonly affected by plastic pollution, mistaking it for jellyfish and consuming it?",
         "a) Sea turtles",
         "b) Dolphins",
         "c) Sharks",
         "d) Jellyfish",
         1),
    15: ("What are 'nurdles' in the context of plastic pollution?",
         "a) Small plastic beads used in personal care products",
         "b) Plastic pellets used as raw material in plastic production",
         "c) Microplastics found in the deep ocean",
         "d) Plastic debris washed ashore on beaches",
         2),
    16: ("How does plastic pollution affect coral reefs?",
         "a) Enhances their growth and resilience",
         "b) Provides a new habitat for marine species",
         "c) Causes bleaching and disrupts their ecosystem",
         "d) Traps nutrients and aids in their survival",
         3),
    17: ("Which international agreement aims to address plastic pollution by minimizing land-based sources of marine debris?",
         "a) The Paris Agreement",
         "b) The Basel Convention",
         "c) The Stockholm Convention",
         "d) The Honolulu Strategy",
         2),
    18: ("How does plastic pollution impact human health?",
         "a) It causes skin rashes and allergies",
         "b) Plastic particles are absorbed through the skin",
         "c) Consuming seafood contaminated with microplastics",
         "d) It has no direct impact on human health",
         3),
    19: ("Which country became the first to ban single-use plastics nationwide in 2020?",
         "a) France",
         "b) Canada",
         "c) Costa Rica",
         "d) Kenya",
         4),
    20: ("What is the term for the breakdown of plastic into smaller particles due to exposure to environmental factors?",
         "a) Photodegradation",
         "b) Biodegradation",
         "c) Desintegration",
         "d) Microfragmentation",
         1),
    21: ("What is the name of the process where plastics break down into smaller particles and enter the food chain?",
         "a) Polymerization",
         "b) Bioaccumulation",
         "c) Leaching",
         "d) Biomagnification",
         2),
    22: ("Which type of plastic is commonly used in grocery bags and food packaging?",
         "a) PVC (Polyvinyl chloride)",
         "b) HDPE (High-Density Polyethylene)",
         "c) PS (Polystyrene)",
         "d) PP (Polypropylene)",
         2),
    23: ("Which organization launched the 'Trash Free Seas' program to combat plastic pollution in the oceans?",
         "a) Greenpeace",
         "b) World Wildlife Fund (WWF)",
         "c) National Oceanic and Atmospheric Administration (NOAA)",
         "d) The Ocean Cleanup",
         3),
    24: ("How do plastic bags affect marine animals when ingested?",
         "a) They provide valuable nutrients",
         "b) They act as a toxin neutralizer",
         "c) They block digestive tracts and cause suffocation",
         "d) They have no harmful effects",
         3),
    25: ("What is the main challenge in recycling mixed plastic waste?",
         "a) The high cost of recycling facilities",
         "b) Lack of demand for recycled plastic products",
         "c) Difficulty in separating different types of plastics",
         "d) The energy-intensive recycling process",
         3),
    26: ("Which international agreement aims to protect the marine environment from ship-based pollution, including plastic waste disposal?",
         "a) The Montreal Protocol",
         "b) The International Convention for the Prevention of Pollution from Ships (MARPOL)",
         "c) The Cartagena Protocol",
         "d) The Rotterdam Convention",
         2),
    27: ("Which alternative material is increasingly used as a more eco-friendly substitute for single-use plastics?",
         "a) Paper",
         "b) Metal",
         "c) Glass",
         "d) Biodegradable plastic",
         4),
    28: ("How can individuals help reduce plastic pollution?",
         "a) Reusing plastic items as much as possible",
         "b) Using only biodegradable plastics",
         "c) Burning plastic waste in open fires",
         "d) Disposing of plastic waste in the ocean",
         1),
    29: ("Which region of the world has the highest concentration of microplastics in seawater?",
         "a) North Atlantic",
         "b) Mediterranean Sea",
         "c) South Pacific",
         "d) Arctic Ocean",
         2),
    30: ("What is 'ghost fishing' in the context of plastic pollution?",
         "a) Fishing for ghost crabs to reduce plastic pollution",
         "b) Fishing with biodegradable nets to minimize waste",
         "c) Abandoned fishing gear continuing to trap and kill marine life",
         "d) Using fishing boats powered by renewable energy",
         3),
    31: ("What is the name of the process by which plastic breaks down into smaller particles and becomes more susceptible to attracting and absorbing pollutants?",
         "a) Leaching",
         "b) Bioaccumulation",
         "c) Hydrolysis",
         "d) Sorption",
         4),
    32: ("Which of the following items is NOT typically made from microplastics?",
         "a) Facial scrubs",
         "b) Clothing fibers",
         "c) Plastic bottles",
         "d) Paints and coatings",
         3),
    33: ("Which type of plastic is commonly used in food containers and yogurt cups?",
         "a) PET (Polyethylene terephthalate)",
         "b) HDPE (High-Density Polyethylene)",
         "c) PS (Polystyrene)",
         "d) PP (Polypropylene)",
         4),
    34: ("How can plastic pollution impact marine ecosystems?",
         "a) Enhance biodiversity in marine habitats",
         "b) Improve water quality and clarity",
         "c) Disrupt the balance of marine ecosystems",
         "d) Promote the growth of coral reefs",
         3),
    35: ("What is the name of the process by which plastic debris is transported from coastlines to remote areas by ocean currents?",
         "a) Plastic drift",
         "b) Marine litter transport",
         "c) Oceanic displacement",
         "d) Beaching",
         2),
    36: ("Which country implemented a law banning single-use plastic bags, styrofoam, and plastic utensils in 2019?",
         "a) Australia",
         "b) United Kingdom",
         "c) Japan",
         "d) Jamaica",
         4),
    37: ("How does plastic pollution affect seabirds?",
         "a) Improves their nesting habitats",
         "b) Provides additional food sources",
         "c) Causes entanglement and ingestion leading to injury and death",
         "d) It has no impact on seabird populations",
         3),
    38: ("What is the name of the technique used to remove plastic debris from the water surface by using floating barriers to collect and concentrate the waste?",
         "a) Marine vacuuming",
         "b) Plastics capture and retrieval",
         "c) Skimming and containment",
         "d) Ocean garbage collecting",
         3),
    39: ("Which type of plastic is commonly used in bottle caps and food containers?",
         "a) PVC (Polyvinyl chloride)",
         "b) HDPE (High-Density Polyethylene)",
         "c) LDPE (Low-Density Polyethylene)",
         "d) PP (Polypropylene)",
         4),
    40: ("How do abandoned fishing nets contribute to plastic pollution in the oceans?",
         "a) They act as artificial reefs, enhancing marine biodiversity",
         "b) They provide food for marine animals",
         "c) They continue to trap and kill marine life (ghost fishing)",
         "d) They break down quickly and decompose harmlessly",
         3),
    41: ("What is the name of the international treaty that aims to protect human health and the environment from the harmful effects of persistent organic pollutants (POPs), including certain plastic additives?",
         "a) The Paris Agreement",
         "b) The Rotterdam Convention",
         "c) The Stockholm Convention",
         "d) The Basel Convention",
         3),
    42: ("Which type of plastic is commonly used in foam cups and takeaway food containers?",
         "a) PET (Polyethylene terephthalate)",
         "b) PS (Polystyrene)",
         "c) HDPE (High-Density Polyethylene)",
         "d) PVC (Polyvinyl chloride)",
         2),
    43: ("Which alternative material is increasingly used as a more eco-friendly substitute for single-use plastics?",
         "a) Paper",
         "b) Metal",
         "c) Glass",
         "d) Biodegradable plastic",
         4),
    44: ("How can governments and industries work together to combat plastic pollution effectively?",
         "a) Implementing stricter regulations on plastic production and usage",
         "b) Encouraging consumers to use more single-use plastics",
         "c) Ignoring the issue and focusing on other environmental concerns",
         "d) Investing in plastic manufacturing to boost the economy",
         1),
    45: ("Which region of the world has the highest concentration of microplastics in seawater?",
         "a) North Atlantic",
         "b) Mediterranean Sea",
         "c) South Pacific",
         "d) Arctic Ocean",
         2),
    46: ("What is 'ghost fishing' in the context of plastic pollution?",
         "a) Fishing for ghost crabs to reduce plastic pollution",
         "b) Fishing with biodegradable nets to minimize waste",
         "c) Abandoned fishing gear continuing to trap and kill marine life",
         "d) Using fishing boats powered by renewable energy",
         3),
    47: ("What is the name of the process by which plastic breaks down into smaller particles and becomes more susceptible to attracting and absorbing pollutants?",
         "a) Leaching",
         "b) Bioaccumulation",
         "c) Hydrolysis",
         "d) Sorption",
         4),
    48: ("Which of the following items is NOT typically made from microplastics?",
         "a) Facial scrubs",
         "b) Clothing fibers",
         "c) Plastic bottles",
         "d) Paints and coatings",
         3),
    49: ("Which type of plastic is commonly used in food containers and yogurt cups?",
         "a) PET (Polyethylene terephthalate)",
         "b) HDPE (High-Density Polyethylene)",
         "c) PS (Polystyrene)",
         "d) PP (Polypropylene)",
         4),
    50: ("How can plastic pollution impact marine ecosystems?",
         "a) Enhance biodiversity in marine habitats",
         "b) Improve water quality and clarity",
         "c) Disrupt the balance of marine ecosystems",
         "d) Promote the growth of coral reefs",
         3),
}

# create a Python dictionary
data = {'current_question_number': 1,
        'Correct Answers': 0, 'Incorrect Answers': 0}
    
def get_random_questions(question_dict):
    selected_keys = random.sample(list(question_dict.keys()), 5)
    selected_questions = [question_dict[key] for key in selected_keys]

    random_questions_dict = {}
    for i, (question, option1, option2, option3, option4, correct_answer) in enumerate(selected_questions, start=1):
        question_data = (
            question,
            option1,
            option2,
            option3,
            option4,
            correct_answer
        )
        random_questions_dict[i] = question_data

    return random_questions_dict


class Quiz:
    def __init__(self, beach_map):
        self.beach_map = beach_map
        self.background_image = pygame.image.load("beach_background.png")
        self.background_image = self.resize_image(
            self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.questions_bank = get_random_questions(questions_dict)
        self.question_data = {'current_question_number': 1,
        'Correct Answers': 0, 'Incorrect Answers': 0}
        
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
                Button(0.23*WINDOW_WIDTH, 0.66*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                       "A", lambda: self.check_answer(1, current_question_number)),
                Button(0.38*WINDOW_WIDTH, 0.66*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                       "B", lambda: self.check_answer(2, current_question_number)),
                Button(0.54*WINDOW_WIDTH, 0.66*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                       "C", lambda: self.check_answer(3, current_question_number)),
                Button(0.70*WINDOW_WIDTH, 0.66*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT,
                       WHITE, "D", lambda: self.check_answer(4, current_question_number)),
                Button(0.83*WINDOW_WIDTH, 0.93*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                       "Back", self.open_beach_map)
            ]
        else:
            self.question_buttons = [Button(0.46*WINDOW_WIDTH, 0.56*WINDOW_HEIGHT, 
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

    def resize_image(self, image, size):
        aspect_ratio = image.get_width() / image.get_height()
        new_width, new_height = size
        # new_height = int(new_width / aspect_ratio)
        # if new_height > size[1]:
        #     new_height = size[1]
        #     new_width = int(new_height * aspect_ratio)
        return pygame.transform.scale(image, (new_width, new_height))

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

            # Calculate the total height of the quiz text
            total_text_height = len(quiz_lines) * 30

            # Set the y_offset for the quiz text to position it at the top of the screen
            y_offset = 50

            for line in quiz_lines:
                quiz_text_surface = quiz_font.render(line, True, GREY)
                quiz_text_rect = quiz_text_surface.get_rect(
                    center=(WINDOW_WIDTH // 2, y_offset))
                surface.blit(quiz_text_surface, quiz_text_rect)
                y_offset += 30  # Adjust the spacing between lines

            # Display the answers under each other
            question_answers = [self.questions_bank[current_question_number][1],
                                self.questions_bank[current_question_number][2],
                                self.questions_bank[current_question_number][3],
                                self.questions_bank[current_question_number][4]]

            question_font = pygame.font.Font(None, 30)
            y_offset += 30  # Add some spacing between the quiz text and answers

            for answer in question_answers:
                answer_text_surface = question_font.render(answer, True, GREY)
                answer_text_rect = answer_text_surface.get_rect(
                    center=(WINDOW_WIDTH // 2, y_offset))
                surface.blit(answer_text_surface, answer_text_rect)
                y_offset += 30  # Adjust the spacing between lines

            answers_text = f"Correct Answers: {correct_answers}    Incorrect Answers: {incorrect_answers}"
            answers_font = pygame.font.Font(None, 30)
            answers_text_surface = answers_font.render(
                answers_text, True, GREY)
            answers_text_rect = answers_text_surface.get_rect(
                center=(250, WINDOW_HEIGHT * 9//10))
            surface.blit(answers_text_surface, answers_text_rect)

            self.buttons = self.create_buttons(current_question_number)

            for button in self.buttons:
                button.draw(surface)
        except KeyError:

            done_text = "End of Quiz"
            done_font = pygame.font.Font(None, 50)
            done_text_surface = done_font.render(done_text, True, GREY)
            done_text_rect = done_text_surface.get_rect(
                center=(0.5*WINDOW_WIDTH, WINDOW_HEIGHT * 0.4))
            surface.blit(done_text_surface, done_text_rect)
            
            answers_text = f"Correct Answers: {correct_answers}    Incorrect Answers: {incorrect_answers}"
            answers_font = pygame.font.Font(None, 30)
            answers_text_surface = answers_font.render(
                answers_text, True, GREY)
            answers_text_rect = answers_text_surface.get_rect(
                center=(250, WINDOW_HEIGHT * 9//10))
            surface.blit(answers_text_surface, answers_text_rect)

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


class HarvesterMenu:
    def __init__(self, beach_map):
        self.beach_map = beach_map
        
        self.background_image = pygame.image.load("beach_background.png")
        self.background_image = self.resize_image(
            self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.file_paths = ['seabin_info.txt', 'WasteShark_info.txt', 'trashwheel_info.txt',
                           'HO_wrack_info.txt', 'litter_picker_info.txt', 'litterboon_info.txt']
        self.harvester_info = [self.load_text_from_file(file_path) for file_path in self.file_paths]
        # self.harvester_info = ["Seabin represents a cutting-edge solution in the battle against marine litter and plastic pollution. This compact yet highly effective device is strategically placed in marinas, harbors, and busy waters, where it tirelessly filters and collects floating debris, plastics, and microplastics from the water's surface. Operating like a floating garbage bin, the Seabin's pump draws water in, capturing waste while allowing clean water to flow out. Its simple yet innovative design showcases the potential of localized initiatives to make a tangible impact on marine conservation. By addressing the issue of plastic pollution at its source, Seabin exemplifies how innovative technologies can contribute to cleaner oceans and inspire a global movement towards more sustainable maritime practices.",
        #                         "WasteShark stands as a groundbreaking aquatic solution at the forefront of tackling waterborne waste and pollution. This autonomous surface water drone operates adeptly in harbors and other aquatic environments, skillfully skimming the water's surface to remove debris, plastics, and other contaminants before they can further harm marine ecosystems. With a design inspired by marine life, WasteShark seamlessly navigates through waterways, collecting waste and transmitting real-time data on water quality. Its innovative approach underscores the potential of technology-driven solutions to safeguard our oceans and water bodies, offering a glimpse into a future where cleaner, healthier aquatic ecosystems can flourish.", 
        #                         "Mr. Trash Wheel is a pioneering solar-powered water wheel renowned for its effective role in mitigating plastic pollution and maintaining cleaner water bodies. Operating in rivers and harbors, this innovative device utilizes water currents to collect debris, from plastic bottles to waste, preventing their entry into oceans. Its eye-catching appearance, often adorned with googly eyes, adds an engaging element to environmental conservation. Serving as a symbol of innovation, Mr. Trash Wheel highlights the potential of inventive solutions in addressing pressing environmental challenges and inspiring global efforts toward a more sustainable future",
        #                         "Hoola One emerges as a trailblazing solution in the realm of beach cleaning and sand restoration. This state-of-the-art machine is engineered to meticulously sift through sand, extracting microplastics, debris, and other pollutants that threaten the coastal ecosystem. Utilizing advanced sieving and filtration mechanisms, Hoola One adeptly separates harmful materials from the sand, leaving behind a cleaner and more pristine shoreline. Its innovative technology showcases the potential of automation in environmental preservation, underscoring the importance of safeguarding our beaches and coastal environments. Hoola One's contribution not only fosters a healthier habitat for marine life but also serves as an inspiring example of how cutting-edge engineering can foster sustainable practices and elevate the global effort to combat plastic pollution at the water's edge.",
        #                         "Beach litter-pickers embody the dedicated individuals who play a vital role in preserving our coastal landscapes. Armed with a sense of environmental responsibility and a passion for keeping our beaches pristine, these volunteers and workers tirelessly patrol shorelines, collecting discarded waste, plastic debris, and litter that pose a threat to marine ecosystems. With each deliberate movement, beach litter-pickers contribute to the restoration of natural beauty and the protection of diverse marine life. Their commitment shines a spotlight on the power of community engagement and individual action in creating positive change. By embodying the spirit of stewardship, beach litter-pickers inspire others to join the effort and collectively ensure that our beaches remain a haven for both people and nature alike.",
        #                         "The LitterBoon Project harnesses cutting-edge technology to combat plastic pollution by employing strategically positioned floating barriers armed with advanced collection systems. These innovative booms are designed to efficiently intercept and capture debris and plastic waste from water bodies, preventing their entry into oceans and rivers. Equipped with sensor-driven data collection, the technology provides real-time insights into waste accumulation patterns, enabling informed environmental management decisions. The LitterBoon's fusion of engineering excellence and environmental consciousness embodies a visionary approach, showcasing how technology-driven solutions can revolutionize the fight against plastic pollution and contribute to the restoration and preservation of aquatic ecosystems."]
        self.harvester_buttons = []
        for i in range(0, 6):
            self.harvester_buttons.append(self.Harvester_button(self.beach_map, 0.1*WINDOW_WIDTH, (0.16*(i+1)-0.14)*WINDOW_HEIGHT,
                self.beach_map.harvesters[i], self.harvester_info[i]))
        
        self.buttons = [Button(0.83*WINDOW_WIDTH, 0.93*WINDOW_HEIGHT, BUTTON_WIDTH,
                               BUTTON_HEIGHT, WHITE, "Back", self.open_beach_map)]
        
    def load_text_from_file(self, file_path):
            with open(file_path, 'r') as file:
                text = file.read()
            return text
    
    class Harvester_button:
        def __init__(self, beach_map, x, y, harvester, info):
            self.beach_map = beach_map
            self.rect = pygame.Rect(x, y, 0.4*WINDOW_WIDTH, 0.1*WINDOW_HEIGHT)
            self.harvester = harvester
            self.info = info
            
            self.enough_money = True
            self.enough_money_timer = None  # Timer to track the display duration
            
            self.buy_button = Button(x, y + 0.1*WINDOW_HEIGHT, 0.075*WINDOW_WIDTH, 
                                     0.056*WINDOW_HEIGHT, (255, 0, 0), "Buy", self.update_harvesters)
            self.info_button = Button(x + 0.075*WINDOW_WIDTH, y + 0.1*WINDOW_HEIGHT, 0.075*WINDOW_WIDTH, 
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
                
            if not self.enough_money:
                done_text = "Not enough money!"
                done_font = pygame.font.Font(None, 30)
                done_text_surface = done_font.render(done_text, True, (255, 0, 0))
                done_text_rect = done_text_surface.get_rect(
                    center=(0.84*WINDOW_WIDTH, WINDOW_HEIGHT * 0.14))
                surface.blit(done_text_surface, done_text_rect)
                
                # Check if the timer has been set or expired
                if self.enough_money_timer is None:
                    self.enough_money_timer = pygame.time.get_ticks()
                else:
                    current_time = pygame.time.get_ticks()
                    elapsed_time = current_time - self.enough_money_timer
                    if elapsed_time > 800:  # Display for 0.8 seconds
                        self.enough_money = True
                        self.enough_money_timer = None
                
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
                self.enough_money = False
    
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
              
    def resize_image(self, image, size):
        aspect_ratio = image.get_width() / image.get_height()
        new_width, new_height = size
        # new_height = int(new_width / aspect_ratio)
        # if new_height > size[1]:
        #     new_height = size[1]
        #     new_width = int(new_height * aspect_ratio)
        return pygame.transform.scale(image, (new_width, new_height))

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
        font = pygame.font.Font(None, 40)

        for button in self.buttons:
            button.draw(surface)
            
        for harvester_button in self.harvester_buttons:
            harvester_button.draw(surface)
            
        font = pygame.font.Font(None, 36)
        formatted_bank = "${:.2f}".format(self.beach_map.bank)  # Format the bank amount with two decimal places
        bank_text_surface = font.render(formatted_bank, True, (0,100,0))
        bank_text_rect = bank_text_surface.get_rect(topright=(WINDOW_WIDTH - 20, 20))
        surface.blit(bank_text_surface, bank_text_rect)

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
        self.background_image = pygame.image.load("beach_background.png")
        self.background_image = self.resize_image(
            self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.buttons = [Button(0.84*WINDOW_WIDTH, 0.9*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                               "Back", self.open_beach_map),
                        Button(0.6*WINDOW_WIDTH, 0.6*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                               "Load Game"),
                        Button(0.7*WINDOW_WIDTH, 0.7*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                               "Save Game"),
                        Button(0.5*WINDOW_WIDTH, 0.5*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                               "Exit Game", self.exit_game)]
        
        #self.sliders = [Slider("Sound Control")] # to be made

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def resize_image(self, image, size):
        aspect_ratio = image.get_width() / image.get_height()
        new_width, new_height = size
        # new_height = int(new_width / aspect_ratio)
        # if new_height > size[1]:
        #     new_height = size[1]
        #     new_width = int(new_height * aspect_ratio)
        return pygame.transform.scale(image, (new_width, new_height))

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
            
        font = pygame.font.Font(None, 36)
        formatted_bank = "${:.2f}".format(self.beach_map.bank)  # Format the bank amount with two decimal places
        bank_text_surface = font.render(formatted_bank, True, (0, 100, 0))
        bank_text_rect = bank_text_surface.get_rect(topright=(WINDOW_WIDTH - 20, 20))
        surface.blit(bank_text_surface, bank_text_rect)
        
        date_text = self.beach_map.date.strftime("%B %Y")  # Format the date as "Month Year"
        date_text_surface = font.render(date_text, True, (10, 10, 150))
        date_text_rect = date_text_surface.get_rect(topleft=(10, 10))
        surface.blit(date_text_surface, date_text_rect)

    def open_beach_map(self):
        clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            self.beach_map.handle_events(events)

            self.beach_map.draw()

            pygame.display.flip()
            clock.tick(FPS)


class BeachMap:
    def __init__(self, screen):
        self.background_image = pygame.image.load("beach_background.png")
        self.background_image = self.resize_image(self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.harvesters = [
            Harvester(["seabin_big.png", "seabin_middle.png", "seabin_small.png",
                       "seabin_middle.png"], 1.17, 4100, (int(0.15*WINDOW_WIDTH), 
                    int(0.3*WINDOW_HEIGHT)), "Seabin", (int(0.11*WINDOW_WIDTH),int(0.11*WINDOW_WIDTH)), 0),
            Harvester(["WasteShark.png"], 150, 24600, (int(0.0125*WINDOW_WIDTH), 0), "WasteShark",
                      (int(0.11*WINDOW_WIDTH),int(0.225*WINDOW_WIDTH)), 2.5),
            Harvester(["trashwheel_1.png", "trashwheel_2.png", 
                          "trashwheel_3.png", "trashwheel_4.png"], 
                      6205, 800000, (int(0.27*WINDOW_WIDTH),0), "Trash Wheel", 
                      (int(0.15*WINDOW_WIDTH), int(0.3*WINDOW_WIDTH)), 1.5),
            Harvester(["HO_wrack_1.png", "HO_wrack_2.png",
                       "HO_wrack_3.png", "HO_wrack_2.png"], 
                      2, 10000, (int(0.81*WINDOW_WIDTH),int(0.375*WINDOW_HEIGHT)),
                      "HO Wrack", (int(0.19*WINDOW_WIDTH),int(0.28*WINDOW_WIDTH)), 2),
            Harvester(["litter_pickers_1.png", "litter_pickers_2.png",
                       "litter_pickers_3.png", "litter_pickers_2.png"], 
                      0.1, 1000, (int(0.71*WINDOW_WIDTH),int(0.028*WINDOW_HEIGHT)),
                      "Litter Picker", (int(0.125*WINDOW_WIDTH), int(0.15*WINDOW_WIDTH)), 1),
            Harvester(["litterboon_wide.png", "litterboon_middle.png",
                       "litterboon_narrow.png", "litterboon_middle.png"], 
                      18, 100000, (int(0.425*WINDOW_WIDTH),0), "LitterBoom",
                      (int(0.22*WINDOW_WIDTH), WINDOW_HEIGHT), 0)]

        self.buttons = [
            Button(0.0625*WINDOW_WIDTH, 0.1*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                   "Harvester Menu", self.open_harvester_menu),
            Button(0.0625*WINDOW_WIDTH,  0.21*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT,
                   WHITE, "Main Menu", self.open_main_menu),
            Button(0.0625*WINDOW_WIDTH,  0.32*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT,
                   WHITE, "Quiz", self.open_quiz),
            Button(0.85*WINDOW_WIDTH, 0.9*WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                   "Next", self.next_term)]
        
        self.screen = screen
        self.multiplier = 1.
        self.bank = 10000
        self.harvesters[4].amount += 1
        
        self.exchange_rate = 100 #1 ton of plastic is worth $100
        self.total_recovery_rate = self.calculate_total_recovery_rate()
        self.waste_rate = 8.e6 #tons of plastic released into ocean per year
        self.total_plastic = 1.5e8
        self.date = datetime.datetime(2023, 8, 1)
        
        self.quiz_completed = False
        self.display_quiz_completed = False
        self.display_quiz_completed_timer = None  # Timer to track the display duration
        self.display_quiz_unopened = False
        self.display_quiz_unopened_timer = None  # Timer to track the display duration

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
            self.date = self.date.replace(month=self.date.month + 1)
        else:
            self.display_quiz_unopened = True

    def resize_image(self, image, size):
        aspect_ratio = image.get_width() / image.get_height()
        new_width, new_height = size
        # new_height = int(new_width / aspect_ratio)
        # if new_height > size[1]:
        #     new_height = size[1]
        #     new_width = int(new_height * aspect_ratio)
        return pygame.transform.scale(image, (new_width, new_height))

    def open_harvester_menu(self):
        harvester_menu = HarvesterMenu(self)
        self.run_sub_menu(harvester_menu)

    def open_main_menu(self):
        main_menu = MainMenu(self)
        self.run_sub_menu(main_menu)

    def open_quiz(self):
        if not self.quiz_completed:
            quiz = Quiz(self)
            self.run_sub_menu(quiz)
        else:
            self.display_quiz_completed = True

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
                resized_image = self.resize_image(harvester.image, harvester.size)
                surface.blit(resized_image, harvester.rect)

        # Draw the buttons on top of the background and harvesters
        for button in self.buttons:
            button.draw(surface)
            
        for harvester in self.harvesters:
            harvester.animate()  # Call the animate method to update

        self.move_harvesters()
        
        font = pygame.font.Font(None, 36)
        formatted_bank = "${:.2f}".format(self.bank)  # Format the bank amount with two decimal places
        bank_text_surface = font.render(formatted_bank, True, (0, 100, 0))
        bank_text_rect = bank_text_surface.get_rect(topright=(WINDOW_WIDTH - 20, 20))
        surface.blit(bank_text_surface, bank_text_rect)
        
        date_text = self.date.strftime("%B %Y")  # Format the date as "Month Year"
        date_text_surface = font.render(date_text, True, (10, 10, 150))
        date_text_rect = date_text_surface.get_rect(topleft=(10, 10))
        surface.blit(date_text_surface, date_text_rect)
        
        if self.display_quiz_completed:
                done_text = ["Quiz already completed!", "Proceed to next term."]
                done_font = pygame.font.Font(None, 30)
                
                text_y = WINDOW_HEIGHT * 0.14
                
                for sentence in done_text:
                    done_text_surface = done_font.render(sentence, True, (255, 0, 0))
                    done_text_rect = done_text_surface.get_rect(center=(0.84*WINDOW_WIDTH, text_y))
                    surface.blit(done_text_surface, done_text_rect)
                    text_y += done_text_surface.get_height() + 5  # Adjust for spacing between lines
                
                # Check if the timer has been set or expired
                if self.display_quiz_completed_timer is None:
                    self.display_quiz_completed_timer = pygame.time.get_ticks()
                else:
                    current_time = pygame.time.get_ticks()
                    elapsed_time = current_time - self.display_quiz_completed_timer
                    if elapsed_time > 1500:  # Display for 1.5 seconds
                        self.display_quiz_completed = False
                        self.display_quiz_completed_timer = None
                        
        if self.display_quiz_unopened:
                done_text = "Complete quiz before the next term!"
                done_font = pygame.font.Font(None, 30)
                done_text_surface = done_font.render(done_text, True, (255, 0, 0))
                done_text_rect = done_text_surface.get_rect(
                    center=(0.74*WINDOW_WIDTH, WINDOW_HEIGHT * 0.14))
                surface.blit(done_text_surface, done_text_rect)
                
                # Check if the timer has been set or expired
                if self.display_quiz_unopened_timer is None:
                    self.display_quiz_unopened_timer = pygame.time.get_ticks()
                else:
                    current_time = pygame.time.get_ticks()
                    elapsed_time = current_time - self.display_quiz_unopened_timer
                    if elapsed_time > 1500:  # Display for 1.5 seconds
                        self.display_quiz_unopened = False
                        self.display_quiz_unopened_timer = None


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