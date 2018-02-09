"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero),
return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until
it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
"""

def best_bomb(grid):
    max_enemies_killed = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            tmp = bomb(grid, x, y)
            if tmp > max_enemies_killed:
                max_enemies_killed = tmp
    return max_enemies_killed

def bomb(grid, x, y):
    if grid[x][y] != '0':
        return 0
    enemies_killed = 0
    i = x
    while 0 <= i:
        if grid[i][y] == 'E':
            enemies_killed += 1
        elif grid[i][y] == 'W':
            break
        i -= 1
    i = x
    while i < len(grid):
        if grid[i][y] == 'E':
            enemies_killed += 1
        elif grid[i][y] == 'W':
            break
        i += 1
    j = y
    while 0 <= j:
        if grid[x][j] == 'E':
            enemies_killed += 1
        elif grid[x][j] == 'W':
            break
        j -= 1
    j = y
    while j < len(grid[0]):
        if grid[x][j] == 'E':
            enemies_killed += 1
        elif grid[x][j] == 'W':
            break
        j += 1
    return enemies_killed

# runtime: O((m * n)(m + n))

grid = [['0', 'E', '0', '0'],
        ['E', '0', 'W', 'E'],
        ['0', 'E', '0', '0']]

grid2 = [['0', '0', '0'],
         ['W', 'W', 'E'],
         ['W', 'E', '0']]

print(best_bomb(grid) == 3)
print(best_bomb(grid2) == 2)
