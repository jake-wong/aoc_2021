increase_total = 0

with open("input.txt") as f:
    is_first = True
    for line in f:
        cur_num = int(line)
        if not is_first and cur_num > prev_num:
            increase_total += 1
        if is_first:
            is_first = False
        prev_num = cur_num

print(increase_total)
