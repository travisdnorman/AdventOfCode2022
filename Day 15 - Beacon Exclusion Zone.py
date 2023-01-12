# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 12:22:24 2022

@author: tn16322

--- Day 15: Beacon Exclusion Zone ---
You feel the ground rumble again as the distress signal leads you to a large network of subterranean tunnels. You don't have time to search them all, but you don't need to: your pack contains a set of deployable sensors that you imagine were originally built to locate lost Elves.

The sensors aren't very powerful, but that's okay; your handheld device indicates that you're close enough to the source of the distress signal to use them. You pull the emergency sensor system out of your pack, hit the big button on top, and the sensors zoom off down the tunnels.

Once a sensor finds a spot it thinks will give it a good reading, it attaches itself to a hard surface and begins monitoring for the nearest signal source beacon. Sensors and beacons always exist at integer coordinates. Each sensor knows its own position and can determine the position of a beacon precisely; however, sensors can only lock on to the one beacon closest to the sensor as measured by the Manhattan distance. (There is never a tie where two beacons are the same distance to a sensor.)

It doesn't take long for the sensors to report back their positions and closest beacons (your puzzle input). For example:

Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
So, consider the sensor at 2,18; the closest beacon to it is at -2,15. For the sensor at 9,16, the closest beacon to it is at 10,16.

Drawing sensors as S and beacons as B, the above arrangement of sensors and beacons looks like this:

               1    1    2    2
     0    5    0    5    0    5
 0 ....S.......................
 1 ......................S.....
 2 ...............S............
 3 ................SB..........
 4 ............................
 5 ............................
 6 ............................
 7 ..........S.......S.........
 8 ............................
 9 ............................
10 ....B.......................
11 ..S.........................
12 ............................
13 ............................
14 ..............S.......S.....
15 B...........................
16 ...........SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....
This isn't necessarily a comprehensive map of all beacons in the area, though. Because each sensor only identifies its closest beacon, if a sensor detects a beacon, you know there are no other beacons that close or closer to that sensor. There could still be beacons that just happen to not be the closest beacon to any sensor. Consider the sensor at 8,7:

               1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########S#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....B############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....
This sensor's closest beacon is at 2,10, and so you know there are no beacons that close or closer (in any positions marked #).

None of the detected beacons seem to be producing the distress signal, so you'll need to work out where the distress beacon is by working out where it isn't. For now, keep things simple by counting the positions where a beacon cannot possibly be along just a single row.

So, suppose you have an arrangement of beacons and sensors like in the example above and, just in the row where y=10, you'd like to count the number of positions a beacon cannot possibly exist. The coverage from all sensors near that row looks like this:

                 1    1    2    2
       0    5    0    5    0    5
 9 ...#########################...
10 ..####B######################..
11 .###S#############.###########.
In this example, in the row where y=10, there are 26 positions where a beacon cannot be present.

Consult the report from the sensors you just deployed. In the row where y=2000000, how many positions cannot contain a beacon?

Your puzzle answer was 5508234.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Your handheld device indicates that the distress signal is coming from a beacon nearby. The distress beacon is not detected by any sensor, but the distress beacon must have x and y coordinates each no lower than 0 and no larger than 4000000.

To isolate the distress beacon's signal, you need to determine its tuning frequency, which can be found by multiplying its x coordinate by 4000000 and then adding its y coordinate.

In the example above, the search space is smaller: instead, the x and y coordinates can each be at most 20. With this reduced search area, there is only a single position that could have a beacon: x=14, y=11. The tuning frequency for this distress beacon is 56000011.

Find the only possible position for the distress beacon. What is its tuning frequency?
"""
y_of_interest = 10
search_area_dim = 4_000_000
sensors = []
beacons = []

result = []

min_x = None
max_x = None

with open("Day 15 - Input.txt", 'r') as f:
    for line in f:
        s_x, s_y, b_x, b_y = map(int, line.strip().replace('Sensor at x=','').replace(' y=','').replace(': closest beacon is at x=',',').replace(' y=','').split(','))
        dist_to_b = abs(s_x-b_x) + abs(s_y-b_y)
        
        temp_min_x = min_x
        temp_max_x = max_x
        
        impacts_result = False
        if s_y <= y_of_interest and s_y + dist_to_b >= y_of_interest:
            temp_min_x = s_x - (s_y + dist_to_b - y_of_interest)
            temp_max_x = s_x + (s_y + dist_to_b - y_of_interest)
            impacts_result = True
        elif s_y >= y_of_interest and s_y - dist_to_b <= y_of_interest:
            temp_min_x = s_x - (y_of_interest - (s_y - dist_to_b))
            temp_max_x = s_x + (y_of_interest - (s_y - dist_to_b))
            impacts_result = True
            
        if temp_min_x is not None:
            if min_x is None:
                min_x = temp_min_x
            elif temp_min_x < min_x:
                result = ['.']*(min_x-temp_min_x) + result
                min_x = temp_min_x
        
        if temp_max_x is not None:
            if max_x is None:
                max_x = temp_max_x
            elif temp_max_x > max_x:
                result = result + ['.']*(temp_max_x-max_x)
                max_x = temp_max_x
            
        #print(temp_min_x, min_x, temp_max_x, max_x)
        
        if min_x is not None and max_x is not None and impacts_result:
            if result:
                result = result[0:(temp_min_x-min_x)] + ['#']*(2*(dist_to_b - abs(s_y-y_of_interest))+1) + result[temp_max_x-min_x:max_x-min_x]
                #print(result)
            else:
                result = ['#']*(max_x-min_x+1)
                #print(result)
        
        sensors.append((s_x,s_y,dist_to_b))
        if (b_x,b_y) not in beacons:
            beacons.append((b_x,b_y))
        
    for x, y in beacons:
        if y == y_of_interest and x >= min_x and x <= max_x:
            result[x-min_x] = 'B'
print('Num spaces beacon is not is: ' + str(result.count('#')))

def metro_distance(s,b): return abs(s[0]-b[0])+abs(s[1]-b[1])
    
#part 2
pos_coeffs = set()
neg_coeffs = set()
for s_x, s_y, b_dist in sensors:
    pos_coeffs.add(s_y-s_x+b_dist+1)
    pos_coeffs.add(s_y-s_x-b_dist-1)
    neg_coeffs.add(s_x+s_y+b_dist+1)
    neg_coeffs.add(s_x+s_y-b_dist-1)
    
for a in pos_coeffs:
    for b in neg_coeffs:
        int_x = (b-a)//2 #x coord of intersection
        int_y = (b+a)//2 #y coord of intersection
        if 0<=int_x<=search_area_dim and 0<=int_y<=search_area_dim:
            if all(metro_distance(s[:2], (int_x,int_y)) > s[2] for s in sensors):
                print('Distress Beacon Tuning Frequency = ', (4_000_000*int_x+int_y))