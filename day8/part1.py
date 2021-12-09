def get_input_output(filepath):
    inputs = []
    outputs = []
    with open(filepath) as f:
        for line in f:
            inputs.append(line.split(" | ")[0].split())
            outputs.append(line.split(" | ")[1].split())
    return inputs, outputs

def total_digits(outputs):
    total = 0
    expected_segments = [2, 3, 4, 7]
    for output in outputs:
        for digit in output:
            segments = len(digit)
            if segments in expected_segments:
                total += 1
    return total

inputs, outputs = get_input_output("input.txt")
print(total_digits(outputs))