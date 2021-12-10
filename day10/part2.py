from collections import deque

def check_tokens(line):
    score = 0
    auto_complete = ""
    active = deque()
    lut = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    brackets = (('(',')'), ('[',']'), ('{','}'), ('<','>'))
    for token in line:
        for bracket in brackets:
            if token == bracket[0]:
                active.append(token)
            elif token == bracket[1]:
                active_bracket = active.pop()
                if active_bracket != bracket[0]:
                    return
    while(active):
        active_bracket = active.pop()
        for bracket in brackets:
            if active_bracket == bracket[0]:
                closing_bracket = bracket[1]
        auto_complete += closing_bracket
        score = (score * 5) + lut[closing_bracket]
    return score

points = 0
scores = []

with open("input.txt") as f:
    brackets = (('(',')'), ('[',']'), ('{','}'), ('<','>'))
    for line in f: 
        score = check_tokens(line)
        if score is not None:
            scores.append(score)
scores = sorted(scores)
points = scores[int((len(scores) - 1) / 2)]
            
print(points)