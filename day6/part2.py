fish_states = [0 for i in range(9)]
with open("input.txt") as f:
    for value in f.read().split(","):
        fish_states[int(value)] += 1


print((fish_states))
for days in range(256):
    saved_state = 0
    for i in range(len(fish_states)):
        if i < 8:
            if i == 0:
                saved_state = fish_states[i]
                fish_states[i] = fish_states[i + 1]
            elif i == 6:
                fish_states[i] = fish_states[i + 1]
                fish_states[6] += saved_state
            else:
                fish_states[i] = fish_states[i + 1]
        elif i == 8:
            fish_states[8] = saved_state
    print(fish_states)

print(sum(fish_states))