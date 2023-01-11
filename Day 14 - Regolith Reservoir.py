# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 17:35:46 2022

@author: tn16322
"""
import numpy as np

x_max = 500
x_min = 500
y_max = 0

paths = []

with open('Day 14 - Input.txt', 'r') as f:
    
    for line in f:
        p = []
        path = line.strip().split(' -> ')
            
        for point in path:
            x, y = map(int,point.split(','))
            p.append((x,y))
            if x > x_max:
                x_max = x
            elif x < x_min:
                x_min = x
                
            if y > y_max:
                y_max = y
                
        paths.append(p)

x_max = max(500+y_max,x_max)+2
x_min = min(500-y_max,x_min)-2
y_max += 1

slice_map = np.array([['.']*(x_max-x_min+1)]*(y_max+1))
slice_map = np.append(slice_map,[['#']*(x_max-x_min+1)], axis=0)
slice_map[0,500-x_min] = '+'

for path in paths:
    for i in range(1,len(path)):
        horizontal_run = abs(path[i-1][0]-path[i][0]) + 1
        vertical_run = abs(path[i-1][1]-path[i][1]) + 1
        lower_x = min(path[i-1][0],path[i][0]) - x_min
        lower_y = min(path[i-1][1],path[i][1])
        slice_map[lower_y:lower_y+vertical_run, lower_x:lower_x+horizontal_run] = [['#']*horizontal_run]*vertical_run
  
unit_placed = True
units_placed = 0
while unit_placed == True:
    unit_pos_x = (500-x_min)
    unit_pos_y = 0
    while True:
        if slice_map[unit_pos_y+1, unit_pos_x] == '.':
            unit_pos_y += 1
        elif slice_map[unit_pos_y+1, unit_pos_x-1] == '.':
            unit_pos_x -= 1
        elif slice_map[unit_pos_y+1, unit_pos_x+1] == '.':
            unit_pos_x += 1
        else:
            slice_map[unit_pos_y, unit_pos_x] = 'o'
            units_placed += 1
            print('unit placed at (' + str(unit_pos_x) + ',' + str(unit_pos_y) + ')')
            if unit_pos_y == 0:
                unit_placed = False
            break

print('num units placed = ' + str(units_placed))