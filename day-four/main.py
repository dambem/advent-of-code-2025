import sys 

try:
    file_path = sys.argv[1]
except IndexError:
    file_path = 'input.txt'

def read_file(file_path:str, suffix:str='X') -> list[str]:
    """
    Reads a string file_path and return a list of str per new line. Suffix enforced.
    
    Args:
        file_path (str): local element filepath 
        suffix (str): string to append each file.
    Returns:
        list[str]: list of strings containing file contents.

        test
    """
    with open(f'input/{file_path}', 'r') as file:
        return [str.strip(x)+suffix for x in file.readlines()]

def scan_nearest(x, y, file):
    
    size_x, size_y = 1, 1
    x_range = list(range(-size_x, size_x+1, 1))
    y_range = list(range(-size_y, size_y+1, 1))

    if x == 0:
        x_range.remove(-1) # don't scan behind
    if x == len(file[y]) -1:
        x_range.remove(1) # don't scan ahead
    if y == 0:
        y_range.remove(-1)
    if y == len(file) -1:
        y_range.remove(1)
    count = 0
    for y_diff in y_range:
        for x_diff in x_range:
            val =(file[y+y_diff][x+x_diff])
            if val == "@":
                count+=1
    return count

def remove_rolls(map_a):
    rolls = 0
    list_y = []
    for y in range(len(map_a)):
        list_x = []
        for x in range(len(map_a)):
            if map_a[y][x] == "@":
                c = scan_nearest(x, y, map_a)
                if c <= 4: 
                    rolls +=1
                    list_x.append('.')
                else: 
                    list_x.append("@")
            else:
                list_x.append('.')
        list_y.append(list_x)
    return rolls, list_y

if __name__ == "__main__":
    file = read_file(file_path)    
    list_y = []
    map_a = file
    rolls = 1
    rolls_total = []
    while rolls > 0:
        rolls, map_a = remove_rolls(map_a)
        rolls_total.append(rolls)
    print(sum(rolls_total))