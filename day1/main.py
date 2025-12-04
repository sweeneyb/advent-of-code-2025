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

def part_one():
    current = 50 
    count = 0
    for line in line_generator("input/input.txt"):
        current = get_next_digit(current, line)
        if current == 0:
            count += 1
    print(count)


if __name__ == "__main__":
    part_one()