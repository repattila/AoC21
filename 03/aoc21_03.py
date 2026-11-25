import sys

digit_counts: list[tuple[int]] = []

with open("res/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        if len(digit_counts) == 0:
            for digit in line:
                match digit:
                    case '0':
                        digit_counts.append((1, 0))
                    case '1':
                        digit_counts.append((0, 1))
        else:
            for digit_num in range(0, len(digit_counts)):
                curr_counts = digit_counts[digit_num]
                match line[digit_num]:
                    case '0':
                        digit_counts[digit_num] = (curr_counts[0] + 1, curr_counts[1])
                    case '1':
                        digit_counts[digit_num] = (curr_counts[0], curr_counts[1] + 1)

gamma = ""
epsilon = ""
for count in digit_counts:
    if count[0] > count[1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(f"The power consumption is: {int(gamma, 2) * int(epsilon, 2)}")
