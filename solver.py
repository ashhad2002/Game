import pygame

def get_empty(grid):
    for i in range(0,9):
        for j in range(0,9):
            if(grid[i][j] == 0):
                return i,j
    return None, None

def possible(grid,row,col,n):
    for i in range(0,9):
        if (grid[i][col] == n):
            return False
        if grid[row][i] == n:
            return False
    r = row // 3
    c = col // 3
    for i in range(r*3, (r*3)+3):
        for j in range(c*3, (c*3)+3):
            if grid[i][j] == n:
                return False
    return True

def solve(grid):
    i, j = get_empty(grid)
    if i is None:
        return True
    for n in range(1,10):
        if possible(grid,i,j,n):
            grid[i][j] = n
            if solve(grid):
                return True
        grid[i][j] = 0
    return False

#-----------------------------#    
#****** leave commented ******#
#-----------------------------#    

# grid = [[1,1,1,1,1,1,1,1,1],
#         [2,5,3,5,4,3,2,9,6],
#         [4,3,1,4,1,2,2,1,7],
#         [6,2,4,3,2,1,8,2,3],
#         [1,2,1,2,4,5,8,3,2],
#         [6,3,6,1,7,6,6,5,4],
#         [5,4,5,4,1,9,5,3,3],
#         [7,5,4,4,8,9,8,3,2],
#         [1,2,7,3,2,6,3,2,1]]

# grid = [[0,3,0,4,0,0,0,6,0],
#         [0,0,0,9,1,0,0,0,0],
#         [2,0,5,0,8,0,0,9,7],
#         [0,9,7,0,3,2,0,0,5],
#         [5,0,3,0,0,4,0,0,0],
#         [1,0,0,5,9,8,7,3,0],
#         [0,6,0,3,0,0,0,0,0],
#         [0,0,4,0,7,1,0,0,0],
#         [0,0,0,0,0,0,4,0,0]]

# if not solve(grid):
#     print("solution not found")

# for n in range(0,9):
#     print(grid[n])