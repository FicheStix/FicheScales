# Walk-the-dog interview response.

import os
import time
GRIDROWS=40
GRIDCOLS=40

def create_grid(row_num,col_num):
    grid = [['' for _ in range(row_num)] for _ in range(col_num)]
    return grid
 
def setup_grid(grid):
    # populate the grid with starting positions
    pattern1 = [(4,4), (4,5), (4,6), (3,6), (2,5)]
    pattern2 = [(10,10), (10,11), (10,12), (11,11), (12,12), (12,14), (13,13)]
    for coord in pattern2:
        change_cell_state('X', grid, coord[0], coord[1])
 
def print_grid(grid):
    os.system('cls')

    for row in range(GRIDROWS-1):
        for col in range(GRIDCOLS-1):
            cell_value = grid[row][col]
            if cell_value == '':
                print('-',end='')
            else:
                print('X',end='')
        print('')
 
def change_cell_state(new_state, grid, row, col):
        grid[row][col] = new_state

 
def is_alive(grid, row, col):
    if grid[row][col] == 'X':
        return True
    else:
        return False
 
def get_live_neighbors(grid, row, col):
    neighbors = []
    live_neighbors = 0
 
    if (row-1 <= 19 and row-1 >= 0) and (col-1 <= 19 and col-1 >= 0):
        neighbors.append(grid[row-1][col-1])    # up-left

    if (row-1 <= 19 and row-1 >= 0) and (col <= 19 and col >= 0):
        neighbors.append(grid[row-1][col])        # up

    if (row-1 <= 19 and row-1 >= 0) and (col+1 <= 19 and col+1 >= 0):    
        neighbors.append(grid[row-1][col+1])     # up-right

    if (row <= 19 and row >= 0) and (col+1 <= 19 and col+1 >= 0):        
        neighbors.append(grid[row][col+1])       # right

    if (row+1 <= 19 and row+1 >= 0) and (col+1 <= 19 and col+1 >= 0):    
        neighbors.append(grid[row+1][col+1])     # down-right

    if (row+1 <= 19 and row+1 >= 0) and (col <= 19 and col >= 0):    
        neighbors.append(grid[row+1][col])       # down
        
    if (row+1 <= 19 and row+1 >= 0) and (col-1 <= 19 and col-1 >= 0):    
        neighbors.append(grid[row+1][col-1])     # down-left

    if (row <= 19 and row >= 0) and (col-1 <= 19 and col-1 >= 0):     
        neighbors.append(grid[row][col-1])       # left
   
    for value in neighbors:
        if value == 'X':
            live_neighbors += 1
 
    return live_neighbors
 
def run_rules(grid, row, col, updates):

    live_cell = is_alive(grid, row, col)
    live_neighbors = get_live_neighbors(grid, row, col)
   
    if live_cell and (live_neighbors == 2 or live_neighbors == 3):
        pass
    elif live_cell and live_neighbors < 2:
        updates.append({'state':'', 'row':row, 'col':col})
    elif live_cell and live_neighbors > 3:
        updates.append({'state':'', 'row':row, 'col':col})
    elif not live_cell and live_neighbors == 3:
        updates.append({'state':'X', 'row':row, 'col':col})
 
def run_game(grid):
    setup_grid(grid)

    # print new game grid
    print_grid(grid)
    time.sleep(.5)

    # lets begin evaluation
    game_round = 0
    while game_round < 100:
        # run rules for each cell in the grid and track cells that need to be updated
        grid_updates = []
        for row in range(20):
            for col in range(20):
                run_rules(grid, row, col, grid_updates)
       
        # apply identified changes to cells after full grid evaluation
        for change in grid_updates:
                    change_cell_state(change['state'], grid, change['row'], change['col'] )

        print_grid(grid)
        time.sleep(.1)
        game_round += 1

    print('This was fun. End of Line')
 
if __name__ == '__main__':
    run_game(create_grid(GRIDROWS, GRIDCOLS))
