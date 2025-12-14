def main():
    print("Hello from day-eight!")
def delimit(string:str, char=','):
    return string.split(char)

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
        clean = [delimit(str.strip(x)) for x in file.readlines()]
        return clean[0]

def euclidian_distance(x, y):
    sum = 0
    for i in range(len(x)):
        sum += (int(x[i]) - int(y[i]))**2
    return float(sum)**0.5
    # dist = ()

if __name__ == "__main__":
    test = read_file('input.txt')
    # print(test)
    a = test[0]
    b = test[1]
    # print(euclidian_distance(a, b))
    for a in range(len(test)):
        distance = euclidian_distance(test[a], a[1])
        for b in range(len(b)):
            if a == b:
                next
            