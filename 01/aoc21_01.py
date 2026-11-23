with open("res/input.txt", "r", encoding="utf-8") as file:
    input_vals = []
    for line in file:
        input_vals.append(int(line))

    increase_count = 0
    prev_val = None

    for window_start in range(0, len(input_vals) - 2):
        curr_val = sum(input_vals[window_start:window_start+3])
        
        if prev_val != None and prev_val < curr_val:
            increase_count += 1

        prev_val = curr_val

    print(f"The value increased {increase_count} times.")
