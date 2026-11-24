import sys

with open("res/input.txt", "r", encoding="utf-8") as file:
    pos_v: int = 0
    pos_h: int = 0
    aim: int = 0
    for line in file:
        match line.split(" "):
            case [cmd, val]:
                match cmd:
                    case "forward":
                        intval = int(val)
                        pos_h += intval
                        pos_v += intval * aim
                    case "up":
                        aim -= int(val)
                    case "down":
                        aim += int(val)
                    case _:
                        print(f"Unexpected command: {cmd}")
                        sys.exit()
            case _:
                print(f"Unexpected command line: {line}")
                sys.exit()

    print(pos_v * pos_h)
