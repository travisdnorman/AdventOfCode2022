# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 21:02:55 2022

@author: tn16322

--- Day 12: Hill Climbing Algorithm ---
You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?

Your puzzle answer was 484.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though; perhaps you can find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the square marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from any square at elevation a to the square marked E.

Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a). If you start at the bottom-left square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^
This path reaches the goal in only 29 steps, the fewest possible.

What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?
"""
import numpy as np

class grid_point:
    def __init__(self, height, pos):
        self.height = height
        self.prev_point_on_path = None
        self.distance_from_start = 0
        self.lat = pos[0]
        self.long = pos[1]
        
        self.prev_point_on_rev_path = None
        self.distance_from_finish = 0
        
    def __str__(self):
        if self.height < 10:
            return ('(('+str(self.lat)+','+str(self.long)+'), 0'+str(self.height)+')')
        else:
            return ('(('+str(self.lat)+','+str(self.long)+'), '+str(self.height)+')')
    
def print_map():
    for r in heightmap:
        print(','.join([str(p.height) for p in r]))
        
def test_point(dep,arr):
    if (dep.height-arr.height) >= -1:
        if arr == finish:
            arr.distance_from_start = dep.distance_from_start+1
            arr.prev_point_on_path = dep
            return -1
        if arr.prev_point_on_path == None:
            arr.distance_from_start = dep.distance_from_start+1
            arr.prev_point_on_path = dep
            
            return 1
        else:
            return 0
    else:
        return 0
    
def test_point_going_down(dep,arr):
    if (dep.height-arr.height) <= 1:
        if arr.height == 0:
            arr.distance_from_finish = dep.distance_from_finish+1
            arr.prev_point_on_rev_path = dep
            return -1
        if arr.prev_point_on_rev_path == None:
            arr.distance_from_finish = dep.distance_from_finish+1
            arr.prev_point_on_rev_path = dep
            
            return 1
        else:
            return 0
    else:
        return 0

with open('Day 12 - Input.txt', 'r') as f:
    m = np.array([[*r] for r in map(str.strip,f.readlines())])

grid_height = len(m)
grid_len = len(m[0])
heightmap = np.ndarray((grid_height,grid_len),dtype=grid_point)    
for i, r in enumerate(m):
    for j, h in enumerate(r):
        if h == 'S':
            heightmap[i,j] = grid_point(0,(i,j))
            start = heightmap[i,j]
        elif h == 'E':
            heightmap[i,j] = grid_point(25,(i,j))
            finish = heightmap[i,j]
        else:
            heightmap[i,j] = grid_point(ord(h) - ord('a'),(i,j))       

#part 1
heads = [start]
while len(heads) != 0:
    #print('heads = [' + ', '.join(map(str,heads)) + ']')
    new_heads = []
    for p in heads:
        if p.lat < grid_height-1:
            result = test_point(p,heightmap[p.lat+1,p.long])
            if result == -1:
                break;
            elif result == 1:
                new_heads.append(heightmap[p.lat+1,p.long])
        if p.lat > 0:
            result = test_point(p,heightmap[p.lat-1,p.long])
            if result == -1:
                break;
            elif result == 1:
                new_heads.append(heightmap[p.lat-1,p.long])  
            
        if p.long < grid_len-1:
            result = test_point(p,heightmap[p.lat,p.long+1])
            if result == -1:
                break;
            elif result == 1:
                new_heads.append(heightmap[p.lat,p.long+1])
        if p.long > 0:
            result = test_point(p,heightmap[p.lat,p.long-1])
            if result == -1:
                break;
            elif result == 1:
                new_heads.append(heightmap[p.lat,p.long-1])
                
    if result == -1:
        break
                
    heads = new_heads

#part 2
heads = [finish]
while True:
    for p in heads:
        if p.lat < grid_height-1:
            dest = heightmap[p.lat+1,p.long]
            result = test_point_going_down(p,dest)
            if result == -1:
                trail_start = dest
                break;
            elif result == 1:
                new_heads.append(heightmap[p.lat+1,p.long])
        if p.lat > 0:
            dest = heightmap[p.lat-1,p.long]
            result = test_point_going_down(p,dest)
            if result == -1:
                trail_start = dest
                break;
            elif result == 1:
                new_heads.append(heightmap[p.lat-1,p.long])  
            
        if p.long < grid_len-1:
            dest = heightmap[p.lat,p.long+1]
            result = test_point_going_down(p,dest)
            if result == -1:
                trail_start = dest
                break;
            elif result == 1:
                new_heads.append(heightmap[p.lat,p.long+1])
        if p.long > 0:
            dest = heightmap[p.lat,p.long-1]
            result = test_point_going_down(p,dest)
            if result == -1:
                trail_start = dest
                break;
            elif result == 1:
                new_heads.append(heightmap[p.lat,p.long-1])
                
    if result == -1:
        break
                
    heads = new_heads
        
print('Shortest Distance = ' + str(finish.distance_from_start))
print('Shortest Distance Trail Length = ' + str(trail_start.distance_from_finish))