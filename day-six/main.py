from collections import defaultdict
import operator

def read_file(file_path:str, suffix:str='X') -> list[list[str]]:
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
        item = [str.split(x, ) for x in clean]
        return item

def vertical_tilt(lists: list[list[str]]):
    test_a = [[] for x in lists[0]]
    for n in lists:
     for i in range(len(n)):
        
        test_a[i].append(n[i])
    return test_a
def calculate(val:list[str], calc):
   op= val.pop()
   sum:int  = int(val[0])
   for n in range(1, len(val)):
      sum = calc(int(sum), int(val[n]) )
   return sum  

def switch_vals(l):
    l = l.copy()
    val_tilt = ["" for j in l]
    l_copy = l
    for j in range(len(l_copy)):
        for i in reversed(range(len(l))): 

            if len(l) == i:
                next
            if len(l[i]) == 1:
                val_tilt[j] = val_tilt[j] + l[i]
                l[i] = " "
                # l.pop(i)
            else:
                val_tilt[j] = val_tilt[j] + l[i][-1]
                l[i] = l[i][:-1]
    return(val_tilt)

def main():
    file = read_file('test.txt')
    print(file)
    vert = vertical_tilt(file)
    total = 0 
    operators = {'+': operator.add, '*': operator.mul}

    for n in vert:
       op = n.pop()
       calc  = operators[op]
       print(n)
       switch = switch_vals(n)
       print(switch)
       total += calculate(n, calc)
    return total
if __name__ == "__main__":
    print(main())
