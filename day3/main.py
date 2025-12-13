
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
    part_one()

    # 17275 is too low
    # 17447 is too high