import re
from functools import reduce

def parse(file:str):
    with open(file, 'r') as file:
        for line in file:
            yield line.strip()


if __name__ == "__main__":

    input = parse('input/example.txt')
    input = parse('input/input.txt')
    problems = []
    firstLine = True
    for line in input:
        line = re.sub(r"\s+", " ", line)
        # print(line)
        
        itmes = line.split(' ')
        if firstLine:
            for item in itmes:
                if item == '':
                    continue
                # print(item)
                problems.append([int(item)])
            firstLine = False
        else:
            if any(ext in line for ext in ['*', '+']):
                print(line)
                result = 0
                items = line.split(' ')
                for idx, op in enumerate(items):
                    print(f"op: {op}")
                    match op:
                        case '*':
                          problemAnswer = 0
                          print(problems[idx])
                          problemAnswer = reduce(lambda x, y: x * y, problems[idx])
                          print(f"Problem {idx+1} answer: {problemAnswer}")
                        case '+':
                          problemAnswer = 0
                          print(problems[idx])
                          problemAnswer = reduce(lambda x, y: x + y, problems[idx])
                          print(f"Problem {idx+1} answer: {problemAnswer}") 
                    result += problemAnswer  
                pass
            else:
                for i in range(len(itmes)):
                    problems[i].append(int(itmes[i]))
    # print(problems)
    print(result)


