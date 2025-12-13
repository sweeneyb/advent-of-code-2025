
def is_valid(id: str) -> bool:
    length = len(id)
    if len(id) % 2 != 0:
        return True
    
    front = id[length//2:]
    back = id[:length//2]
    if front == back:
        return False
    return True

def is_valid_part_two(id: str) -> bool:
    for i in range (1, (len(id)//2)+1):
        if len(id)%i != 0:
           continue
        if is_repeated_sequence(id, i):
            return False
    return True

def is_repeated_sequence(id: str, seq_length:int) -> bool:
    for i in range (0, len(id)//seq_length):
        if id[0:seq_length] != id[i*seq_length:(i+1)*seq_length]:
            return False
    return True


def generate_next_id(file: str) -> str:
     with open(file, "r") as file:
        for line in file:
            text_range = [x.strip() for x in line.split(",")]
            for r in text_range:
                begin, end = r.split("-")
                print(f"Range: {begin} to {end}")
                for i in range (int(begin), int(end)+1):
                    yield i
    

def part_one(validator:callable):
    invalid_accumulator = 0
    # scanner = generate_next_id('input/example.txt')
    scanner = generate_next_id('input/input.txt')
    for i in scanner:
        if not validator(str(i)):
            invalid_accumulator += i
    print (invalid_accumulator)


if __name__ == "__main__":
    # part_one(validator=is_valid)
    part_one(validator=is_valid_part_two)