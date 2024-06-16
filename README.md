# MazeSolver

This is a simple maze generator and solver built with Python and Tkinter.
The maze defaults to a 20X20 grid. the entrance is always the top left cell,
and the exit is always the bottom right cell.

It implements an algorithm between depth-first search and greedy best-first search.
Simply-put, the algorithm always checks if it can move right or down first (toward the exit)
before it checks if it can move left or up. This reduces some of the over-head of a traditional
DFS on most attempts.