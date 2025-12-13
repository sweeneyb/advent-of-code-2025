import itertools

def generate_next_id(file: str) -> str:
     with open(file, "r") as file:
        for line in file:
            yield line.strip()

def part_one():
    scanner = generate_next_id('input/example.txt')
    scanner = generate_next_id('input/input.txt')
    joltage = 0
    for i in scanner:

        biggest, bigger = get_batteries(i)
        # print(f"{i}:: {biggest.value + bigger.value} :: {biggest.index} & {bigger.index}")
        joltage += int(f"{biggest.value}{bigger.value}")
    print (joltage)


def find_max_of(substring: str, start, end):
    max_value = max(substring[start:end])
    index = substring.index(max_value, start, end)
    return index

def line_joltage(all_batteries: str, size:int) -> int:
    to_keep = size
    front = 0
    joltage = ""

    while to_keep > 0:
        idx = find_max_of(all_batteries, front, len(all_batteries)-to_keep+1 )
        joltage += all_batteries[idx]
        to_keep-=1
        front = idx+1
    print(f"{joltage}")
    return int(f"{joltage}")

def  part_two():
    scanner = generate_next_id('input/example.txt')
    scanner = generate_next_id('input/input.txt')
    joltage_agg = 0
    for i in scanner:
        joltage = line_joltage(i, 12)
        joltage_agg += int(joltage)
    print(f"total: {joltage_agg}")

class Battery:
    def __init__(self, bank, index):
        self.bank = bank
        self.index = index
        self.value = bank[index]

def get_batteries(batteries:str)-> tuple[Battery, Battery]:

    bigger = Battery(batteries, len(batteries)-1)
    biggest = Battery(batteries, len(batteries)-2)
    for i in reversed(range ( 0, len(batteries)-2,)):
        # print(f"{i}: {batteries[i]} order {biggest.value} {bigger.value}")
        if batteries[i] >= biggest.value:
            # print(f"moving ...")
            bigger = max( [biggest, bigger], key=lambda number: number.value)
            biggest = Battery(batteries, i)
        elif batteries[i] > bigger.value and i >= biggest.index:
            bigger = Battery(batteries, i)
        
    # answer = f"{biggest.value}{bigger.value}"
    # print(answer)
    # return int(answer)
    return (biggest, bigger)

if __name__ == "__main__":
    # part_one()
    # 17443 is correct

    part_two() # 172167155440541