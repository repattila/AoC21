with open("res/input.txt", "r", encoding="utf-8") as file:
    increase_count = 0
    prev_val = None

    for line in file:
        curr_val = int(line)
        if prev_val != None and prev_val < curr_val:
            increase_count += 1

        prev_val = curr_val

    print(f"The value increased {increase_count} times.")
