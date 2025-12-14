def main():
    print("Hello from day-five!")
def delimit(string:str, char=','):
    return string.split(char)

def merge_overlap(arr):
    res = []
    res.append(arr[0])
    for i in range(1, len(arr)):
        last = res[-1]
        print(last)
        curr = arr[i]
        print(curr)
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)
    return res
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
        return str.strip(file.read())
if __name__ == "__main__":

    file = (read_file('test.txt'))
    a, b = (delimit(file, char="\n\n"))
    ranges = delimit(a, char="\n")
    ids = delimit(b, char="\n")
    set_vals = set()
    range_vals = []
    range_sets = []
    for n in ranges:
        start, end = delimit(n, char='-')
        range_vals.append([int(start), int(end)])
    fresh = 0
    dict_vals = {}
    range_vals.sort()
    print(range_vals)
    arr = merge_overlap(range_vals)
    print("MERGED")
    print(arr)

    diff = 0
    for i in arr:
        diff += len(range(i[0], i[1]+1))
    print(diff)
    main()
