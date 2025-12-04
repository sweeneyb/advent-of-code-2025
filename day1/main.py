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
        

if __name__ == "__main__":
    with open("input/input.txt", "r") as file:
    # with open("input/input.txt", "r") as file:    
        current = 50 
        count = 0
        
        for line in file:
            # print(f"Current: {current}")
            current = get_next_digit(current, line)
            if current == 0:
                count += 1
            # print(f"{line.strip()} -> {current}")
        print(count)