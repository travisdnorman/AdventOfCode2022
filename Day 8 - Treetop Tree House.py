# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:06:50 2022

@author: tn16322

--- Day 8: Treetop Tree House ---
The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390
Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
The top-middle 5 is visible from the top and right.
The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
The left-middle 5 is visible, but only from the right.
The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
The right-middle 3 is visible from the right.
In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?

Your puzzle answer was 1843.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle 5 in the second row:

30373
25512
65332
33549
35390
Looking up, its view is not blocked; it can see 1 tree (of height 3).
Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
Looking right, its view is not blocked; it can see 2 trees.
Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).
A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

30373
25512
65332
33549
35390
Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
Looking left, its view is not blocked; it can see 2 trees.
Looking down, its view is also not blocked; it can see 1 tree.
Looking right, its view is blocked at 2 trees (by a massive tree of height 9).
This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

Consider each tree on your map. What is the highest scenic score possible for any tree?
"""
import numpy as np

with open('Day 8 - Input.txt', 'r') as f:
    grid = []
    
    for line in f:
        grid.append([*map(int,line.strip())])

grid = np.array(grid)
seen_trees = np.zeros(grid.shape) 

grid_width = grid.shape[1]
grid_height = grid.shape[0]

#view from left
for i,row in enumerate(grid):
    max_height = -1
    for j,h in enumerate(row):
        if h > max_height:
            seen_trees[i,j] = 1
            max_height = h

#view from right
for i,row in enumerate(grid):
    max_height = -1
    for j in reversed(range(len(row))):
        if row[j] > max_height:
            seen_trees[i,j] = 1
            max_height = row[j]
            
#view from top
for j in range(len(grid[0])):
    max_height = -1
    for i in range(len(grid)):
        if grid[i,j] > max_height:
            seen_trees[i,j] = 1
            max_height = grid[i,j]
            
#view from bottom
for j in range(len(grid[0])):
    max_height = -1
    for i in reversed(range(len(grid))):
        if grid[i,j] > max_height:
            seen_trees[i,j] = 1
            max_height = grid[i,j]

max_scenic_score = 0

for i in range(1, grid_height-1):
    for j in range(1, grid_width-1):
        h = grid[i,j]
        
        sight_distance = 1
        #view to the left
        while (j-sight_distance) > 0 and h > grid[i,j-sight_distance]:
            sight_distance += 1
        view_to_left = sight_distance
        
        sight_distance = 1
        #view to the right
        while (j+sight_distance) < (grid_width-1) and h > grid[i,j+sight_distance]:
            sight_distance += 1
        view_to_right = sight_distance
        
        sight_distance = 1
        #view up
        while (i-sight_distance) > 0 and h > grid[i-sight_distance,j]:
            sight_distance += 1
        view_up = sight_distance
            
        sight_distance = 1
        #view down
        while (i+sight_distance) < (grid_height-1) and h > grid[i+sight_distance,j]:
            sight_distance += 1
        view_down = sight_distance
        
        scenic_score = view_down*view_up*view_to_left*view_to_right
        
        max_scenic_score = scenic_score if scenic_score > max_scenic_score else max_scenic_score

num_seen_trees = np.count_nonzero(seen_trees)        
print("num seen trees = " + str(num_seen_trees))
print("max scenic score = " + str(max_scenic_score))