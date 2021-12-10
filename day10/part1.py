from collections import deque

def check_tokens(line):
    active = deque()
    lut = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    brackets = (('(',')'), ('[',']'), ('{','}'), ('<','>'))
    for token in line:
        for bracket in brackets:
            if token == bracket[0]:
                active.append(token)
            elif token == bracket[1]:
                active_bracket = active.pop()
                if active_bracket != bracket[0]:
                    return lut[token]
    return 0

points = 0

with open("input.txt") as f:
    brackets = (('(',')'), ('[',']'), ('{','}'), ('<','>'))
    for line in f: 
        points += check_tokens(line)
            
print(points)