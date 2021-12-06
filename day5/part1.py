def check_horizontal(line):
    x1 = line[0][0]
    x2 = line[1][0]
    if(x1 == x2):
        return True
    return False

def check_vertical(line):
    y1 = line[0][1]
    y2 = line[1][1]
    if(y1 == y2):
        return True
    return False

def map_ocean_floor(points, map_size):
    map = [[0 for i in range(map_size)] for j in range(map_size)]
    for line in points:
        y_coords = []
        x_coords = []
        x1, y1 = line[0]
        x2, y2 = line[1]
        if check_horizontal(line):
            if y2 < y1:
                y_coords = range(y2, y1 + 1)
            else:
                y_coords = range(y1, y2 + 1)
            for y in y_coords:
                map[y][x1] += 1
        if check_vertical(line):
            if x2 < x1:
                x_coords = range(x2, x1 + 1)
            else:
                x_coords = range(x1, x2 + 1)
            for x in x_coords:
                map[y1][x] += 1
    return map

def count_dangerous_points(map):
    count = 0
    for row in map:
        for point in row:
            if point >= 2:
                count += 1
    return count

def read_points(file_path):
    points = []
    map_size = 0
    with open(file_path) as file:
        for line in file:
            pos_1, pos_2 = line.split(" -> ")
            pos_1 = list(map(int, pos_1.split(",")))
            pos_2 = list(map(int, pos_2.split(",")))
            points.append([pos_1, pos_2])
            for pos in pos_1, pos_2:
                for value in pos:
                    if value > map_size:
                        map_size = value

    return points, map_size + 1

points, map_size = read_points("input.txt")
map = map_ocean_floor(points, map_size)
print(count_dangerous_points(map))