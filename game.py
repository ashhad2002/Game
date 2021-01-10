import pygame
import sys
import random
from pygame.math import Vector2
from solver import *
from pygame.math import Vector2


def location(pos): 
    global x 
    x = pos[0]//spacing 
    global y 
    y = pos[1]//spacing

def draw_grid():
    for i in range (9): 
        for j in range (9): 
            if grid[i][j] != 0:   
                text1 = big_text.render(str(grid[i][j]), 1, (0, 0, 0)) 
                screen.blit(text1, (j * spacing + 20,i * spacing + 15)) 

    for i in range(10): 
        if i % 3 == 0 : 
            thick = 3
        else: 
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * spacing), (screen_size, i * spacing), thick) 
        pygame.draw.line(screen, (0, 0, 0), (i * spacing, 0), (i * spacing, screen_size), thick)

def highlight(): 
    pygame.draw.line(screen, (0, 255, 255), (x * spacing-3, (y)*spacing), (x * spacing + spacing + 3, (y)*spacing), 3) 
    pygame.draw.line(screen, (0, 255, 255), ( (x)* spacing, y * spacing ), ((x) * spacing, y * spacing + spacing), 3)
    pygame.draw.line(screen, (0, 255, 255), (x * spacing-3, (y + 1)*spacing), (x * spacing + spacing + 3, (y + 1)*spacing), 3) 
    pygame.draw.line(screen, (0, 255, 255), ( (x + 1)* spacing, y * spacing ), ((x + 1) * spacing, y * spacing + spacing), 3)

def draw_num(n):
    number = big_text.render(str(n), 1, (0, 0, 0)) 
    screen.blit(number, (x * spacing + 20, y * spacing + 15)) 

pygame.init()
screen_size = 500
screen = pygame.display.set_mode((screen_size,screen_size))
clock = pygame.time.Clock()

pygame.display.set_caption("Sudoku!!!") 
img = pygame.image.load('icon.png') 
win = pygame.image.load('d.png').convert_alpha()
win = pygame.transform.scale(win,(200*2, 47*2))
pygame.display.set_icon(img) 

x = 0
y = 0
n = 0
spacing = screen_size / 9
big_text = pygame.font.SysFont("comicsans", 45) 


grid = [[0,3,0,4,0,0,0,6,0],
        [0,0,0,9,1,0,0,0,0],
        [2,0,5,0,8,0,0,9,7],
        [0,9,7,0,3,2,0,0,5],
        [5,0,3,0,0,4,0,0,0],
        [1,0,0,5,9,8,7,3,0],
        [0,6,0,3,0,0,0,0,0],
        [0,0,4,0,7,1,0,0,0],
        [0,0,0,0,0,0,4,0,0]]

# grid = [[8,2,7,1,5,4,3,9,6],
#         [9,6,5,3,2,7,1,4,8],
#         [3,4,1,6,8,8,7,5,2],
#         [5,9,3,4,6,8,2,7,1],
#         [4,7,2,5,1,3,6,8,9],
#         [6,1,8,9,7,2,4,3,5],
#         [7,8,6,2,3,5,9,1,4],
#         [1,5,4,7,9,6,8,2,3],
#         [2,3,9,8,4,1,5,6,7]]

og_grid = [g[:] for g in grid]
solved_grid = [q[:] for q in grid]
solve(solved_grid)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            pos = pygame.mouse.get_pos() 
            location(pos) 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                    print(grid[0])
            if event.key == pygame.K_DOWN:
                    print(og_grid[0])
            if event.key == pygame.K_1: 
                n = 1
            if event.key == pygame.K_2: 
                n = 2  
            if event.key == pygame.K_3: 
                n = 3
            if event.key == pygame.K_4: 
                n = 4
            if event.key == pygame.K_5: 
                n = 5
            if event.key == pygame.K_6: 
                n = 6 
            if event.key == pygame.K_7: 
                n = 7
            if event.key == pygame.K_8: 
                n = 8
            if event.key == pygame.K_9: 
                n = 9
            if event.key == pygame.K_j: 
                copygrid = [j[:] for j in grid]
            if event.key == pygame.K_r: 
                grid = [r[:] for r in og_grid]
            if event.key == pygame.K_k: 
                grid = [p[:] for p in copygrid]
            if event.key == pygame.K_s: 
                grid = og_grid
                pygame.time.delay(200)
                solve(grid)
    screen.fill((255,255,255))
    draw_grid()
    highlight()
    if n != 0:
        draw_num(n)
        grid[int(y)][int(x)] = n
        n = 0
    if grid == solved_grid:
        pygame.time.delay(2000)
        screen.blit(win, (50,200)) 
    pygame.display.update()
    clock.tick(10)
    
