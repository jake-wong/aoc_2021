from collections import deque

# Return array of windows
def get_windows():
    windows = []
    with open("input.txt") as f:
        active_windows = deque([])
        for line in f:
            cur_num = int(line)
            new_window = []
            active_windows.append(new_window)
            if len(active_windows) > 3:
                discarded = active_windows.popleft()
                windows.append(discarded)
            for active in active_windows:
                active.append(cur_num)
        discarded = active_windows.popleft()
        windows.append(discarded)
    return windows

# Returns a list of the sum of each window
def sum_windows(windows):
    sums = []
    for window in windows:
        win_total = sum(window)
        sums.append(win_total)
    return sums

# Returns the number of values that have increased
def check_increase(list):
    increase_total = 0
    is_first = True
    for cur_num in list:
        if not is_first and cur_num > prev_num:
            increase_total += 1
        if is_first:
            is_first = False
        prev_num = cur_num
    return increase_total
    
windows = get_windows()
sums = sum_windows(windows)
increase_total = check_increase(sums)
print(increase_total)