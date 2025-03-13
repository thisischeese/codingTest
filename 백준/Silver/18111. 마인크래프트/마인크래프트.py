import sys

N, M, B = map(int, sys.stdin.readline().split())
land = []
for _ in range(N):
    land.extend(map(int, sys.stdin.readline().split()))

height_count = [0] * 257 
for h in land:
    height_count[h] += 1

min_time = float('inf')
optimal_height = 0


for target_height in range(257):
    remove_blocks = 0 
    add_blocks = 0

    for h in range(257):  
        if height_count[h] > 0:
            if h > target_height:
                remove_blocks += (h - target_height) * height_count[h]
            else:
                add_blocks += (target_height - h) * height_count[h]


    if remove_blocks + B >= add_blocks:
        time_needed = (remove_blocks * 2) + add_blocks
        if time_needed < min_time or (time_needed == min_time and target_height > optimal_height):
            min_time = time_needed
            optimal_height = target_height


print(min_time, optimal_height)
