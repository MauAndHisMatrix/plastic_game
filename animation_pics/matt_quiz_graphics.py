import pygame
import sys
import json

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50
BUTTON_SPACING = 20
WHITE = (255, 255, 255)
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

# open a file for writing
with open('data.json', 'w') as f:
    # write the dictionary to the file in JSON format
    json.dump(data, f)


class Quiz:
    def __init__(self):
        self.background_image = pygame.image.load("beach_background.png")
        self.background_image = self.resize_image(
            self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def get_question_tuple(self):
        data = dict()
        with open('data.json', 'r') as file:
            data = json.load(file)
        print(data)
        return data

    def write_question_tuple(self, data):
        with open('data.json', 'w') as f:
            # write the dictionary to the file in JSON format
            json.dump(data, f)

    def create_buttons(self, current_question_number):
        self.question_buttons = [
            Button(50, 300, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                   "A", lambda: self.check_answer(1, current_question_number)),
            Button(200, 300, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                   "B", lambda: self.check_answer(2, current_question_number)),
            Button(350, 300, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                   "C", lambda: self.check_answer(3, current_question_number)),
            Button(500, 300, BUTTON_WIDTH, BUTTON_HEIGHT,
                   WHITE, "D", lambda: self.check_answer(4, current_question_number)),
            Button(300, 400, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                   "Quit", self.open_beach_map)
        ]
        return self.question_buttons

    def check_answer(self, answer, current_question_number):
        mark = questions_dict[current_question_number][-1] == answer
        print(mark)
        data = self.get_question_tuple()

        data["current_question_number"] += 1

        if mark:
            data["Correct Answers"] += 1
        elif not mark:
            data["Incorrect Answers"] += 1

        self.write_question_tuple(data)

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

            for button in self.buttons:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        if button.is_clicked(pos):
                            print("performing action line 385")
                            button.perform_action()

    def draw(self, surface):
        surface.fill((0, 0, 0))

        surface.blit(self.background_image, (0, 0))
        font = pygame.font.Font(None, 40)

        data = self.get_question_tuple()
        current_question_number, correct_answers, incorrect_answers = data[
            "current_question_number"], data["Correct Answers"], data["Incorrect Answers"]

        quiz_text = questions_dict[current_question_number][0]
        quiz_font = pygame.font.Font(None, 30)
        max_text_width = WINDOW_WIDTH - 100  # Allow 100 pixels margin on each side
        quiz_lines = []
        words = quiz_text.split()

        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            test_line_surface = quiz_font.render(test_line, True, WHITE)

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
            quiz_text_surface = quiz_font.render(line, True, WHITE)
            quiz_text_rect = quiz_text_surface.get_rect(
                center=(WINDOW_WIDTH // 2, y_offset))
            surface.blit(quiz_text_surface, quiz_text_rect)
            y_offset += 30  # Adjust the spacing between lines

        # Display the answers under each other
        question_answers = [questions_dict[current_question_number][1],
                            questions_dict[current_question_number][2],
                            questions_dict[current_question_number][3],
                            questions_dict[current_question_number][4]]

        question_font = pygame.font.Font(None, 30)
        y_offset += 30  # Add some spacing between the quiz text and answers

        for answer in question_answers:
            answer_text_surface = question_font.render(answer, True, WHITE)
            answer_text_rect = answer_text_surface.get_rect(
                center=(WINDOW_WIDTH // 2, y_offset))
            surface.blit(answer_text_surface, answer_text_rect)
            y_offset += 30  # Adjust the spacing between lines

        answers_text = f"Correct Answers: {correct_answers}    Incorrect Answers: {incorrect_answers}"
        answers_font = pygame.font.Font(None, 30)
        answers_text_surface = answers_font.render(answers_text, True, WHITE)
        answers_text_rect = answers_text_surface.get_rect(
            center=(250, WINDOW_HEIGHT * 9//10))
        surface.blit(answers_text_surface, answers_text_rect)

        self.buttons = self.create_buttons(current_question_number)

        for button in self.buttons:
            button.draw(surface)

    def open_beach_map(self):
        main()


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
    def __init__(self, image_path, x, y):
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.original_image, (self.original_image.get_width(
        ) // 4, self.original_image.get_height() // 4))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class HarvesterMenu:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        self.value3 = 0

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self, surface):
        surface.fill(BLACK)
        font = pygame.font.Font(None, 40)
        value_text = f"Value 1: {self.value1}, Value 2: {self.value2}, Value 3: {self.value3}"
        text_surface = font.render(value_text, True, WHITE)
        text_rect = text_surface.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        surface.blit(text_surface, text_rect)


class MainMenu:
    def __init__(self):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self, surface):
        surface.fill(BLACK)
        font = pygame.font.Font(None, 40)
        text_surface = font.render("Main Menu", True, WHITE)
        text_rect = text_surface.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        surface.blit(text_surface, text_rect)


class BeachMap:
    def __init__(self, screen):
        self.background_image = pygame.image.load("beach_background.png")
        self.background_image = self.resize_image(
            self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.harvesters = [
            Harvester("litterboon_narrow.png", 100, 200),
            Harvester("litterboon_wide.png", 300, 400)
        ]

        self.buttons = [
            Button(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT, WHITE,
                   "Harvester Menu", self.open_harvester_menu),
            Button(50, 110, BUTTON_WIDTH, BUTTON_HEIGHT,
                   WHITE, "Main Menu", self.open_main_menu),
            Button(50, 170, BUTTON_WIDTH, BUTTON_HEIGHT,
                   WHITE, "Quiz", self.open_quiz)
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

    def open_harvester_menu(self):
        harvester_menu = HarvesterMenu()
        self.run_sub_menu(harvester_menu)

    def open_main_menu(self):
        main_menu = MainMenu()
        self.run_sub_menu(main_menu)

    def open_quiz(self):
        quiz = Quiz()
        self.run_sub_menu(quiz)

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
                            print("performing action line 557")
                            button.perform_action()

    def draw(self):
        surface = self.screen
        # Draw the background image
        surface.blit(self.background_image, (0, 0))

        # Draw the harvesters on top of the background
        for harvester in self.harvesters:
            surface.blit(harvester.image, harvester.rect)

        # Draw the buttons on top of the background and harvesters
        for button in self.buttons:
            button.draw(surface)


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
