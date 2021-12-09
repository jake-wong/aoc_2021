def get_input_output(filepath):
    inputs = []
    outputs = []
    with open(filepath) as f:
        for line in f:
            inputs.append(line.split(" | ")[0].split())
            outputs.append(line.split(" | ")[1].split())
    return inputs, outputs

def get_digits(input):
    digits = {}
    temp = input.copy()
    for pattern in input:
        key = "".join(sorted(pattern))
        if len(pattern) == 2:
            digits[key] = '1'
            temp.remove(pattern)
        elif len(pattern) == 3:
            digits[key] = '7'
            temp.remove(pattern)
        elif len(pattern) == 4:
            digits[key] = '4'
            temp.remove(pattern)
        elif len(pattern) == 7:
            digits[key] = '8'
            temp.remove(pattern)
    input = temp.copy()
    for pattern in input:
        segments = {value:key for key, value in digits.items()}
        key = "".join(sorted(pattern))
        letter_set = set(pattern)
        if len(pattern) == 5:
            # print(f"{set(segments['1'])}, {letter_set}")
            if set(segments['1']).issubset(letter_set):
                digits[key] = '3'
                temp.remove(pattern)
        elif len(pattern) == 6:
            if set(segments['4']).issubset(letter_set):
                digits[key] = '9'
                temp.remove(pattern)
            elif not set(segments['1']).issubset(letter_set):
                digits[key] = '6'
                temp.remove(pattern)
            else:
                digits[key] = '0'
                temp.remove(pattern)
    input = temp.copy()
    for pattern in input:
        segments = {value:key for key, value in digits.items()}
        key = "".join(sorted(pattern))
        letter_set = set(pattern)
        if len(pattern) == 5:
            if letter_set.issubset(set(segments['6'])):
                digits[key] = '5'
            else:
                digits[key] = '2'
    return digits

def convert(input, output):
    digits = get_digits(input)
    number = ""
    for segment in output:
        key = "".join(sorted(segment))
        number += digits[key]
    return int(number)

def get_total(inputs, outputs):
    total = 0
    for input, output in zip(inputs, outputs):
        total += convert(input, output)
    return total

inputs, outputs = get_input_output("input.txt")
print(get_total(inputs, outputs))