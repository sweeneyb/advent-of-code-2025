
class Interval:

    def __init__(self):
        self.intervals = []
    
    def add_interval(self, start, end):
        self.intervals.append((start, end+1))
    
    def is_in(self, number: int)-> bool:
        for (start, end) in self.intervals:
            if start < number and number < end:
                return True
        return False

def parse(file:str):
    with open(file, 'r') as file:
        interval = Interval()
        for line in file:
            yield line


def builder(generator):
    interval = Interval()
    for line in generator:
        line = line.strip()
        components = line.split('-')

        if line == "":
            break
        interval.add_interval(int(components[0]), int(components[1]))
        print(f"{line}")
    ids = []
    for line in generator:
        ids.append(int(line))
    print(f"{ids}")
    return (interval, ids)

        
            


if __name__ == "__main__":

    gen = parse('input/example.txt')
    gen = parse('input/input.txt')
    interval, ids = builder(gen)
    total = 0
    for i in ids:
        if interval.is_in(i):
            total +=1
    print(f"{total}")