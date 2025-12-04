def line_generator(file_path: str):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

def get_next_digit(current:int, line: str) -> int:
    direction = line[0]
    distance = int(line[1:].strip())
    if direction == "R":
        return (current + distance) % 100
    else:
        new =  (current - distance)
        while new < 0:
            new += 100
        return new

def get_next_digit_with_cliks(current:int, line: str) -> tuple[int, int]:
    direction = line[0]
    distance = int(line[1:].strip())
    if direction == "R":
        new = current + distance
        clicks = new // 100
        new = new % 100
        return (new, clicks)
    else:
        new = current - distance
        clicks = 0
        while new < 0:
            new += 100
            clicks += 1
        if new == 0:
            clicks += 1
        if current == 0:
            clicks -=1 
        return (new, clicks)


    pass

def part_one():
    current = 50 
    count = 0
    for line in line_generator("input/input.txt"):
        current = get_next_digit(current, line)
        if current == 0:
            count += 1
    print(count)

def part_two():
    current = 50
    clicks = 0
    for line in line_generator("input/input.txt"):
    # for line in line_generator("input/example.txt"):    
        current, current_clicks = get_next_digit_with_cliks(current, line)
        # print (f"After {line} -> {current} with {current_clicks} clicks")
        clicks += current_clicks     
    print (clicks)

if __name__ == "__main__":
    # part_one() # 1071
    part_two() #6700