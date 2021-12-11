from collections import deque

def read_octopuses():
    octopuses = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip('\n')
            octopuses.append([int(num) for num in line])
    return octopuses

def increase_by_one(octopuses):
    for y in range(len(octopuses)):
        for x in range(len(octopuses[0])):
            octopuses[y][x] += 1

def check_for_flash(octopuses):
    offsets = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
    flashed = set()
    to_visit = deque()
    height = len(octopuses)
    width = len(octopuses[0])

    for y in range(height):
        for x in range(width):
            if octopuses[y][x] > 9:
                to_visit.append((x,y))
    
    while(to_visit):
        x, y = to_visit.popleft()
        octopuses[y][x] = 0
        flashed.add((x, y))
        for dx, dy in offsets:
            if 0 <= x + dx < width and 0 <= y + dy < height and (x+dx, y+dy) not in to_visit:
                if octopuses[y+dy][x+dx] != 0:
                    octopuses[y+dy][x+dx] += 1
                if octopuses[y+dy][x+dx] > 9 and (x+dx, y+dy) not in flashed:
                    to_visit.append((x+dx, y+dy))
    return(len(flashed))

def update_state(octopuses):
    increase_by_one(octopuses)
    flash_count = check_for_flash(octopuses)
    return flash_count

flashes = 0
steps = 100
octopuses = read_octopuses()
for i in range(steps):
    flashes += update_state(octopuses)
print(flashes)