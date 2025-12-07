
def is_valid(id: str) -> bool:
    length = len(id)
    if len(id) % 2 != 0:
        return True
    
    front = id[length//2:]
    back = id[:length//2]
    if front == back:
        return False
    return True

def part_one():
    invalid_accumulator = 0
    # with open('input/example.txt', "r") as file:
    with open('input/input.txt', "r") as file:
        for line in file:
            text_range = [x.strip() for x in line.split(",")]
            for r in text_range:
                begin, end = r.split("-")
                print(f"Range: {begin} to {end}")
                for i in range (int(begin), int(end)+1):
                    if not is_valid(str(i)):
                        invalid_accumulator += i
    print (invalid_accumulator)



if __name__ == "__main__":
    part_one()