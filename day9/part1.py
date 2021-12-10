import copy

def read_map(file):
    map = []
    with open(file) as f:
        for line in f:
            line = line.strip("\n")
            row = [int(num) for num in line]
            map.append(row)
    return map

def check_if_lowest(map, x, y):
    offsets = [(-1,0), (1,0), (0,-1), (0,1)]
    cur_pos = map[y][x]
    surrounding_count = 0
    is_lower_count = 0
    for y_offset, x_offset in offsets:
        offset_pos = map[y + y_offset][x + x_offset]
        if offset_pos != -1:
            surrounding_count += 1
            if cur_pos < offset_pos:
                is_lower_count += 1
    if is_lower_count == surrounding_count:
        return True
    return False
    
def get_lowest_points(map):
    width = len(map[0])
    height = len(map)

    padded_map = copy.deepcopy(map)
    padded_map.insert(0, [-1 for i in range(width)])
    padded_map.append([-1 for i in range(width)])
    for row in padded_map:
        row.insert(0, -1)
        row.append(-1)
    width = len(padded_map[0])
    height = len(padded_map)

    bool_map = copy.deepcopy(map)
    total = 0
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            bool_map[y - 1][x - 1] = (padded_map[y][x], check_if_lowest(padded_map, x, y))
    return bool_map

def total_lowest_points(bool_map):
    total = 0
    for row in bool_map:
        for item in row:
            if item[1]:
                total = total + (item[0] + 1)
    return total

map = read_map("input.txt")
bool_map = get_lowest_points(map)
sum = total_lowest_points(bool_map)
print(sum)