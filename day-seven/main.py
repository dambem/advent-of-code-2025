def read_file(file_path:str) -> list[list[str]]:
    """
    Reads a string file_path and return a list of str per new line. Suffix enforced.
    
    Args:
        file_path (str): local element filepath 
        suffix (str): string to append each file.
    Returns:
        list[str]: list of strings containing file contents.
    """
    with open(f'input/{file_path}', 'r') as file:
        clean = [str.strip(x) for x in file.readlines()]
        return clean

def count_and_cleanduplicates(list_a, dicts):
    # dicts = {}
    for n in list_a:
        # print("NUM")
        # print(f'{n}, {dicts}, {dicts.get(n)}')
        if dicts.get(n) is not None:
            dicts[n] = dicts[n] + 1
        else:
            dicts[n] = 0
    
    return list(set(list_a)), sum(dicts.values()), dicts

def main():
    test = read_file("input.txt")
    s = test[0]
    split = 0
    timelines = [s.index('S')]
    dicts = {}
    for n in range(len(test)):
        new_timelines = []
        for i in range(len(timelines)):
            rays_to_add = []
            ray = timelines[i]
            if test[n][ray] == '^':
                if ray+1 not in rays_to_add:
                    new_timelines.append(ray+1)
                if ray-1 not in rays_to_add:
                    new_timelines.append(ray-1)
                split += 1
            else:
                if ray not in rays_to_add:
                    new_timelines.append(ray)
        
        # new_list, dup, dicts = count_and_cleanduplicates(new_timelines, dicts)
        timelines = new_timelines
    print(len(timelines))
    print(split)
if __name__ == "__main__":
    main()
