# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:54:19 2022

@author: tn16322
"""
max_calorie_elves = [(0,0)]*3

with open('Day 1 - Calorie Counting Input.txt', 'r') as f:
    current_elf = 1
    current_sum = 0
    
    for line in f.readlines():
        line = line.strip()
        if (line == ""):
            if (current_sum > max_calorie_elves[2][0]):
                max_calorie_elves.append((current_elf,current_sum))
                max_calorie_elves = sorted(max_calorie_elves,key = lambda x: x[1],reverse=True)[:3]
            current_sum = 0
            current_elf += 1
        else:
            current_sum += int(line)
    #check that last elve isn't the one with the most
    if (current_sum > max_calorie_elves[2][0]):
        max_calorie_elves.append((current_elf,current_sum))
        max_calorie_elves = sorted(max_calorie_elves,key = lambda x: x[1],reverse=True)[:3]

top3_sum = sum(i for _,i in max_calorie_elves)
list_top3 = [i for i,_ in max_calorie_elves]

print("elves with most are elves #" + str(list_top3))
print("sum of top 3 calories = " + str(top3_sum))