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

# time complexity: O((m * n)(m + n))
# space complexity: O(1)
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

# time complexity: O(m * n)
# space complexity: O(m * n)
def best_bomb_optimized(grid):
    max_enemies_killed = 0
    row_kill_scores = get_row_kill_scores(grid)
    col_kill_scores = get_col_kill_scores(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            tmp = row_kill_scores[i][j] + col_kill_scores[i][j]
            if tmp > max_enemies_killed:
                max_enemies_killed = tmp
    return max_enemies_killed

def get_row_kill_scores(grid):
    kill_scores = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
    for i in range(len(grid)):
        start = 0
        enemies_killed = 0
        for j in range(len(grid[0])):
            if grid[i][j] == 'E':
                enemies_killed += 1
            elif grid[i][j] == 'W':
                for k in range(start, j):
                    if grid[i][k] == '0':
                        kill_scores[i][k] = enemies_killed
                start = j
                enemies_killed = 0
        for k in range(start, len(grid[0])):
            if grid[i][k] == '0':
                kill_scores[i][k] = enemies_killed
    return kill_scores

def get_col_kill_scores(grid):
    kill_scores = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
    for j in range(len(grid[0])):
        start = 0
        enemies_killed = 0
        for i in range(len(grid)):
            if grid[i][j] == 'E':
                enemies_killed += 1
            elif grid[i][j] == 'W':
                for k in range(start, i):
                    if grid[k][j] == '0':
                        kill_scores[k][j] = enemies_killed
                start = i
                enemies_killed = 0
        for k in range(start, len(grid)):
            if grid[k][j] == '0':
                kill_scores[k][j] = enemies_killed
    return kill_scores

grid = [['0', 'E', '0', '0'],
        ['E', '0', 'W', 'E'],
        ['0', 'E', '0', '0']]

grid2 = [['0', '0', '0'],
         ['W', 'W', 'E'],
         ['W', 'E', '0']]

print(best_bomb_optimized(grid) == 3)
print(best_bomb_optimized(grid2) == 2)
