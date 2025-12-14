

def read_map(file: str):
    with open(file, "r") as file:
        rows = []
        for line in file:
            row = list(line.strip())
            rows.append(row)
    return rows

def expand_borders(rows):
    height = len(rows)
    width = len(rows[0])

    new_rows = []
    top_row = []
    for i in range (0,width+2):
        top_row.append('.')
    new_rows.append(top_row)

    
    for i in range(0,height):
        new_row = ['.']
        for j in range(0,width):
            new_row.append(rows[i][j])
        new_row.append('.')
        new_rows.append(new_row)
    new_rows.append(top_row)
    
    return new_rows

def count_adjacent_rolls(board:list[list[str]], x:int, y:int) -> int:
    rolls = 0
    for i in range (x-1, x+2):
        if board[y-1][i] == '@':
            rolls += 1
        if board[y+1][i] == '@':
            rolls += 1
    if board[y][x-1] == '@':
            rolls += 1
    if board[y][x+1] == '@':
            rolls += 1
    return rolls

def count_addressable_rolls(board: list[list[str]], minimum: int, is_part_two: bool = False):
    total = 0
    for h in range (1, len(board)-1):
        row = ""
        for w in range (1, len(board[0])-1):
            if board[h][w] != '@':
                row += '.'
            elif count_adjacent_rolls(board, w, h) < minimum:
                if is_part_two:
                    board[h][w] = '.'
                total += 1
                row+='x'
            else:
                row+='@'
        print(f"{row}")
    return total

if __name__ == "__main__":

    input = read_map('input/example.txt')
    input = read_map('input/input.txt')
    board = expand_borders(input)

    #part 1
    # result = count_addressable_rolls(board, 4)
    # print(f"{result}") # 1480

    #part 2
    '''
    I think this is lucky.  Replacing a @ with . while scanning should throw off the math on the next row
    '''
    total = count_addressable_rolls(board, 4, is_part_two = True)
    this_iter = total
    while this_iter > 0:
        this_iter = count_addressable_rolls(board, 4, is_part_two = True)
        total += this_iter
    print(f"{total}") # 8899