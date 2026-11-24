import sys

with open("res/input.txt", "r", encoding="utf-8") as file:
    pos_v = 0
    pos_h = 0
    for line in file:
        match line.split(" "):
            case [cmd, val]:
                match cmd:
                    case "forward":
                        pos_h += int(val)
                    case "up":
                        pos_v -= int(val)
                    case "down":
                        pos_v += int(val)
                    case _:
                        print(f"Unexpected command: {cmd}")
                        sys.exit()
            case _:
                print(f"Unexpected command line: {line}")
                sys.exit()

    print(pos_v * pos_h)
