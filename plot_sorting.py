'''
Python program to visualise various sorting algorithms including
'''

import pygame
import random
from bubble_sort_lists import bubble_sort
from insertion_sort_lists import insertion_sort
from selection_sort_lists import selection_sort
from merge_sort_lists import merge_sort

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

# Number of rectangles to visualize
NUMBER_OF_RECTANGLES = 200

# Gap width between rectangles
GAP_WIDTH = 0

# Delay between visualization frames (in milliseconds)
DELAY = 50

# Calculate the width of each rectangle based on screen width, gap width, and number of rectangles
RECTANGLE_WIDTH = (SCREEN_WIDTH - GAP_WIDTH * (NUMBER_OF_RECTANGLES + 1)) / NUMBER_OF_RECTANGLES

#Relative height of the rectangles
RECTANGLE_HEIGHT = 65

def generate_list(size=100):
    '''Generate a list of random numbers'''
    arr = [i for i in range(1, size + 1)] # Create a list of numbers from 1 to size
    random.shuffle(arr) # Shuffle the list to make it random
    return arr

class Rectangle:
    '''Rectangle used to visualise a bar of sort'''
    def __init__(self, x, height, surface, colour):
        '''Initialise the rectangle'''
        self.x = x
        self.height = height
        self.surface = surface
        self.colour = colour

    def draw(self):
        '''Draws rectangle'''
        pygame.draw.rect(self.surface, self.colour, pygame.Rect(self.x, SCREEN_HEIGHT -  self.height, RECTANGLE_WIDTH, self.height))
    
def display_pygame(list_of_lists):
    '''Displays the sorting process'''
    pygame.init()   # Initialize Pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create a Pygame window
    quit_flag = False
    
    # Iterate over each list of heights
    for arr in list_of_lists:

        pygame.time.delay(DELAY) # Pause to delay visualization
        screen.fill((0,0,0)) # Clear the screen
        list_of_rects = [Rectangle(GAP_WIDTH * (i + 1) + i * RECTANGLE_WIDTH, RECTANGLE_HEIGHT * height / (NUMBER_OF_RECTANGLES / 10), screen, (255,255,255)) for i, height in enumerate(arr)] # Create a list of Rectangle objects based on the heights
        # Draw each rectangle
        for rect in list_of_rects:
            rect.draw()

        pygame.display.update() #Update the display

        # Check for quit event
        for event in pygame.event.get():      
            if event.type == pygame.QUIT: 
                quit_flag = True

        # If quit event detected, exit the loop
        if quit_flag:
            break
    
     # Keep the window open until the user closes it
    while not quit_flag:
        for event in pygame.event.get():      
            if event.type == pygame.QUIT: 
                quit_flag = True

def main():
    '''Main programm'''
    random_list = generate_list(NUMBER_OF_RECTANGLES) # Generate a random list of numbers to be sorted
    list_of_lists = merge_sort(random_list) # Sort the list using chosen sorting algorithm
    display_pygame(list_of_lists) # Display the sorting process

if __name__ == '__main__':
    main()