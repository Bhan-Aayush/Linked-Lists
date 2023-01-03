import random  
from typing import Tuple  
  
import pygame  
from pygame.colordict import THECOLORS  
  
from linked_list import LinkedList, _Node  
  
 
# Graphics constants  
SCREEN_SIZE = (800, 800)  # (width, height)  
GRID_SIZE = 8  
NODE_COLOR = (0, 0, 255)  
NODE_WIDTH = 100  
NODE_HEIGHT = 100  
  
  
  
# Pygame helper functions 

def initialize_screen(screen_size: tuple[int, int], allowed: list) -> pygame.Surface:  
    """Initialize pygame and the display window. """
    
    pygame.display.init()  
    pygame.font.init()  
    screen = pygame.display.set_mode(screen_size)  
    screen.fill(THECOLORS['white'])  
    pygame.display.flip()  
  
    pygame.event.clear()  
    pygame.event.set_blocked(None)  
    pygame.event.set_allowed([pygame.QUIT] + allowed)  
  
    return screen  
  
  
def draw_text(screen: pygame.Surface, text: str, pos: tuple[int, int]) -> None:  
    """Draw the given text to the pygame screen at the given position. 
 
    pos represents the *upper-left corner* of the text. 
    """  
    font = pygame.font.SysFont('inconsolata', 22)  
    text_surface = font.render(text, True, THECOLORS['black'])  
    width, height = text_surface.get_size()  
    screen.blit(text_surface,  
                pygame.Rect(pos, (pos[0] + width, pos[1] + height)))  
  
  
def draw_grid(screen: pygame.Surface) -> None:  
    """Draws a square grid on the given surface."""
    
    color = THECOLORS['grey']  
    width, height = screen.get_size()  
  
    for col in range(1, GRID_SIZE):  
        x = col * (width // GRID_SIZE)  
        pygame.draw.line(screen, color, (x, 0), (x, height))  
  
    for row in range(1, GRID_SIZE):  
        y = row * (height // GRID_SIZE)  
        pygame.draw.line(screen, color, (0, y), (width, y))  
  
    
# 1. Drawing nodes and links  

def draw_node(screen: pygame.Surface, node: _Node, pos: Tuple[int, int]) -> None:  
    """Draw a node on the screen at the given position."""
    
    pygame.draw.rect(screen, NODE_COLOR, (pos[0], pos[1], NODE_WIDTH, NODE_HEIGHT), 1)  
    pygame.draw.rect(screen, NODE_COLOR, (pos[0] + NODE_WIDTH, pos[1], 100, 100), 1)  
    draw_text(screen, str(node.item), (pos[0] + int(NODE_WIDTH / 2) - 5,  
                                       pos[1] + int(NODE_WIDTH / 2) - 5))  
  
  
def draw_link(screen: pygame.Surface, start: Tuple[int, int], end: Tuple[int, int]) -> None:  
    """Draw a line representing a link from `start` to `end`."""
    
    pygame.draw.circle(screen, NODE_COLOR, (start[0], start[1]), NODE_WIDTH / 10)  
    pygame.draw.line(screen, NODE_COLOR, start, end, 1)  
  
  
def draw_three_nodes(screen_size: Tuple[int, int]) -> None:  
    """Draw three nodes on a pygame screen of the given size."""
    
    screen = initialize_screen(screen_size, [])  
    node1 = _Node(1)  
    node2 = _Node(2)  
    node3 = _Node(3)  
    node1.next = node2  
    node2.next = node3  
  
    draw_node(screen, node1, (10, 100))  
    draw_link(screen, (160, 150), (260, 150))  
    draw_node(screen, node2, (260, 100))  
    draw_link(screen, (410, 150), (510, 150))  
    draw_node(screen, node3, (510, 100))  
    draw_link(screen, (660, 150), (760, 150))  
    draw_text(screen, 'None', (760, 145))  
    ...  
  
    pygame.display.flip()  
    pygame.event.wait()  
    pygame.display.quit()  
  
  
  
# 2. Drawing a full linked list  
  
def draw_list(screen: pygame.Surface, lst: LinkedList, show_grid: bool = False) -> None:  
    """Draw the given linked list on the screen. """
    
    x = 100  
    y = 100  
    if show_grid:  
        draw_grid(screen)  
  
    curr = lst._first  
    curr_index = 0  
  
    while curr is not None:  
        pygame.draw.rect(screen, NODE_COLOR, ((x * curr_index) % SCREEN_SIZE[0] + 10,  
                                              (y * int(curr_index / GRID_SIZE)) + 25,  
                                              NODE_WIDTH / 2 - 10, NODE_HEIGHT / 2), 1)  
        pygame.draw.rect(screen, NODE_COLOR, ((x * curr_index) % SCREEN_SIZE[0] + NODE_WIDTH / 2,  
                                              (y * int(curr_index / GRID_SIZE)) + 25,  
                                              NODE_WIDTH / 2 - 10, NODE_HEIGHT / 2), 1)  
  
        if (curr_index + 1) % GRID_SIZE == 0:  
            pygame.draw.line(screen, NODE_COLOR, (25, (y * int(curr_index / GRID_SIZE)) + 100),  
                             (SCREEN_SIZE[0] - 25, (y * int(curr_index / GRID_SIZE)) + 100), 1)  
            pygame.draw.line(screen, NODE_COLOR, (SCREEN_SIZE[1] - 25,  
                                                  (y * int(curr_index / GRID_SIZE)) + 50),  
                             (SCREEN_SIZE[1] - 25, (y * int(curr_index / GRID_SIZE)) + 100), 1)  
            pygame.draw.line(screen, NODE_COLOR, (25, (y * int(curr_index / GRID_SIZE)) + 100),  
                             (25, (y * int(curr_index / GRID_SIZE)) + 125), 1)  
        else:  
            pygame.draw.line(screen, NODE_COLOR, ((x * curr_index) % SCREEN_SIZE[0] + 75,  
                                                  (y * int(curr_index / GRID_SIZE)) + 50),  
                             ((x * curr_index) % SCREEN_SIZE[0] + 110,  
                              (y * int(curr_index / GRID_SIZE)) + 50), 1)  
  
        pygame.draw.circle(screen, NODE_COLOR, (((x * curr_index) % SCREEN_SIZE[0] + 75,  
                                                 (y * int(curr_index / GRID_SIZE)) + 50)),  
                           NODE_WIDTH / 20)  
        draw_text(screen, str(curr.item), (((x * curr_index) % SCREEN_SIZE[0]) + 15,  
                                           (y * int(curr_index / GRID_SIZE)) + 45))  
  
        curr = curr.next  
        curr_index = curr_index + 1  
  
    if curr is None:  
        draw_text(screen, "None", (((x * curr_index) % SCREEN_SIZE[0]) + 15,  
                                   (y * int(curr_index / GRID_SIZE)) + 45))  
  
  
def draw_fifty_nodes(screen_size: Tuple[int, int]) -> None:  
    """Draws 50 nodes from a LinkedList. 
    """  
    screen = initialize_screen(screen_size, [])  
    linky = LinkedList([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90,  
                        95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165,  
                        170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240,  
                        245, 250])  
  
    draw_list(screen, linky, False)  
    ...  
  
    # Don't change the code below (it simply waits until you close the Pygame window)  
    pygame.display.flip()  
    pygame.event.wait()  
    pygame.display.quit()  
  
  
  
# 3. Handling user events  

def run_visualization(screen_size: tuple[int, int], ll_class: type,  
                      show_grid: bool = False) -> None:  
    """Run the linked list visualization.  """  

    # Initialize the Pygame screen, allowing for mouse click events.  
    screen = initialize_screen(screen_size, [pygame.MOUSEBUTTONDOWN])  
  
    # Initialize a random linked list of length 50.  
    lst = ll_class(random.sample(range(-99, 1000), 50))  
  
    while True:  
        # Draw the list (on a white background)  
        screen.fill(THECOLORS['white'])  
        draw_list(screen, lst, show_grid)  
        pygame.display.flip()  
  
        # Wait for an event (either pygame.MOUSEBUTTONDOWN or pygame.QUIT)  
        event = pygame.event.wait()  
  
        if event.type == pygame.MOUSEBUTTONDOWN:  
            # Call our event handling method  
            handle_mouse_click(lst, event, screen.get_size())  
        elif event.type == pygame.QUIT:  
            break  
  
    pygame.display.quit()  
  
  
def handle_mouse_click(lst: LinkedList, event: pygame.event.Event,  
                       screen_size: Tuple[int, int]) -> None:  
    """Handle a mouse click event. """
    
    x, y = event.pos[0], event.pos[1]  
    index = int(y / (screen_size[1] / GRID_SIZE)) * GRID_SIZE + \  
        int(x / (screen_size[0] / GRID_SIZE))  
  
    if index >= len(lst):  
        return  
    elif event.button == 1:  
        lst.pop(index)  
    elif event.button == 3:  
        list_form = lst.to_list()  
        item = list_form[index]  
        lst.__contains__(item)  
