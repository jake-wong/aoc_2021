import copy
from collections import deque

def read_map(file):
    map = []
    with open(file) as f:
        for line in f:
            line = line.strip("\n")
            row = [int(num) for num in line]
            map.append(row)
    return map

def check_surroundings(padded_map, visited, x, y):
    offsets = [(-1,0), (1,0), (0,-1), (0,1)]
    basin_points = []
    to_visit = deque(((x, y),))
    while to_visit:
        cur_x, cur_y = to_visit.popleft()
        visited.add((cur_x, cur_y))
        if padded_map[cur_y][cur_x] < 9:
            basin_points.append((cur_x, cur_y))
            for x_offset, y_offset in offsets:
                # 🤮
                if padded_map[cur_y + y_offset][cur_x + x_offset] != -1 and (cur_x + x_offset, cur_y + y_offset) not in visited and (cur_x + x_offset, cur_y + y_offset) not in to_visit:
                    to_visit.append((cur_x + x_offset, cur_y + y_offset))
    return len(basin_points)

def get_basin_score(map):
    padded_map = copy.deepcopy(map)
    padded_map.insert(0, [-1 for i in range(len(map[0]))])
    padded_map.append([-1 for i in range(len(map[0]))])
    for row in padded_map:
        row.insert(0, -1)
        row.append(-1)
    visited = set()
    to_visit = deque()
    basin_sizes = []
    width = len(padded_map[0]) - 2
    height = len(padded_map) - 1
    for y in range(1, height):
        for x in range(1, width):
            if (x, y) not in visited:
                basin_sizes.append(check_surroundings(padded_map, visited, x, y))
    basin_sizes = sorted(basin_sizes)[-3:]
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

map = read_map("input.txt")
score = get_basin_score(map)
print(score)