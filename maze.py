"""
You are given a 2D grid representing a maze. A 0 represents a path, and a 1
represents a wall. You start at the top left of the maze (0, 0) and want to
reach the bottom right of the maze (M - 1, N - 1). You can only move in the
right or down direction. Return the list of coordinates that correspond a valid
solution (traveling along the path). If there are no valid paths, return the
empty list.

Example:
[[0, 1, 0, 1],
 [0, 0, 0, 1],
 [1, 0, 1, 0],
 [0, 0, 0, 0]] -> [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]
"""

def solve_maze(maze):
    return solve_maze_helper(maze, [(0, 0)])

def solve_maze_helper(maze, path):
    x, y = path[len(path) - 1]
    if (x == len(maze) - 1 and y == len(maze[0]) - 1):
        return path
    if (x >= len(maze) or y >= len(maze[0])):
        return []
    if maze[x][y] == 1:
        return []
    move_right = solve_maze_helper(maze, path + [(x + 1, y)])
    if move_right != []:
        return move_right
    move_down = solve_maze_helper(maze, path + [(x, y + 1)])
    if move_down != []:
        return move_down
    return []

maze = [[0, 1, 0, 1],
        [0, 0, 0, 1],
        [1, 0, 1, 0],
        [0, 0, 0, 0]]
maze2 = [[0, 1, 1],
         [0, 1, 1],
         [1, 1, 0]]
print(solve_maze(maze))
print(solve_maze(maze2))
